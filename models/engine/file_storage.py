#!/usr/bin/python3
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
        FileStorage.__objects[f'BaseModel.{obj.id}'] = obj

    def save(self):
        """ Save the __objects to a file.json
        """
        temp = {}
        temp.update(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as json_file:
            for key, values in temp.items():
                if not isinstance(values, dict):
                    temp[key] = values.to_dict()
            json.dump(temp, json_file, indent=4)

    def reload(self):
        """ Reads from file.json and saves it to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r',
                      encoding='UTF-8') as json_file:
                temp = json.load(json_file)
                for key in temp:
                    FileStorage.__objects = key
        except FileNotFoundError:
            pass
