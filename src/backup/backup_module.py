import os
import shutil
from datetime import datetime

def create_backup(source, destination):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(destination, f"backup_{timestamp}")
        shutil.copytree(source, backup_path)
        return {'status': 'success', 'backup_path': backup_path}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def list_backups(backup_dir):
    try:
        backups = [d for d in os.listdir(backup_dir) if d.startswith("backup_")]
        return {'status': 'success', 'backups': backups}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
