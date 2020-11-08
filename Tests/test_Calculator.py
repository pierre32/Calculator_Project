mport unittest
from calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/src/data/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_subtraction(self):
        test_data = CsvReader('/src/src/data/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply(self):
        test_data = CsvReader('/src/src/data/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide(self):
        test_data = CsvReader('/src/src/data/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        test_data = CsvReader('/src/src/data/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('/src/src/data/square_root.csv').data
        for row in test_data:
            self.assertTrue(
                abs(self.calculator.square_root(row['Value 1']) - float(row['Result'])) < 0.0000001
            )
            self.assertTrue(
                abs(self.calculator.result - float(row['Result'])) < 0.0000001
            )


if __name__ == '__main__':
    unittest.main()
