from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self,3, 3) == 9

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 10, 6) == 4

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 9, 1) == 10

    def test_multiply_calculator_failed(self):
        assert self.calc.multiply(self, 3, 3) == 3


