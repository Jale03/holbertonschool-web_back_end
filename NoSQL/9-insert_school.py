#!/usr/bin/env python3
"""
Inserts a new document in a collection using kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document into mongo_collection
    Returns the new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
