#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return deletion-resilient pagination"""

        assert index is not None
        assert isinstance(index, int)
        assert index >= 0
        assert isinstance(page_size, int)
        assert page_size > 0

        data = self.indexed_dataset()
        data_len = len(data)

        if index >= data_len:
            raise AssertionError

        current_index = index
        result = []
        count = 0

        # data topla (silinmiş index-ləri keçərək)
        while count < page_size and current_index < data_len:
            if current_index in data:
                result.append(data[current_index])
                count += 1
            current_index += 1

        # next valid index tap
        next_index = current_index if current_index < data_len else None

        return {
            "index": index,
            "data": result,
            "page_size": page_size,
            "next_index": next_index
        }
