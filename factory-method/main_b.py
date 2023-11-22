from good.Serialization.serializers import factory
from good.object_serializer import Song, ObjectSerializer

if __name__ == "__main__":
    song = Song('1', 'Water of Love', 'Dire Straits')
    serializer = ObjectSerializer()
    print(serializer.serialize(song, 'JSON'))
    print(serializer.serialize(song, 'XML'))
    # If we try to serialize the song in YAML format, we get a ValueError:
    try:
        serializer.serialize(song, 'YAML')
    except ValueError as e:
        print(e)

