import bad.serializer_demo as sd


song = sd.Song('1', 'Water of Love', 'Dire Straits')
serializer = sd.SongSerializer() # -> New serializer object

json_song = serializer.serialize(song, 'JSON')
xml_song = serializer.serialize(song, 'XML')

if __name__ == "__main__":
    print(json_song)
    print(xml_song)
    
    
    # If we try to serialize the song in YAML format, we get a ValueError:
    try:
        serializer.serialize(song, 'YAML')
    except ValueError as e:
        print(e)

    
# The problem with this approach is that we have to 
# modify the SongSerializer class every time we want to add a new format, broken the Open-Closed Principle.