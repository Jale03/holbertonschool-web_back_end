#!/usr/bin/env python3
"""
Lists all documents in a collection
"""

def list_all(mongo_collection):
    """
    Returns all documents in a collection
    or empty list if none exist
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
