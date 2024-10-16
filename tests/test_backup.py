import unittest
from src.backup.backup_module import BackupModule

class TestBackupModule(unittest.TestCase):
    def setUp(self):
        self.backup_module = BackupModule()

    def test_create_full_backup(self):
        result = self.backup_module.create_full_backup("/source", "/destination")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
