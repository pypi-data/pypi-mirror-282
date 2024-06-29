import os
from os.path import join as pjoin
import logging
import datetime
import traceback
from sys import exit
import pandas as pd
import atexit
import inspect
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import functools
import time
import json
from .locker_util import LockManager


LOG_SYSTEM_VERSION="1.3.3"
LOG_TIME_STAMP_FMT = '_%y%m%d_%H%M%S'
CACHE_LOG_DIR="./cache_log"
CACHE_LOG_TIME_STAMP_FMT='_%y%m%d'
NOTIFICATION_DIR=pjoin(os.path.dirname(os.path.abspath(__file__)), "notification")
LOG_FORMAT="%(asctime)s - %(caller_func_name)s - %(levelname)s - %(message)s"
os.makedirs(NOTIFICATION_DIR, exist_ok=True)

class Logger:
    _instance = None

    def __new__(cls, task_entry=None, cache_log_folder=None):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_registry = {}
            cls._instance.cache_log = cls.create_cache_log(cache_log_folder=cache_log_folder)
            cls._instance.task_entry = None
            cls._instance.task_type = "Default"
            cls._instance.default_folder = None
            cls._instance.notification_location = NOTIFICATION_DIR
            cls._instance.alert_level = -1

        return cls._instance
    

    @staticmethod
    def create_cache_log(cache_log_folder=None):
        cache_log_name="DEFAULT_CACHE_LOG"
        
        if cache_log_folder is None:
            mod_path = os.path.dirname(os.path.abspath(__file__))
            cacke_log_dir_path = pjoin(mod_path, CACHE_LOG_DIR) if CACHE_LOG_DIR.startswith("./") else CACHE_LOG_DIR
        else:
            print(f"Cache log inited at {cache_log_folder}")
            cacke_log_dir_path = cache_log_folder

        if cache_log_name not in logging.Logger.manager.loggerDict:     
            print(f"         -------- Initializing cache log at {cacke_log_dir_path}")
            os.makedirs(cacke_log_dir_path, exist_ok=True)
            _logger, _file_handler = Logger.init_log(
                cache_log_name, 
                "cache_log_on", 
                cacke_log_dir_path,
                level=logging.DEBUG, 
                time_stamp=True,
                log_fmt=LOG_FORMAT
            )
            atexit.register(Logger.close_log, _logger, _file_handler, cache_log_name)    
        return _logger


    @staticmethod
    def init_log(log_name, log_file_name, log_fd_path, level=logging.DEBUG, time_stamp=True, log_fmt='%(asctime)s - %(caller_func_name)s - %(levelname)s - %(message)s'):
        def get_time_stamp(log_file_name, log_fd_path, time_stamp):
            max_time = ""
            if not time_stamp:
                return max_time
            
            if time_stamp=="_Init":
                for filename in os.listdir(log_fd_path):
                    match = re.match(rf"{log_file_name}(_\d{{6}}_\d{{6}}).log", filename)
                    if match:
                        cur_time = match.group(1)
                        if not max_time or cur_time > max_time:
                            max_time = cur_time
                            
            if max_time:
                return max_time
            else:
                return datetime.datetime.now().strftime(LOG_TIME_STAMP_FMT)
            
        cur_time = get_time_stamp(log_file_name, log_fd_path, time_stamp)
        
        
        if len(log_file_name) > 4 and log_file_name.endswith(".log"):
            log_file_name = log_file_name[:-4]

        log_file_path = pjoin(log_fd_path, f"{log_file_name}{cur_time}.log")

        assert os.path.isdir(log_fd_path), f"{log_fd_path} is not a folder"
        logger = logging.getLogger(log_name)
        logger.setLevel(level)

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(log_fmt))

        logger.addHandler(file_handler)
        
        # Store the original methods
        original_info = logger.info
        original_debug = logger.debug
        original_warning = logger.warning
        original_error = logger.error
        original_critical = logger.critical
        logger.log_file_path=log_file_path

        def split_kwargs(**kwargs):
            log_kwargs = {key[5:]: value for key, value in kwargs.items() if key.startswith('_log_')}
            other_kwargs = {key: value for key, value in kwargs.items() if not key.startswith('_log_')}
            return log_kwargs, other_kwargs

        def get_log_string(*args, **kwargs):
            modified_args = []
            for arg in args:
                if isinstance(arg, pd.DataFrame):
                    # Convert DataFrame to string with added lines
                    spliter="\n--------------------------------------\n"
                    df_str =  spliter + arg.to_string(max_rows=kwargs.get("max_rows", 10), max_cols=kwargs.get("max_cols", 10), max_colwidth=kwargs.get("max_colwidth", 35), show_dimensions=True) + spliter
                    modified_args.append(df_str)
                elif isinstance(arg, dict):
                    spliter="\n- - - - - - - - - - - - - - - - - - - \n"
                    rows = []
                    for k, v in arg.items():
                        rows.append({'key': k, 'value': v})

                    df_str = spliter + pd.DataFrame(rows).to_string(max_rows=kwargs.get("max_rows", 10), max_cols=kwargs.get("max_cols", 10), max_colwidth=kwargs.get("max_colwidth", 35), show_dimensions=True) + spliter
                    modified_args.append(df_str)
                elif isinstance(arg, float):
                    modified_args.append("{:.6f}".format(arg).rstrip('0'))
                else:
                    modified_args.append(str(arg))

            msg = ' '.join(modified_args)
            return msg
        
        def read_log_file(file_path, severity_level=logging.WARNING):
            """Function to read a log file and return contents that meet or exceed the given severity level."""
            severity_map = {
                'CRITICAL': logging.CRITICAL,
                'ERROR': logging.ERROR,
                'WARNING': logging.WARNING,
                'INFO': logging.INFO,
                'DEBUG': logging.DEBUG
            }
            filtered_contents = []
            with open(file_path, 'r') as file:
                for line in file:
                    try:
                        log_level_name = line.split('-')[4].strip()
                        if severity_map[log_level_name] >= severity_level:
                            filtered_contents.append(line.strip())
                    except IndexError:
                        continue
                    except Exception as e:
                        print(e)
                        continue
            return "\n".join(filtered_contents)
            
        def draft_critical_alert_email(msg, **kwargs):
            email_json_lock=LockManager("email_json_lock")
            email_json_lock.get_lock(wait=True)

            history_message=""
            if kwargs.get("no_phi", False) and kwargs.get("append_log", False):
                if "log_file_path" in kwargs:
                    history_message="\n\nHistory Message:\n"+read_log_file(kwargs["log_file_path"])
                else:
                    print("Unexpect log attributes, cannot send critical alert email")

            alert_folder=pjoin(NOTIFICATION_DIR, "CriticalAlert")
            os.makedirs(alert_folder,exist_ok=True)
            json_filename=f"Alert_Critical_{datetime.datetime.now().strftime(LOG_TIME_STAMP_FMT)}.json"
            with open(pjoin(alert_folder, json_filename), "a") as f:
                json.dump({
                    "subject": "MCheck ClinicalHOS - " + kwargs.get("subject", "Critical Alert Information"),
                    "body": msg+history_message,
                    "timestamp": datetime.datetime.now().strftime(LOG_TIME_STAMP_FMT)
                }, f, indent=4)
            email_json_lock.release_lock()


        # Modify the logging methods for any number of arguments
        def modified_log_method(original_method, *args, **kwargs):
            func_name = inspect.stack()[2].function
            log_kwargs, kwargs=split_kwargs(**kwargs)
            msg=get_log_string(*args, **log_kwargs)
            original_method(msg, extra={'caller_func_name': func_name}, **kwargs)
            if original_method.__name__=="critical":
                draft_critical_alert_email(msg, **log_kwargs)
        

        logger.info = lambda *args, **kwargs: modified_log_method(original_info, *args, **kwargs)
        logger.debug = lambda *args, **kwargs: modified_log_method(original_debug, *args, **kwargs)
        logger.warning = lambda *args, **kwargs: modified_log_method(original_warning, *args, **kwargs)
        logger.error = lambda *args, **kwargs: modified_log_method(original_error, *args, **kwargs)
        logger.critical = lambda *args, **kwargs: modified_log_method(original_critical, *args, **{**kwargs, '_log_log_file_path': logger.log_file_path})

        # Create 'p' prefixed methods that will log and then print
        def print_and_log_method(original_method, *args, **kwargs): 
            func_name = inspect.stack()[2].function
            log_kwargs, kwargs=split_kwargs(**kwargs)
            msg=get_log_string(*args, **log_kwargs)
            original_method(msg, extra={'caller_func_name': func_name}, **kwargs)
            print(msg)
            if original_method.__name__=="critical":
                draft_critical_alert_email(msg, **log_kwargs)

        logger.pinfo = lambda *args, **kwargs: print_and_log_method(original_info, *args, **kwargs)
        logger.pdebug = lambda *args, **kwargs: print_and_log_method(original_debug, *args, **kwargs)
        logger.pwarning = lambda *args, **kwargs: print_and_log_method(original_warning, *args, **kwargs)
        logger.perror = lambda *args, **kwargs: print_and_log_method(original_error, *args, **kwargs)
        logger.pcritical = lambda *args, **kwargs: print_and_log_method(original_critical, *args, **{**kwargs, '_log_log_file_path': logger.log_file_path})

        return logger, file_handler

    @staticmethod
    def close_log(logger, file_handler, log_name):
        file_handler.close()
        logger.removeHandler(file_handler)
        del logging.Logger.manager.loggerDict[log_name]

    def set_entry(self, task_entry=None, task_type=None, default_folder=None, notification_location=None, alert_level=-1):
        if self.task_entry is None and task_entry is not None:
            self.task_entry = task_entry
        if self.default_folder is None and default_folder is not None:
            self.default_folder = default_folder
        if self.notification_location is None and notification_location is not None:
            self.notification_location=notification_location
        if self.task_type=="Default" and task_type is not None:
            self.task_type=task_type
        if self.alert_level==-1 and alert_level is not None:
            self.alert_level=alert_level


    def log_system(self, log_name, _log_file_name, _log_fd_path, level=logging.DEBUG, ignore_check=False, time_stamp=True, verbose=False, on_call=[]):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                def check_logger_existence(log_name, ignore_check=False):
                    segments = log_name.split(".")
                    current_name = ""
                    
                    for i, segment in enumerate(segments[:-1]):
                        current_name = f"{current_name}.{segment}" if current_name else segment
                        
                        if current_name not in logging.Logger.manager.loggerDict:
                            if ignore_check:
                                return ".".join(segments[:i] + ["__".join(segments[i:])])
                            else:
                                raise AssertionError(f"Incorrect flow for log **{current_name}**, the parent log file hasn't created yet or is no longer alive")
                    
                    if log_name in logging.Logger.manager.loggerDict:
                        raise AssertionError("Logger already inited")
                    return log_name

                def clean_error_msg(traceback_str):
                    lines = traceback_str.split('\n')
                    filtered_lines = [line for i, line in enumerate(lines) if "log_system_util" not in line \
                            and (i == 0 or "log_system_util" not in lines[i - 1])]
                    return '\n'.join(filtered_lines)

                nonlocal log_name
                nonlocal _log_file_name
                nonlocal _log_fd_path
                nonlocal level
                nonlocal ignore_check
                assert isinstance(on_call, list), "on_call variable should be a list"
                
                log_name=check_logger_existence(log_name, ignore_check)

                self.log_registry[func.__name__] = log_name
                
                log_fd_path=self.default_folder if _log_fd_path=="Default" else _log_fd_path
                if log_fd_path is None:
                    log_fd_path = kwargs.pop('ovr_log_fd_path', None)
                assert log_fd_path is not None, "No valid log_fd_path/ovr_log_fd_path given"
                
                log_file_name=_log_file_name
                if not log_file_name:
                    log_file_name = kwargs.pop('ovr_log_file_name', None)
                assert log_file_name is not None, "No valid log_file_name/ovr_log_file_name given"
                
                os.makedirs(log_fd_path, exist_ok=True)
                _logger, _file_handler = self.init_log(
                    log_name, log_file_name, log_fd_path, level=level, time_stamp=time_stamp)
                if verbose:
                    print(f"         -------- log *{log_name}* initialized at {log_fd_path}")
                
                error_status=False
                try:
                    kwargs.pop('log', None)
                    kwargs['log'] = _logger
                    return func(*args, **kwargs)
                except Exception as e:
                    error_status=True
                    _logger.perror(f"For task_entry: {self.task_entry}")
                    _logger.perror(f"Uncatched Error: {e}")
                    tb_str = clean_error_msg(traceback.format_exc())
                    _logger.perror(f"traceback info : {tb_str}")

                    if self.alert_level>=0:
                        alert_folder=pjoin(self.notification_location, self.task_type)
                        os.makedirs(alert_folder,exist_ok=True)
                        email_json_lock=LockManager("email_json_lock")
                        email_json_lock.get_lock(wait=True)
                        json_filename=f"Failure_{self.task_entry}_{datetime.datetime.now().strftime(LOG_TIME_STAMP_FMT)}.json"
                        with open(pjoin(alert_folder, json_filename), "a") as f:
                            json.dump({
                                "subject": self.task_entry,
                                "body": tb_str,
                                "timestamp": datetime.datetime.now().strftime(LOG_TIME_STAMP_FMT)
                            }, f, indent=4)
                        email_json_lock.release_lock()
                        
                finally:
                    if func.__name__ in self.log_registry:
                        del self.log_registry[func.__name__]
                    Logger.close_log(_logger, _file_handler, log_name)
                    if verbose:
                        print(f"         ^^^^^^^^ log *{log_name}* successfully closed")
                    if error_status:
                        exit(1)
            return wrapper
        return decorator
    
    
    def get_log(self, _log_name, _dev=False):
        def decorator(func):
            def wrapper(*args, **kwargs):
                def get_potential_log_names(original_name):
                    if original_name in logging.Logger.manager.loggerDict:
                        return original_name
                    
                    # Replace from the last dot and so forth
                    segments = original_name.split(".")
                    for i in range(2, len(segments)+1):
                        potential_name=".".join(segments[:-i] +[ "__".join(segments[-i:])])
                        if potential_name in logging.Logger.manager.loggerDict:
                            return potential_name
                    assert False, f"Incorrect flow, the log file *{original_name}*not created"
                nonlocal _log_name
                nonlocal _dev
                
                log_name = _log_name
                if log_name is None:
                    log_name=kwargs.pop('ovr_log_name', None)    
                elif log_name == "_Inherit":
                    partent_func_name = inspect.stack()[1].function
                    if func.__name__ in self.log_registry and func.__name__!=partent_func_name:
                        assert False, f"Multi functions calls {func.__name__} simultaneously"
                    log_name = self.log_registry.get(partent_func_name, None)
                else:
                    log_name=get_potential_log_names(log_name)
                    
                self.log_registry[func.__name__] = log_name
                # Check if we need cache log.
                if log_name is not None:
                    _log = logging.getLogger(log_name)
                else:
                    if not _dev:
                        print("!!! Warning No static log_name or pass a valid ovr_log_name given")
                        print(f"   For function: {func.__name__}\nArgs: {args}\nKwargs: {kwargs}\n")
                    _log = self.cache_log
                try:
                    return func(*args, log=_log, **kwargs)
                finally:
                    del self.log_registry[func.__name__]
            return wrapper
        return decorator
     
    def helper(self, width=None):
        def display_format_dict(info_name, dic, cols=["Version", "Updates"]):
            k_sz = 50
            v_sz = 120 if width is None else width
            _rows = []
            for k, v in dic.items():
                _rows.append({cols[0]: k, cols[1]: v})


            fmt_row = [f"{'':3}  {cols[0]:<{k_sz}} {cols[1]:<{v_sz}}", "\n"]
            for idx, (k, v) in enumerate(dic.items()):
                fmt_row.append(f"{idx:<3}  {k[:k_sz]:<{k_sz}} {v[:v_sz]:<{v_sz}}")
                p = v_sz
                while p <= len(v):
                    fmt_row.append(f"{'':<3}  {'':<{k_sz}} {v[p:p+v_sz]:<{v_sz}}")
                    p += v_sz

            df_str = "\n"+"- "*10 + f"\n{info_name}:\n" + \
                "\n".join(fmt_row) + "\n"
            print(df_str)
            return df_str

        version_info = {
            "1.1.3": "Raise error back; Merge Assertion error to Uncatched error; add instrution and log_helper function, add run time log instance fetch.",
            "1.1.4": "Added cache log folder to handle unexpected life cycle issue; Reverse/cancel the error raise.",
            "1.1.5": "Update cache log time stamp; Update cache log folder path; Update file handler tracker.",
            "1.1.6": "Add automatic function name flag for cache log.",
            "1.1.7": "Add automatic function name flag to all records. Add dev option for cache log.",
            "1.2.0": "Change the log system to class structure.",
            "1.2.1": "Support _inherit method for get_log in order to make the use of log system convinient.",
            "1.2.2": "Support unique cache log and handle incorrect _inherit log by cache log.",
            "1.2.3": "Support default log folder name and add task_entry variable for future features.",
            "1.2.4": "Add email report and on-call mechanism.",
            "1.2.5": "Add email credential configurable.",
            "1.2.6": "Support nested log system. Error trace when we get in correct log flow.",
            "1.2.7": "Cache log location configurable. Email alert level and frequency configurable.",
            "1.2.8": "Allow send an email to multiple recipients.",
            "1.2.9": "Add kwargs for log message to control DataFrame & Dictionary elements printed shape.",
            "1.3.0": "Split out email system to notification system. Optimize error message. Add task_type to align notification system",
            "1.3.1": "Clean the set entry function",
            "1.3.2": "Add automatic alerting email merchanism for critinal message and configurable subject",
            "1.3.3": "Add new parameters _log_no_phi and _log_append_log for critical message email to attach the hitorical log message."
        }

        usage_info = {
            "Initialize log class first:": "logger=Logger()",
            "Initialize a log instance": "@logger.log_system(log_name, _log_file_name, _log_fd_path, level=logging.DEBUG, ignore_check=False, time_stamp=True, verbose=False, on_call=['yinghao.li@hilabs.com'])",
            "Write info to an existing log instance": "@logger.get_log(log_name)",
            "Write info to cache log for developing and debuging": "@logger.get_log(None)",
            "Write info to the log file same to the parent function": '@logger.get_log("_Inherit")',
            "Write infomatrion to log file only": "log.debug(), log.info(), log.warning(), log.error(), log.critical()",
            "Print infomatrion then write to log file": "log.pdebug(), log.pinfo(), log.pwarning(), log.perror(), log.pcritical()",
            "Set default folder to avoid pass folder name everywhere": "logger.set_entry(default_folder='')",
        }

        usage_example = {
            "First we always need to initialize log class:": "logger=Logger()",
            "log_system with static folder and file name": "@logger.log_system('root_log', 'test_log', './log_files')",
            "log_system with runtime folder": "@logger.log_system('root_log', 'test_log', None)def func(log=None) <==> func(ovr_log_fd_path='../logs')",
            "log_system with default folder": "@logger.log_system('root_log', 'Default', None)def func(log=None)",
            "log_system with runtime file name": "@logger.log_system('root_log', None, './log_files')def func(log=None) <==> func(ovr_log_file_name='new_log')",
            "Using existing log": "@logger.get_log('root_log')def sub_func(log=None)",
            "Set default folder for log system": "logger.set_entry(task_entry='dq_check', default_folder='/usr/ec2/cdi/logs', task_on_call=['yinghao.li@hilabs.com'])"
        }

        parameter_info = {
            "log_name": "The name of log instance, used as identifier, use .(dot) to indicate a sub_log/child of a like (e.g. root.leaf where root.leaf is a child log instance of root), all message to a log instance will also get passed to its parent log instance automatically",
            "log_file_name": "Name of log file attached to the log instance (same log_name may have difference log_file_name when log instance are not runing at the same time)",
            "log_fd_path": "Path of a folder to save log files (same log_name may have difference log_fd_path when log instance are not runing at the same time)",
            "level (defalut=logging.DEBUG)": "Level of the log instance, only message equal or higher to this level will be write/saved to the log file. Levels: [DEBUG, INFO, WARNING, ERROR, CRITICAL]",
            "ignore_check (defalut=False)": "Set this to True allows build children log without existing of parent logs, Do not use this with ovr_log_name simultaneously",
            "time_stamp (defalut=True)": "Whether the log file name will be appeneded with time_stamp of creation",
            "verbose (defalut=False)": "Whether to print detail & progress information of log system/instance",
            "ovr_log_fd_path": "This is a paramter can be used when calling the function with @log_system, if _log_fd_path is set to None, then we use this variable as the folder path for log files.",
            "ovr_log_file_name": "This is a paramter can be used when calling the function with @log_system, if _log_file_name is set to None, then we use this variable as the log file name to create the log instance.",
            "ovr_log_name": "This is a paramter can be used when calling the function with @get_log, if log_name is set to None, then we use this variable to fetch the existing log instance. This will disable the ignore_check parameter for @log_system"
        }

        display_format_dict("Version Info", version_info)
        display_format_dict("Usage Info", usage_info, cols=["Usage", "Code"])
        display_format_dict("Usage Examples", usage_example, cols=["Scenario ", "Code"])
        display_format_dict("Parameter Info", parameter_info,
                            cols=["Parameter", "Explanation"])

    

    


