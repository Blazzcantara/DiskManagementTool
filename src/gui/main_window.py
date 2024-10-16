from PyQt5.QtWidgets import QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self, tool):
        super().__init__()
        self.tool = tool
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Disk Management Tool")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        tab_widget = QTabWidget()
        layout.addWidget(tab_widget)

        tab_widget.addTab(self.create_analysis_tab(), "Analysis")
        tab_widget.addTab(self.create_backup_tab(), "Backup")
        tab_widget.addTab(self.create_recovery_tab(), "Recovery")
        tab_widget.addTab(self.create_repair_tab(), "Repair")
        tab_widget.addTab(self.create_monitoring_tab(), "Monitoring")

    def create_analysis_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)

        analyze_button = QPushButton("Analyze Disk")
        analyze_button.clicked.connect(self.analyze_disk)
        layout.addWidget(analyze_button)

        self.analysis_result = QLabel("Analysis Result:")
        layout.addWidget(self.analysis_result)

        return tab

    def analyze_disk(self):
        disk_path, _ = QFileDialog.getOpenFileName(self, "Select Disk")
        if disk_path:
            result = self.tool.analysis_module.analyze_disk(disk_path)
            self.analysis_result.setText(str(result))

    # Implement other tabs similarly
