import json
import xml.etree.ElementTree as et
from abc import ABC, abstractmethod

from bad.serializer_demo import Song

# Serializer only for Songs objects

class SerializerInterface(ABC):
    @abstractmethod
    def _serialize(self, song: Song) -> str:
        raise NotImplementedError('serialize() not implemented')


class JsonSerializer(SerializerInterface):
    def _serialize(self, song: Song) -> str:
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

class XmlSerializer(SerializerInterface):
    def _serialize(self, song: Song) -> str:
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


# Creator function
def serialize(song: Song , serializer: SerializerInterface) -> str:
    return serializer._serialize(song)


class SongSerializerV1:
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        print(serializer)
        return serializer(song)

    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')
