# -*- coding: utf-8 -*-
'''
Create Date: 2024/04/01
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

__created_date__ = "2024/04/01"
__author__ = "@1chooo (Hugo ChunHo Lin)"
__version__ = "v0.0.1"

import sys
from os.path import join
from os.path import dirname
from os.path import abspath

# Back to the project root directory path
project_root = join(
    dirname(abspath(__file__)),
    '..',       # You may need to change the path to follow the 'test/' directory
)
sys.path.append(project_root)

import unittest
from app.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), None)

if __name__ == '__main__':
    unittest.main()
