import logging
from src.utils.error_handler import handle_error, AnalysisError
from src.utils.os_compatibility import OSCompatibility

logger = logging.getLogger(__name__)

class AnalysisModule:
    @handle_error
    def analyze_disk(self, disk_path):
        logger.info(f"Starting analysis of disk: {disk_path}")
        
        if not OSCompatibility.is_valid_disk(disk_path):
            raise AnalysisError(f"Invalid disk path: {disk_path}")

        smart_data = OSCompatibility.get_smart_data(disk_path)
        space_analysis = OSCompatibility.get_disk_space(disk_path)
        performance_metrics = OSCompatibility.measure_disk_performance(disk_path)
        
        logger.info(f"Analysis complete for disk: {disk_path}")
        
        return {
            'smart_data': smart_data,
            'space_analysis': space_analysis,
            'performance_metrics': performance_metrics
        }
