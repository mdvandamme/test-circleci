#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import unittest
from src.math import Math

class MathTest(unittest.TestCase):
    
    def test_addition_1(self):
        # Make test fail
        self.assertEqual(Math.addition(3, 4), 8)
        
    def test_addition_2(self):
        # Make test fail
        self.assertEqual(Math.addition(3, 4), 7)
        
    def test_soustraction_1(self):
        # Make test fail
        self.assertEqual(Math.soustraction(3, 4), -1)
        
    def test_soustraction_2(self):
        # Make test fail
        self.assertEqual(Math.soustraction(3, -4), 7)
    