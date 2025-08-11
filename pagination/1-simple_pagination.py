#!/usr/bin/env python3
"""
Function about pagination
return a tuple size two: a page starting and how much elements by page
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of page asked and size of page
    """
    start: int = page * page_size - page_size
    still: int = start + page_size
    return (start, still)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        datas = self.dataset()
        start_stop: Tuple[int, int] = index_range(page, page_size)
        start: int = start_stop[0]
        if start > len(datas):
            return []
        end: int = start_stop[1]
        data_page = datas[start:end]
        return data_page
