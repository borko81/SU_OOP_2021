class Hotel:
    def __init__(self, name):
        self.name: str = name
        self.rooms = []
        self.guests: int = 0
 
    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)
 
    def add_room(self, room):
        self.rooms.append(room)
 
    def take_room(self, room_number, people):
        room = self._find_room_by_number(room_number)
        res = room.take_room(people) is None
        if res:  # success
            self.guests += people
        else:
            return res
 
    def free_room(self, room_number):
        room = self._find_room_by_number(room_number)
        room_guests = room.guests
        res = room.free_room()
        if res is None:
            self.guests -= room_guests
        else:
            return res
 
    def _find_room_by_number(self, number):
        return [room for room in self.rooms if room.number == number][0]

 
    def print_status(self):
        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f"Free rooms: {', '.join(map(str, free_rooms))}")
        print(f"Taken rooms: {', '.join(map(str, taken_rooms))}")