import unittest
from classes.src.guests import Guest
from classes.src.rooms import Room
from classes.src.songs import Songs

class TestGuest(unittest.TestCase):
    
    # def setUp(self):
        
    #     self.guest = Guest("Anne")
    #     self.guest_2 = Guest("Jeff")
    #     self.room = Room(12, 25, 30)
    #     self.song = Song("Brown Eyed Girl", "Give me shelter")
        
    def setUp(self):
        self.guest = Guest("Anne", "Jeff")

    # def test_remove_guest_from_room(self):
    #     input = ["Anne", "Jeff"]
    #     expected_output = "Anne"
    #     result = remove_guest_from_room(input)
    #     self.assertEqual(expected_output, result)

