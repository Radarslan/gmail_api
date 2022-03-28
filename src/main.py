from pprint import pprint
from typing import List

from googleapiclient.discovery import Resource
from googleapiclient.discovery import build

from src.filters.body import Body
from src.filters.filter import Filter
from src.filters.subject import Subject
from src.gmail_client import create_message
from src.gmail_client import get_message
from src.gmail_client import get_messages
from src.gmail_client import send_message
from src.gmail_credentials import get_credentials
from src.settings.constants import RECEIVER
from src.settings.constants import SENDER


def get_query(filters: List[Filter]) -> str:
    if filters is not None:
        query_filters = []
        for filter in filters:
            if filter.name is None:
                query_filters.append(f"'{filter.filter}'")
            else:
                query_filters.append(f"{filter.name}:{filter.filter}")
        return " ".join(query_filters)

    return ""


def search_messages_example(service: Resource):
    """
    search filters, can be created for any of the filters described here
    https://support.google.com/mail/answer/7190
    this one is to search for words in the subject line
    Example: subject:dinner
    """

    # TODO: change this filters to match your email subject line
    #  or body words
    filters = [
        Subject(name="subject", filter="Next steps"),
        Body(filter="hope you are"),
    ]
    query = get_query(filters)

    messages = get_messages(service, query)
    for message in messages:
        pprint(get_message(service=service, message_id=message["id"]))


if __name__ == "__main__":
    credentials = get_credentials()
    service = build("gmail", "v1", credentials=credentials)

    # search emails
    search_messages_example(service)

    # send an email
    message = create_message(
        sender=SENDER, to=RECEIVER, subject="test", message_text="test"
    )
    pprint(send_message(service, message))
