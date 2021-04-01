
import unittest
import fizzbuzz


class FizzBuzz(unittest.TestCase):

    def test_that_multiple_of_three_is_fizz(self):
        # Arrange
        i = 33
        expectedResult = "fizz"
        # Act
        receive = fizzbuzz.fizzbuzz(i)
        # Assert
        self.assertEqual(expectedResult, receive)

    def test_that_multiple_of_five_is_buzz(self):
        # Arrange
        i = 10
        expectedResult = "buzz"
        # Act
        receive = fizzbuzz.fizzbuzz(i)
        # Assert
        self.assertEqual(expectedResult, receive)

    def test_that_multiple_of_five_and_three_is_fizzbuzz(self):
        # Arrange
        i = 15
        expectedResult = "fizzbuzz"
        # Act
        receive = fizzbuzz.fizzbuzz(i)
        # Assert
        self.assertEqual(expectedResult, receive)


if __name__ == '__main__':
    unittest.main()