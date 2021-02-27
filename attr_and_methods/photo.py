class PhotoAlbum:

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photo_count(cls, photo_count: int):
        return cls(photo_count // 0.25)

    def add_photo(self, label: str):
        for position in range(len(self.photos)):
            if len(self.photos[position]) < 4:
                self.photos[position].append(label)
                return f"{label} photo added successfully on page {position + 1} slot {len(self.photos[position])}"
        return "No more free spots"

    def display(self):
        insert_line = '-' * 11 + '\n'
        result = insert_line
        for page in range(len(self.photos)):
            result += '[] ' * len(self.photos[page]) + '\n'
            result += insert_line
        return result


if __name__ == '__main__':
    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())
