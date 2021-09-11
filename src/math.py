#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""


class Math():
    
    def addition(value1, value2):
    
        if not isinstance(value1, int) and not isinstance(value2, int):
            return 'Invalid input'
        
        else:
            return value1 + value2
        
    
    def soustraction (value1, value2):
        
        if not isinstance(value1, int) and not isinstance(value2, int):
            return 'Invalid input'
        
        else:
            return value1 - value2