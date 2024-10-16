import sys
import logging
from PyQt5.QtWidgets import QApplication
from src.gui.main_window import MainWindow
from src.analysis.analysis_module import AnalysisModule
from src.backup.backup_module import BackupModule
from src.recovery.recovery_module import RecoveryModule
from src.repair.repair_module import RepairModule
from src.monitoring.monitoring_module import MonitoringModule
from src.utils.logging_config import setup_logging
from src.utils.os_compatibility import OSCompatibility

class DiskManagementTool:
    def __init__(self):
        setup_logging()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing Disk Management Tool")

        self.analysis_module = AnalysisModule()
        self.backup_module = BackupModule()
        self.recovery_module = RecoveryModule()
        self.repair_module = RepairModule()
        self.monitoring_module = MonitoringModule()

    def run_gui(self):
        self.logger.info("Starting GUI application")
        app = QApplication(sys.argv)
        main_window = MainWindow(self)
        main_window.show()
        sys.exit(app.exec_())

    def run_cli(self):
        self.logger.info("Starting CLI application")
        while True:
            command = input("Enter command (analyze/backup/recover/repair/monitor/exit): ").lower()
            if command == 'exit':
                break
            self.process_command(command)

    def process_command(self, command):
        if command == 'analyze':
            disk = input("Enter disk path to analyze: ")
            result = self.analysis_module.analyze_disk(disk)
            print(result)
        elif command == 'backup':
            source = input("Enter source path: ")
            destination = input("Enter destination path: ")
            result = self.backup_module.create_full_backup(source, destination)
            print(f"Backup created at: {result}")
        # Implement other commands similarly

if __name__ == "__main__":
    tool = DiskManagementTool()
    if OSCompatibility.has_gui():
        tool.run_gui()
    else:
        tool.run_cli()
