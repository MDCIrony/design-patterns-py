import bad.serializer_demo as bs
import good.serializer_demo as gs




if __name__ == "__main__":
    mode = "GOOD"
    song = bs.Song('1', 'Water of Love', 'Dire Straits')
    jsonSerializer = gs.JsonSerializer()
    xmlSerializer = gs.XmlSerializer()
    
    if mode == "BAD":
        serializer = bs.SongSerializer() # -> New serializer object
        print(serializer.serialize(song, 'JSON'))
        print(serializer.serialize(song, 'XML'))   
        
        # If we try to serialize the song in YAML format, we get a ValueError:
        try:
            serializer.serialize(song, 'YAML')
        except ValueError as e:
            print(e)
    else:
        print(gs.serialize(song, jsonSerializer))
        # serializer = gs.SongSerializerV1()
        # print(serializer.serialize(song, 'JSON'))
        
    
# The problem with this approach is that we have to 
# modify the SongSerializer class every time we want to add a new format, broken the Open-Closed Principle.