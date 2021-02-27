from attr_and_methods.topics.category import Category
from attr_and_methods.topics.document import Document
from attr_and_methods.topics.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        temp = [c for c in self.categories if c.id == category_id]
        try:
            temp[0].edit(new_name)
        except IndexError:
            pass

    def edit_topic(self, topic_id, new_topic: str, new_storage_folder: str):
        temp = [c for c in self.topics if c.id == topic_id]
        try:
            temp[0].edit(new_topic, new_storage_folder)
        except IndexError:
            pass

    def edit_document(self, document_id: int, new_file_name: str):
        temp = [c for c in self.documents if c.id == document_id]
        try:
            temp[0].edit(new_file_name)
        except IndexError:
            pass

    def delete_category(self, category_id):
        temp = [c for c in self.categories if c.id == category_id]
        try:
            self.categories.remove(temp[0])
        except IndexError:
            pass

    def delete_topic(self, topic_id):
        temp = [c for c in self.topics if c.id == topic_id]
        try:
            self.topics.remove(temp[0])
        except IndexError:
            pass

    def delete_document(self, document_id):
        temp = [c for c in self.documents if c.id == document_id]
        try:
            self.documents.remove(temp[0])
        except IndexError:
            pass

    def get_document(self, document_id):
        temp = [c for c in self.documents if c.id == document_id]
        try:
            return temp[0].__repr__()
        except IndexError:
            pass

    def __repr__(self):
        result = ''
        for d in self.documents:
            result += d.__repr__() + '\n'
        return result
