#!/usr/bin/python3
"""A class BaseModel that defines all
    common attributes/methods for other classes
   """
import uuid
from datetime import datetime


time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A template that defines all common
        attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs) -> None:
        """Assigns all instance attributes
        """
        self.id = str(uuid.uuid4())
        if kwargs:
            kwargs.pop("__class__")
            for keys in kwargs:
                if keys is 'created_at' or keys is 'updated_at':
                    self.keys = datetime.strptime(kwargs[keys], time_format)
                    self.keys = kwargs[keys]
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict representation the class"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.updated_at.strftime(time_format)
        new_dict['updated_at'] = self.created_at.strftime(time_format)
        return new_dict

    def __str__(self) -> str:
        """Returns a string representation of the class"""
        return f"[BaseModel] ({self.id}) {self.__dict__})"
