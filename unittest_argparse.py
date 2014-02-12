#!/usr/bin/env python
# encoding: utf-8

import unittest
import sys
import argparse


class TestHelpSpot(unittest.TestCase):

    "A few simple tests for HelpSpot"

    def __init__(self, testname, user, pword):
        super(TestHelpSpot, self).__init__(testname)
        print user
        print pword

    def test_version(self):
        print 'do test_version'

    def test_get_with_param(self):
        print 'do test_get_with_param'


def main():
    """Main program."""
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x ** args.y

    if args.quiet:
        print answer
    elif args.verbose:
        print "{} to the power {} equals {}".format(args.x, args.y, answer)
    else:
        print "{}^{} == {}".format(args.x, args.y, answer)
    user = args.x
    pword = args.y

    success = True
    suite = unittest.TestSuite()
    suite.addTest(TestHelpSpot("test_version", user, pword))
    suite.addTest(TestHelpSpot("test_get_with_param", user, pword))

    success = unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful()
    # That's all
    if success:
        return 0
    else:
        return 1
if __name__ == '__main__':
    exitcode = main()
    sys.exit(exitcode)
