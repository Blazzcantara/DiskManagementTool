import unittest
from unittest.mock import patch
from src.analysis.analysis_module import AnalysisModule

class TestAnalysisModule(unittest.TestCase):
    def setUp(self):
        self.analysis_module = AnalysisModule()

    @patch('src.utils.os_compatibility.OSCompatibility.is_valid_disk')
    @patch('src.utils.os_compatibility.OSCompatibility.get_smart_data')
    @patch('src.utils.os_compatibility.OSCompatibility.get_disk_space')
    @patch('src.utils.os_compatibility.OSCompatibility.measure_disk_performance')
    def test_analyze_disk(self, mock_performance, mock_space, mock_smart, mock_valid):
        mock_valid.return_value = True
        mock_smart.return_value = {"Smart": "Data"}
        mock_space.return_value = {"Space": "Analysis"}
        mock_performance.return_value = {"Performance": "Metrics"}

        result = self.analysis_module.analyze_disk("/dev/sda")

        self.assertIn('smart_data', result)
        self.assertIn('space_analysis', result)
        self.assertIn('performance_metrics', result)

if __name__ == '__main__':
    unittest.main()
