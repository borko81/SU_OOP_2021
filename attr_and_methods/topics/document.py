from attr_and_methods.topics.category import Category
from attr_and_methods.topics.topic import Topic


class Document:

    def __init__(self, id, category_id, topic_id, file_name):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instance(cls, id, category: Category, topic: Topic, file_name: str):
        return cls(id, category, topic, file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        try:
            self.tags.remove(tag_content)
        except ValueError:
            pass

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        joined_tags = ', '.join(self.tags)
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {joined_tags}"
