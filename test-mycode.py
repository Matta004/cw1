import unittest
import decrypt
class test_my_code(unittest.TestCase):
    def test_encrypt(self):
        test1 = decrypt.encrypt("COVENTRY")
        self.assertEqual("LC UY MU AK",test1,"incorrect")

if __name__ == "__main__":
    unittest.main()