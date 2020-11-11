import unittest
import leap_year

class Testleap_year(unittest.TestCase):
    def test_input_year(self):
             self.assertEqual(leap_year.input_year(2020),  None)
             self.assertEqual(leap_year.input_year(2021),  None)
             self.assertEqual(leap_year.input_year(2024),  None)
             self.assertEqual(leap_year.input_year(2025),  None)
             
if __name__=='__main__':
    unittest.main()	           
   	            