import unittest
import addOrder

notCustomers = ["Okolo-Kulak-Okolo Oscar", "Ivanov1 Ivan", "Wolfeschlegelsteinhausenbergerdorffa Roman", "Le Yan", "Lee Yn", "Okolo:Kulak Oscar", 
                "O-Kulak Oscar", "Okolo-K Oscar", "Okolo-Kulak Oscar1", "Okolo-Kulak Os-car", "12345 54321", "PushkinAlexandr"]

class Test_test_CheckCustomerFalse(unittest.TestCase):
    def test_CustomersFalse(self):
         for  i in notCustomers:
            self.assertFalse(addOrder.checkCustomer(i), i) 
        

if __name__ == '__main__':
    unittest.main()
