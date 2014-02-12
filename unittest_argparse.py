#!/usr/bin/env python
# encoding: utf-8

import unittest
import sys


class TestHelpSpot(unittest.TestCase):

    "A few simple tests for HelpSpot"

    def __init__(self, testname, path, user, pword):
        super(TestHelpSpot, self).__init__(testname)

    def test_version(self):
      print 'do test_version'

    def test_get_with_param(self):
      print 'do test_get_with_param'


def main():
    """Main program."""
    user = sys.argv[1]
    pword = sys.argv[2]
    path = sys.argv[3]

    success = True
    suite = unittest.TestSuite()
    suite.addTest(TestHelpSpot("test_version", path, user, pword))
    suite.addTest(TestHelpSpot("test_get_with_param", path, user, pword))

    success = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    # That's all
    if success:
        return 0
    else:
        return 1
if __name__ == '__main__':
    exitcode = main()
    sys.exit(exitcode)
