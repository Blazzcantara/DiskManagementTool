import logging
from src.utils.error_handler import handle_error
from src.utils.os_compatibility import OSCompatibility

logger = logging.getLogger(__name__)

class BackupModule:
    @handle_error
    def create_full_backup(self, source, destination):
        logger.info(f"Creating full backup from {source} to {destination}")
        # Implement backup logic here
        return "Backup path"

    @handle_error
    def create_incremental_backup(self, source, destination, last_backup):
        logger.info(f"Creating incremental backup from {source} to {destination}")
        # Implement incremental backup logic here
        return "Incremental backup path"
