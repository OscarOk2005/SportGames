import unittest
import addParthner

list_date_cor = ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01', '2023-07-01', '2023-08-01', '2023-09-01', '2023-10-01', '2023-11-01', '2023-12-01']
list_date_uncore = ['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01', '2025-05-01', '2025-06-01', '1800-07-01', '1800-08-01', '1800-09-01', '1800-10-01', '1800-11-01', '1800-12-01']

class Test_test_AddParthner_CheckDate(unittest.TestCase):
    def test_T_Date(self):
        for check in list_date_cor:
            self.assertTrue(addParthner.checkStart_date(check));
        
    def test_F_Date(self):
        for check in list_date_uncore:
            self.assertFalse(addParthner.checkStart_date(check));

if __name__ == '__main__':
    unittest.main()
