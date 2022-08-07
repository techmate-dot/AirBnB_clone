#!/usr/bin/python3
"""A class BaseModel that defines all
    common attributes/methods for other classes
   """
import uuid
from datetime import datetime


class BaseModel:
    """A template that defines all common
        attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs) -> None:
        """Assigns all instance attributes
        """
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at
        if kwargs:
            kwargs.pop("__class__")
            for keys in kwargs:
                self.keys = kwargs[keys]

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict representation the class"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
    def __str__(self) -> str:
        """Returns a string representation of the class"""

        return f"[BaseModel] ({self.id}) {self.__dict__})"
