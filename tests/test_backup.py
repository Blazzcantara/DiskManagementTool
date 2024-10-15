import unittest
import tempfile
import os
import shutil
from src.backup.backup_module import create_backup, list_backups

class TestBackup(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.source_dir = os.path.join(self.temp_dir, "source")
        self.backup_dir = os.path.join(self.temp_dir, "backup")
        os.mkdir(self.source_dir)
        os.mkdir(self.backup_dir)
        
        # Create a test file
        with open(os.path.join(self.source_dir, "test_file.txt"), "w") as f:
            f.write("Test content")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_create_backup(self):
        result = create_backup(self.source_dir, self.backup_dir)
        self.assertEqual(result['status'], 'success')
        self.assertTrue(os.path.exists(result['backup_path']))

    def test_list_backups(self):
        create_backup(self.source_dir, self.backup_dir)
        result = list_backups(self.backup_dir)
        self.assertEqual(result['status'], 'success')
        self.assertEqual(len(result['backups']), 1)

if __name__ == '__main__':
    unittest.main()
