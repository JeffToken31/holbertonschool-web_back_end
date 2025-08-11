#!/usr/bin/env python3
"""
Function about pagination
return a tuple size two: a page starting and how much elements by page
"""
from typing import Tuple, List, Dict
import csv
from math import ceil


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
        """
        Get desired page of dataset
        """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, object]:
        """
        Function take a set of datas and return all parameters in dict
        """
        datas = self.dataset()
        start_stop: Tuple[int, int] = index_range(page, page_size)
        start: int = start_stop[0]
        end: int = start_stop[1]
        if start > len(datas):
            data_page = []
        else:
            data_page = datas[start:end]
        result = {}
        result['page_size'] = page_size
        result['page'] = page
        result['data'] = data_page
        if page + 1 < len(datas):
            result['next_page'] = page + 1
        else:
            result['next_page'] = None
        if page - 1 != 0:
            result['prev_page'] = page - 1
        else:
            result['prev_page'] = None
        result['total_pages'] = ceil(len(datas) / page_size)
        return result
