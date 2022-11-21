import unittest
from src.guests import Guest
from src.rooms import Room
from src.songs import Song
from src.caraoke import Caraoke

class TestCaraoke(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Anne", "Jeff")
        self.rooms = Room(2, 4, 6, 8)
        self.songs = Song ("Help", "Hey ya")

        