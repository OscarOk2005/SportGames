import unittest
import addArticle

list_date_incor = ["", "asasdasdsad", 1231, "20/02/2022", '30.02.2016', '10.10.2025', 
                   '2021.10.10', '12345678', '10.10.10', '29.02.2021', '12.13.2020', '00.10.2021']

class Test_text_F_date(unittest.TestCase):
    def test_incorrect_date(self):
        for i in list_date_incor:
            self.assertFalse(addArticle.isValidDate(i))

if __name__ == '__main__':
    unittest.main()
