from unittest import TestCase
import random
import my_application


class MyApplication(TestCase):

    def test_remove_duplicates(self):

        expected = []
        given = []

        for _ in range(10):
            v = random.randint(1, 5)
            given.append(v)

            if v not in expected:
                expected.append(v)

        result = my_application.remove_duplicates(given)
        self.assertIsNotNone(result, "the value your function returned was none, did you forget a return statement?")
        self.assertListEqual(expected, result, f"The value your function {result} return did not match expected value")
        self.assertIs(given, result, "you are not return the same list your function was given")

