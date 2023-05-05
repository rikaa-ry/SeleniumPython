import unittest
from unittest.suite import TestSuite
import register, login, addToCart

if __name__ == "__main__":

    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(register))
    suite.addTest(tests.loadTestsFromModule(login))
    # suite.addTest(tests.loadTestsFromModule(addToCart))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)