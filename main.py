import unittest
from unittest.suite import TestSuite
import register, login, addToCart, checkout

if __name__ == "__main__":

    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(register))
    suite.addTest(tests.loadTestsFromModule(login))
    suite.addTest(tests.loadTestsFromModule(addToCart))
    suite.addTest(tests.loadTestsFromModule(checkout))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)