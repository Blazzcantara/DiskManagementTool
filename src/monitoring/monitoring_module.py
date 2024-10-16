import logging
import threading
from src.utils.error_handler import handle_error

logger = logging.getLogger(__name__)

class MonitoringModule:
    def __init__(self):
        self.stop_flag = threading.Event()

    @handle_error
    def start_monitoring(self, disk_path):
        logger.info(f"Starting monitoring for disk: {disk_path}")
        # Implement monitoring logic here
        self.stop_flag.clear()
        # Start a monitoring thread here

    def stop_monitoring(self):
        logger.info("Stopping monitoring")
        self.stop_flag.set()
