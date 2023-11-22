# In serializers.py
from good.Serialization.interfaces import Serializer, Serializable
from good.Serialization.serializers import factory


# Generic serializer for any object type
# Any object that implements serialize() can be serialized


class Song(Serializable):
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer: Serializer) -> None:
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)

class ObjectSerializer:
    def serialize(self, serializable: Serializable, format: str):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()
