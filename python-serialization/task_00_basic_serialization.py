#!/usr/bin/env python3
"""Serialize dictionaries to JSON files and deserialize them."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a JSON file and return the deserialized data."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
