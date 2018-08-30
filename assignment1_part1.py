#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Working with classes and functions"""


class ListDivideException(Exception):
    """Custom exception class"""
    pass
  

def listDivide(numbers, divide=2):

    """Returns number of elements in the numbers list,  

    divisible by divide.

    
    Args:

        numbers (list): A list of numbers.

        divide (int):   It has a default value of 2.
       

    Return:  

        int: Number of elements in the numbers list, divisible by divide.
       

    Example:
       
        In [91]:listDivide([1,2,3,4,5,6])

        Out[91]: 3
       
        """

    count_div_by_divide = 0

    for x in numbers:

        if (x%divide)==0:

            count_div_by_divide += 1

    return count_div_by_divide


def testListDivide():

    """Performs the following tests on listDivide"""

    try:

        if listDivide([1,2,3,4,5])<>2:

            raise ListDivideException('No idenfied number divided by 2')

        elif listDivide([2,4,6,8,10])<>5:

            raise ListDivideException('No idenfied number divided by 2')

        elif listDivide([30, 54, 63,98, 100],10)<>2:

            raise ListDivideException('No idenfied number divided by 10')

        elif listDivide([]) <> 0:

            raise ListDivideException('Empty list')

        elif listDivide([1,2,3,4,5], 1)<>5:

            raise ListDivideException('No idenfied number divided by 2')

    except ListDivideException:

     raise
