from database  import get_name
import os

name = get_name()


def is_ubuntu():
    if 'Ubuntu' in os.name:
        return True 
    else:
        return False


print(is_ubuntu())


music_path = "/media/indrajeet/Inderjit/music/"

