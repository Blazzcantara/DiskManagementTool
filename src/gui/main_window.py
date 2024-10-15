# ... (previous content)
from src.backup.backup_module import create_backup, list_backups

class MainWindow(QMainWindow):
    # ... (previous methods)

    def setup_backup_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        create_backup_button = QPushButton("Create Backup")
        create_backup_button.clicked.connect(self.create_backup)
        layout.addWidget(create_backup_button)
        
        list_backups_button = QPushButton("List Backups")
        list_backups_button.clicked.connect(self.list_backups)
        layout.addWidget(list_backups_button)
        
        self.backup_result_label = QLabel()
        layout.addWidget(self.backup_result_label)
        
        self.tabs.addTab(tab, "Backup")

    def create_backup(self):
        source = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        if source:
            destination = QFileDialog.getExistingDirectory(self, "Select Backup Destination")
            if destination:
                result = create_backup(source, destination)
                self.backup_result_label.setText(str(result))

    def list_backups(self):
        backup_dir = QFileDialog.getExistingDirectory(self, "Select Backup Directory")
        if backup_dir:
            result = list_backups(backup_dir)
            self.backup_result_label.setText(str(result))

# ... (rest of the file)
