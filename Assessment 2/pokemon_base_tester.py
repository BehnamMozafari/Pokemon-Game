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
            result_level = c.get_level()
            if result_level != 2:
                self.verificationErrors.append(f"update_level did not work")
                return
        try:
            c.decrease_hp()
            result_decrease = c.get_hp()
            if result_decrease != "hp should not be negative":
                self.verificationErrors.append(f"update_level did not work")
                return






