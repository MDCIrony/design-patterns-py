import json
import xml.etree.ElementTree as et

from good.Serialization.interfaces import Serializer, Serializable

class JsonSerializer(Serializer):
    def start_object(self, object_name: str, object_id: str) -> None:
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name: str, value: str) -> None:
        self._current_object[name] = value

    def to_str(self) -> str:
        return json.dumps(self._current_object)


class XmlSerializer(Serializer):
    def start_object(self, object_name: str, object_id: str) -> None:
        self._current_object = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name: str, value: str) -> None:
        prop = et.SubElement(self._current_object, name)
        prop.text = value

    def to_str(self) -> str:
        return et.tostring(self._current_object, encoding='unicode')

class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)
