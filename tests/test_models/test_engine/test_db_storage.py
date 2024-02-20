#!/usr/bin/python3
"""test db"""
import unittest
from models.engine import db_storage
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "test not relevant")
class test_dbStorage(unittest.TestCase):
    pass
