#!/usr/bin/env python3

"""
Server class to paginate a database of popular baby names.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indexes for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset from the CSV file.

        Returns:
            List[List]: The dataset as a list of rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of the
        dataset based on the page number and page size.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The number of
            items per page. Defaults to 10.

        Returns:
            List[List]: The paginated dataset as a list of rows.
        """
        assert isinstance(page, int) and page > 0
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        paginated_data = dataset[start_index:end_index]
        return paginated_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves a specific page of the dataset
        along with pagination information.

        Args:
            page (int, optional): The page number
            Defaults to 1.
            page_size (int, optional): The number of
            items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing the paginated
            dataset and pagination information.
                  Includes keys: 'page_size', 'page',
                  'data', 'next_page', 'prev_page', 'total_pages'.
        """
        assert isinstance(page, int) and page > 0
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        paginated_data = dataset[start_index:end_index]

        total_pages = math.ceil(len(dataset) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(paginated_data),
            "page": page,
            "data": paginated_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
