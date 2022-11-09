import unittest
import code

class Testmycode(unittest.TestCase):

    def encrypt_test(self):
        text1 = code.encrypt(6,"")
        self.assertEqual(text1,"", "")

    def decrypt_test(self):
        text1 = code.decrypt("", 6, "")
        self.assertEqual(text1,"", 6, "")


