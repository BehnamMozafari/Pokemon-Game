import unittest

from tester_base import TesterBase


class TestPokemonBase(TesterBase):
    def test_bulbasaur_string(self):
        from pokemon import Bulbasaur
        try:
            c = Bulbasaur()
        except Exception as e:
            self.verificationErrors.append(f"Bulbasaur could not be instantiated: {str(e)}.")
            return
        try:
            c.update_level()
            result = c.get_level()
            if result != 2:
                self.verificationErrors.append(f"update_level did not work")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")

    def test_squirtle_string(self):
        from pokemon import Squirtle
        try:
            c = Squirtle()
        except Exception as e:
            self.verificationErrors.append(f"Squirtle could not be instantiated: {str(e)}.")
            return
        try:
            s = str(c)
            if s != "Squirtle's HP = 8 and level = 1":
                self.verificationErrors.append(f"String method did not return correct string: {s}")
        except Exception as e:
            self.verificationErrors.append(f"String method failed. {e}")
