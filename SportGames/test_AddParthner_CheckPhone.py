import unittest
import addParthner

list_phone_cor = ['+71234567890', '+71234567891', '+71234567892', '+71234567893', '+71234567894', '+71234567895', '+71234567896', '+71234567897', '+71234567898', '+71234567899', '81234567890', '81234567891', '81234567892', '81234567893', '81234567894', '81234567895', '81234567896', '81234567897', '81234567898', '81234567899']
list_phone_uncore = ['+11234567890', '+21234567891', '+31234567892', '+41234567893', '+51234567894', '+61234567895', '+81234567896', '+91234567897', '+01234567898', '+7123456789', '812345678900']

class Test_AddParthner_CheckPhone(unittest.TestCase):
    def test_T_Phone(self):
        for check in list_phone_cor:
            self.assertTrue(addParthner.checkPhone(check));

    def test_F_Phone(self):
        for check in list_phone_uncore:
            self.assertFalse(addParthner.checkPhone(check));

if __name__ == '__main__':
    unittest.main()
