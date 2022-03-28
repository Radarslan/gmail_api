import base64
from email.mime.text import MIMEText
from typing import Dict
from typing import List

from googleapiclient.discovery import Resource

from src.exceptions.gmail_exceptions import greedy_gmail_exception
from src.settings.custom_types import Message
from src.settings.custom_types import Messages


@greedy_gmail_exception
def get_messages(service: Resource, query: str) -> List[Messages]:
    results = (
        service.users()
        .messages()
        .list(userId="me", maxResults=10, q=query)
        .execute()
    )

    if "messages" in results and len(results["messages"]) > 0:
        return results["messages"]

    return []


@greedy_gmail_exception
def get_message(service: Resource, message_id: str) -> Message:
    results = (
        service.users().messages().get(userId="me", id=message_id).execute()
    )

    return results


def create_message(
    sender: str, to: str, subject: str, message_text: str
) -> Dict[str, str]:
    """
    Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {
        "raw": base64.urlsafe_b64encode(message.as_string().encode()).decode()
    }


@greedy_gmail_exception
def send_message(service: Resource, message: str) -> Message:
    """Send an email message.

    Args:
    service: Authorized Gmail API service instance.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    return service.users().messages().send(userId="me", body=message).execute()
