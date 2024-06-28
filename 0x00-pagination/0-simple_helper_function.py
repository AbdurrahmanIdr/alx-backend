#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
     Returns the start and end index range for a given page. This is useful for generating an index range based on the page number and page size
     
     Args:
     	 page: The page to get the index range for
     	 page_size: The size of the page in bytes
     
     Returns: 
     	 A tuple of two integers ( start end ) where start is the start of the page and end is the end of the
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
