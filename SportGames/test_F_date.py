import unittest
import addArticle

list_date_incor = ["", "asasdasdsad", 1231, "20/02/2002" ]

class Test_text_F_date(unittest.TestCase):
    def test_incorrect_date(self):
        for i in list_date_incor:
            self.assertFalse(addArticle.isValidDate(i))

if __name__ == '__main__':
    unittest.main()
