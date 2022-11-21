class Room:

    def __init__(self, num):
        self.num = num
        self.guest_list = []
        self.song_list = []


    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)

    def remove_guest_to_room(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_room(self, song):
        self.song_list.append(song)