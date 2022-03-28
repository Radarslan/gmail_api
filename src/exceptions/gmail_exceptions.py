import sys
from typing import Any
from typing import Callable

from googleapiclient.errors import HttpError


def greedy_gmail_exception(func: Callable) -> Callable:
    """
    this is just example for wide range of exceptions
    to handle specific one, it must be added into the wrapper
    """

    def wrapper(*args, **kwargs) -> Any:
        try:
            result = func(*args, **kwargs)

        # best practice is to add specific exception here and
        # except UnexpectedBodyError as error:
        #     do something useful here
        #     add message to results, add error to reporting system, etc.
        # "greedy" or "wide" example
        except HttpError as error:
            print(f"gmail api request failed: {error}")
            sys.exit(1)

        return result

    return wrapper
