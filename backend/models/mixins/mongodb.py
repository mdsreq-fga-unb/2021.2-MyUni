from os import environ

from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDBMixin:
    def __init__(self):
        host = environ.get("MONGO_HOST")
        port = environ.get("MONGO_PORT")
        user = environ.get("MONGO_USER")
        password = environ.get("MONGO_PASSWORD")

        if not all([host, port, user, password]):
            raise Exception(".env file missing variables")

        self._client = MongoClient(
            host=host,
            port=int(port),
            username=user,
            password=password
        )

        self._user_db = self._client.user
        self.user_collection: Collection = self._user_db.user

        self._discipline_db = self._client.discipline
        self.discipline_collection: Collection = self._discipline_db.discipline

        self._forum_db = self._client.forum
        self.forum_collection: Collection = self._forum_db.forum

        self._note_db = self._client.note
        self.note_collection: Collection = self._note_db.note

    @property
    def client(self):
        return self._client
