#!/usr/bin/env python3
"""
module for task 0: Simple helper function
"""

import json


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range that takes two integer
    Args:
        int(page)
        int(page_size)
    Returns:
        tuple(start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    dataset = (start_index, end_index)
    return dataset
