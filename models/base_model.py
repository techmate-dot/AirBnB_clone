#!/usr/bin/python3
"""A class BaseModel that defines all
    common attributes/methods for other classes
   """
import uuid
import datetime


class BaseModel:
    """A template that defines all common
        attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs) -> None:
        """Assigns all instance attributes
        """
        self.created_at = datetime.datetime.now()
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
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dict representation the class"""
        bm_dict = dict(self.__dict__)
        bm_dict['__class__'] = type(self).__name__
        bm_dict['created_at'] = bm_dict['created_at'].isoformat()
        bm_dict['updated_at'] = bm_dict['updated_at'].isoformat()
        return bm_dict

    def __str__(self) -> str:
        """Returns a string representation of the class"""

        return f"[BaseModel] ({self.id}) {self.__dict__})"
