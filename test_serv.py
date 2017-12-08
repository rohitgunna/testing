import unittest
import parser1

class Test_main(unittest.TestCase):

    def test_scientific(self):
        #assert parser1.parse(".3e-8") == "0.3*10**-8"
        assert parser1.parse("44.4E-2") == "444*10**-3"
        assert parser1.parse("12.e55") == None
        assert parser1.parse("4.35e+1") == "435*10**-1"
        assert parser1.parse("1.7E-7") == "17*10**-8"
                
if __name__ == '__main__':
    unittest.main(verbosity=2,exit=False)
