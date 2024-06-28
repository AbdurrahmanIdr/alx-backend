#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index range for a given page. 
     
    Args:
     	page: The page to get the index range for
     	page_size: The size of the page in bytes
     
     Returns: 
     	A tuple of two integers ( start end ) where start is the start of the page 
        and end is the end of the
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
         Initializes a new Server instance. 
         @ In None @ Out __init__ None @ Out __dataset None @ Out
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
         Read and cache the dataset. 
         This is used for testing and should not be used in production as
         it relies on the data_file being in the same directory 
         as the test_data_dir.
         
         Returns: 
         	 List of lists each list representing a row in the dataset. 
             The first list is the header and the rest are the data
        """
        # Load the dataset from the data file.
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         Retrieves a page of data. This is useful for pagination. 
         The page can be specified by page number and page size.
         
         Args:
         	 page: Page number to retrieve. Default is 1.
         	 page_size: Number of items per page. Default is 10.
         
         Returns: 
         	 List of lists of data. 
             Each list is a list of item in the page ( as List [ List ]
        """
        assert isinstance(page) == int and isinstance(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        # Returns a list of data.
        if start > len(data):
            return []
        return data[start:end]
