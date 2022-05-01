import unittest

from tester_base import TesterBase, captured_output


class TestPokeTeam(TesterBase):

    def test_limit(self):
        from poke_team import PokeTeam
        # testing __init__ method, choose_team method, assign_team method
        try:
            team = PokeTeam("Behnam")
        except Exception as e:
            self.verificationErrors.append(f"Behnam's team could not be instantiated: {str(e)}.")
            return
        try:
            with captured_output("9 1 1\n0 0 1") as (inp, out, err):
                # 9 1 1 should fail, since it is too many pokemon.
                # So 0 0 1 should be the correct team.
                team.choose_team(0, None)
        except Exception as e:
            self.verificationErrors.append(f"Ash's team could not be chosen: {str(e)}.")
            return
        output = out.getvalue().strip()

        # Check the prompt is being printed.
        try:
            assert "is the number of Charmanders" in output
            assert "is the number of Bulbasaurs" in output
            assert "is the number of Squirtles" in output
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not print prompt correctly.")
        try:
            assert str(
                team) == "Charmander's HP = 7 and level = 1, Bulbasaur's HP = 9 and level = 1, Squirtle's HP = 8 and level = 1"
        except AssertionError:
            self.verificationErrors.append(f"PokeTeam does not handle limit correctly. {str(team)}")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokeTeam)
    unittest.TextTestRunner(verbosity=0).run(suite)