import unittest
from classes.src.rooms import Room
from classes.src.guests import Guest
from classes.src.songs import Songs

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room(2)
        self.guest = Guest("Anne")
        self.song = Songs ("Help")
       
        
    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        expected_output = 1
        self.assertEqual(expected_output, len(self.room.guest_list))

    def test_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest)
        self.assertEqual(1, len(self.room.guest_list))
        self.room.remove_guest_to_room(self.guest)
        expected_output = 0
        self.assertEqual(expected_output, len(self.room.guest_list))
    
    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song)
        expected_output = 1
        self.assertEqual (expected_output, len(self.room.song_list))
  