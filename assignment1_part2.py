#!/usr/bin*//env python
# -*- coding: utf-8 -*-
"""A simple class"""


class Book(object):
    def __init__(self, author, tittle):
        """Sets author and tittle to the object variables
        
        Attr:
            author (str).  Author of the book
            tittle (str).  Tittle of the book"""
        self.author = author
        self.tittle = tittle
    
    def tittle_tittle(self):
        """Refers to the object itself"""
        print self.tittle
        
    def author_author(self):
        """Referes to the object itself"""
        print self.author
        
    def display(self):
        """prints out a string representing the book
        
        Return:
            Str.  A string with name of the book and author.
            
        Examples:
            Of Mice and Men written by John Steinbeck
            To Kill a Mockingbird written by Harper Lee
        """
        print self.tittle + ' written by ' + self.author
        

book1 = Book('John Steinbeck','Of Mice and Men')
book1.display()
book2 = Book('Harper Lee','To Kill a Mockingbird' )
book2.display()
