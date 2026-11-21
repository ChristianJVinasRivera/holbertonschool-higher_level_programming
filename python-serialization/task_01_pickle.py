#!/usr/bin/env python3
"""Serialize and deserialize custom objects using pickle."""

import pickle


class CustomObject:
    """Represent an object that can be saved and restored."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Save the object to a binary file, returning None on failure."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Restore an object from a file, returning None on failure."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
