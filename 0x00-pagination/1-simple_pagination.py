#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the start and end index range for a given page.

    Args:
        page (int): The page to get the index range for.
        page_size (int): The size of the page in items.

    Returns:
        Tuple[int, int]: A tuple of two integers (start, end) where start is
        the start of the page and end is the end of the page.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads and caches the dataset.

        Returns:
            List[List]: List of lists where each list represents a row in the
            dataset. The first list is the header and the rest are the data.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data.

        Args:
            page (int): Page number to retrieve. Default is 1.
            page_size (int): Number of items per page. Default is 10.

        Returns:
            List[List]: List of lists of data. Each list is a list of items
            in the page.
        """
        assert isinstance(page, int) and isinstance(
            page_size, int
        ), "Both page and page_size must be integers."
        assert (
            page > 0 and page_size > 0
        ), "Both page and page_size must be greater than 0."
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
