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
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
