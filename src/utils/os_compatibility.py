import platform
import os

class OSCompatibility:
    @staticmethod
    def get_os():
        return platform.system()

    @staticmethod
    def is_valid_disk(disk_path):
        return os.path.exists(disk_path)

    @staticmethod
    def get_smart_data(disk_path):
        # Implement OS-specific SMART data retrieval
        pass

    @staticmethod
    def get_disk_space(disk_path):
        # Implement OS-specific disk space retrieval
        pass

    @staticmethod
    def measure_disk_performance(disk_path):
        # Implement OS-specific disk performance measurement
        pass

    @staticmethod
    def has_gui():
        return True  # Implement actual check if needed
