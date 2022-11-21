import unittest
from classes.src.songs import Songs

class TestSongs(unittest.TestCase):
    
    def setUp(self):
        self.num = Songs("Help!")