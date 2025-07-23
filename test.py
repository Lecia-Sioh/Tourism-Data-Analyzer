import unittest
from pge import VisitorsAnalyticsUtils

class TestVisitorsAnalyticsUtils(unittest.TestCase):

    def setUp(self):
        # Define the test CSV file path
        self.test_file = "Int_Monthly_Visitor.csv"

    def test_load_data_file_structure(self):
        utils = VisitorsAnalyticsUtils(self.test_file)
        utils.loadDataFile()

        # Count actual rows and columns
        actual_rows = len(utils.data)
        actual_columns = len(utils.data.columns)

        # Print the detected values
        print(f"\nDetected Rows: {actual_rows}")
        print(f"Detected Columns: {actual_columns}")

        # Assert expected structure
        self.assertEqual(actual_rows, 479)
        self.assertEqual(actual_columns, 36)

if __name__ == '__main__':
    unittest.main()
