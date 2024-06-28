#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
         Initializes a new Server instance.
         Subclasses should override this method to perform initialization tasks 
         such as setting up the dataset
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
         Read and cache the dataset. 
         This is used for testing and should not be used in production as it relies 
         on the data_file being in the same directory as the test_data_dir.
         
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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Returns a dictionary of the dataset indexed by sorting position starting at 0.
         This is useful for debugging the performance of a dataset that is used 
         to determine the number of iterations that have been performed on the dataset.
         
        Returns: 
         A dictionary of the dataset indexed by sorting position starting at 0.
         The keys are the integers in the range 0 to
        """
        # Set the indexed dataset to be used for indexing.
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
         Retrieves information about a hyperparameter and its page. 
         This is useful for finding the index of an individual hyperparameter in a data set
         
         Args:
         	 index: ( Optional def = None ) 
             The index of the hyperparameter to retrieve
         	 page_size: ( Optional def = 10 ) The size of the page
         
         Returns: 
         	 A dictionary with the following keys : index next_index
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        # Add data to page_data.
        for i, item in data.items():
            # Append item to page_data.
            if i >= start and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            # If data_count is equal to page_size set next_index to the next page.
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
