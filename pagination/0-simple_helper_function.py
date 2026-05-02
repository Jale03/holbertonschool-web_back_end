#!/usr/bin/env python3
"""
Pagination helper module.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start and end index for pagination.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
