import unittest

import addOrder

customers = ["Okolo-Kulak Oscar", "Lee Yan", "Wolfeschlegelsteinhausenbergerdorff Ivan", "Ivanov Roman", "Rimskiy-Korsakov Timofay"]



class Test_test_CheckCustomer(unittest.TestCase):
    def test_CustomersTrue(self):
         for  i in customers:
            self.assertTrue(addOrder.checkCustomer(i), i) 

if __name__ == '__main__':
    unittest.main()
