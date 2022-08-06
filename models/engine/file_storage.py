""" Store all object representation
    """
import json


class FileStorage:
    """ Convert the dictionary representation
        to a JSON string
    """
    __file_path = "file.json"
    __objects = {}  # will store all object by <class name>.id

    def all(self):
        """ returns the dictionary __objects

        Returns:
            (obj): dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

        Args:
            obj (obj): New object that will be save in __objects
        """
    # Todo: change the key to "<class name>.id" e.g "Basemode.121212"
        FileStorage.__objects[obj["id"]] = obj

    def save(self):
        """ Save the __objects to a file.json
        """
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as json_file:
            if len(FileStorage.__objects) != 0:
                json.dump(FileStorage.__objects, json_file, indent=4)

    def reload(self):
        """ Reads from file.json and saves it to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r',
                      encoding='UTF-8') as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
