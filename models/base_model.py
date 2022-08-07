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
        DateTime = datetime.datetime.now().isoformat()
        self.created_at = DateTime
        self.id = str(uuid.uuid4())
        self.updated_at = DateTime
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

        new_dict = {'__class__': 'BaseModel'}
        self.created_at = str(self.created_at)
        self.updated_at = str(self.updated_at)
        return {**new_dict, **self.__dict__}

    def __str__(self) -> str:
        """Returns a string representation of the class"""

        return f"[BaseModel] ({self.id}) {self.__dict__})"
