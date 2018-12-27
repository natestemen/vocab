"""Tests for our main vcb CLI module."""


from subprocess import PIPE
from subprocess import Popen as popen
from unittest import TestCase

from vcb import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(["vcb", "-h"], stdout=PIPE).communicate()[0]
        self.assertTrue("Usage:" in output)

        output = popen(["vcb", "--help"], stdout=PIPE).communicate()[0]
        self.assertTrue("Usage:" in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(["vcb", "--version"], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
