from funciones import calcula_media
import unittest

class Test_misfunciones(unittest.TestCase):
    
    def setUp(self):
        print("Entrando en setup")
    
    def teardown(self):
        print("Entrando en teardown")
        
    def test_1(self):
        result = calcula_media([5,5,5])
        self.assertEqual(result, 5)
        
    def test_2(self):
        result = calcula_media([5,5,5])
        self.assertEqual(result, 15)

    def test_3(self):
        self.assertIn(1, [1, 2])
        
if __name__ == '__main__':
    unittest.main()