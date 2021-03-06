#!/usr/bin/python3
"""
save file JSON the dictionaries passed
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Prints a dictionary with all created instances"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the dictionary __objects the new object
        """
        key = type(obj).__name__+"." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary __objects into a JSON file
        """
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()  # convert each object into a dict
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        """
        Updates the dictionary __objects from a json file
        """
        class_obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_obj[key] = eval(value["__class__"] + "(**value)")
        except Exception:
            pass
