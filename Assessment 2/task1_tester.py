import unittest

from tester_base import TesterBase

class TestTask1(TesterBase):

    def test_charmander_string(self):
        from pokemon import Charmander
        try:
            c = Charmander()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Charmander's HP = 7 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    ### ADD TESTS HERE
    def test_poke_type(self):
        from pokemon import Charmander
        try:
            c = Charmander()
            type123 = c.get_poke_type()
        except Exception as e:
            self.verificationErrors.append(f"Charmander could not be instantiated: {str(e)}.")
            return
        try:
            if type123 != "Fire":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask1)
    unittest.TextTestRunner(verbosity=0).run(suite)