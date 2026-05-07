#!/usr/bin/env python3
"""
Returns list of schools that have a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools that contain the topic in their topics list
    """
    return list(mongo_collection.find({"topics": topic}))
