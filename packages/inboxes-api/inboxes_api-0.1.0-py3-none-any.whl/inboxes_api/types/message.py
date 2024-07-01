from datetime import datetime

from pydantic import Field, TypeAdapter

from .base import InboxesType


class MessagePreview(InboxesType):
    """
    Model representing a preview of a message.

    Attributes:
        id (str): Unique identifier for the message.
        sender (str): Sender of the message.
        reciever (str): Receiver of the message.
        subject (str): Subject of the message.
        created_at (datetime): Timestamp when the message was created.
    """

    id: str = Field(alias="uid")
    sender: str = Field(alias="from")
    reciever: str = Field(alias="to")
    subject: str
    created_at: datetime


class Message(MessagePreview):
    """
    Model representing a full message, including the preview and the text content.

    Attributes:
        text (str): Text content of the message.
    """

    text: str


class MessageAttachment(InboxesType):
    """
    Model representing an attachment in a message.

    Attributes:
        download_url (str): URL to download the attachment.
    """

    download_url: str


message_preview_list = TypeAdapter(list[MessagePreview])
