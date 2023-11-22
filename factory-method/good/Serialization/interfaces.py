from abc import ABC, abstractmethod

class Serializer(ABC):
    def __init__(self):
        self._current_object = None
    
    @abstractmethod
    def start_object(self, object_name: str, object_id: str) -> None:
        raise NotImplementedError('start_object() not implemented')

    @abstractmethod
    def add_property(self, name: str, value: str) -> None:
        raise NotImplementedError('add_property() not implemented')

    @abstractmethod
    def to_str(self) -> str:
        raise NotImplementedError('to_str() not implemented')



class Serializable(ABC):
    @abstractmethod
    def serialize(self, serializer: Serializer) -> None:
        raise NotImplementedError('serialize() not implemented')


class Song(Serializable):
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer: Serializer) -> None:
        serializer.start_object('song', self.song_id)
        serializer.add_property('title', self.title)
        serializer.add_property('artist', self.artist)