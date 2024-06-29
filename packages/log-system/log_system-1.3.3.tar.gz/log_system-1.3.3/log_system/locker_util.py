import fasteners
from os.path import join as pjoin
import os

LOCK_MANAGER_VERSION="1.0.3"
DEFAULT_LOCK_DIR=pjoin(os.path.dirname(os.path.abspath(__file__)), "locks")
os.makedirs(DEFAULT_LOCK_DIR, exist_ok=True)

class LockManager:
    """
    LockManager is a utility class for handling inter-process locks
    to prevent concurrent access to shared resources in a multi-process
    environment. It uses the fasteners library to manage locks using
    file-based locking.
    
    Attributes:
        lock (fasteners.InterProcessLock): The lock object used for synchronization.

    Usage:
        wait=False: immediate return True(lock get) or False
        wait=True: keep waiting until lock get or interrupt, then return True(lock get) or False
        wait=10(or any int/float): keep waiting until lock get or 10 seconds passed, then return True(lock get) or False
    """
    
    def __init__(self, lock_name, verbose=True):
        """
        Initializes a LockManager instance.

        Args:
            lock_name (str): A unique name identifier for the lock.
        """
        # Load configuration properties and determine the lock file path
        lock_folder_path = DEFAULT_LOCK_DIR
        
        # Construct the full path for the lock file
        lock_path = pjoin(lock_folder_path, f"lock_{lock_name}")
        
        # Create an inter-process lock object
        self.lock = fasteners.InterProcessLock(lock_path)
        self.verbose = verbose
        self.lock_name=lock_name

    def get_lock(self, wait=False):
        """
        Attempts to acquire the lock.

        Args:
            wait (bool): If True, the call will block until the lock is acquired.
                         If False, the call will immediately return False if the
                         lock is not available (non-blocking).
                         
        Returns:
            bool: True if the lock was acquired, False otherwise.
        """
        if isinstance(wait, bool):
            blocking = wait
            timeout = None
        elif isinstance(wait, int) or isinstance(wait, float):  # Supports int or float for timeout
            blocking = True
            timeout = wait
        
        # Attempt to acquire the lock with the specified blocking behavior
        if self.lock.acquire(blocking=blocking, timeout=timeout):
            if self.verbose:
                print(f"{self.lock_name} Lock ACQUIRED.")
            return True
        else:
            if self.verbose:
                print(f"Could not acquire the lock for {self.lock_name}")
            return False

    def release_lock(self):
        """
        Releases the lock if it is currently held by this LockManager instance.
        """
        # Release the lock and log the action
        try:
            self.lock.release()
            print(f"{self.lock_name} Lock RELEASED.")
        except:
            print(f"{self.lock_name} Lock was not locked.")
        

    def verify_lock(self):
        """
        Check if lock is locked.
        """
        # Release the lock and log the action
        if self.lock.acquire(blocking=False, timeout=None):
            self.lock.release()
            return True
        else:
            return False

    version_info = {
            "1.0.1": "Added Version Control. Added Lock Name",
            "1.0.2": "Handled lock release error when lock not locked",
            "1.0.3": "Moved Module under log system"}



        