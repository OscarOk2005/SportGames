import unittest
import addArticle

list_date_cor = ['04.06.2024', '01.01.2000', '31.01.2000', '31.12.2023', '29.02.2020', '30.06.2020',
                 '10.10.2010', '12.12.2012']

class Test_test_T_date(unittest.TestCase):
    def test_correct_date(self):
        for i in list_date_cor:
            self.assertTrue(addArticle.isValidDate(i))

if __name__ == '__main__':
    unittest.main()
