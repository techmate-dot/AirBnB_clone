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
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            kwargs.pop("__class__")
            for keys, values in kwargs.items():
                if keys == 'created_at' or keys == 'updated_at':
                    setattr(self, keys, datetime.strptime(values, time_format))
                else:
                    setattr(self, keys, kwargs[keys])
        if not kwargs:
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
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__})"
