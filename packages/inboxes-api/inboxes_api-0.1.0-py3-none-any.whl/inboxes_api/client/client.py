from typing import cast

from ..types.message import (
    Message,
    MessageAttachment,
    MessagePreview,
    message_preview_list,
)
from .session.aiohttp import AiohttpSession


class InboxesClient(AiohttpSession):
    """
    Client for interacting with the Inboxes API using asynchronous HTTP requests.

    Methods:
        delete_inbox(email: str) -> bool:
            Deletes an inbox for the given email.

        create_inbox(email: str) -> bool:
            Creates an inbox for the given email.

        get_messages(email: str) -> list[MessagePreview]:
            Retrieves a list of message previews for the given email.

        get_message(message_id: str) -> Message:
            Retrieves the full message for the given message ID.

        delete_message(message_id: str) -> bool:
            Deletes the message with the given message ID.

        get_attachment(message_id: str, attachment_id: str) -> MessageAttachment:
            Retrieves an attachment for the given message ID and attachment ID.
    """

    async def delete_inbox(self, email: str) -> bool:
        """
        Delete an inbox for the given email.

        Args:
            email (str): The email address of the inbox to delete.

        Returns:
            bool: True if the inbox was deleted, False otherwise.
        """
        result: dict[str, bool] = await self.delete(endpoint=self._url.inbox_url(email=email))
        return cast(bool, result.get("deleted", False))

    async def create_inbox(self, email: str) -> bool:
        """
        Create an inbox for the given email.

        Args:
            email (str): The email address for the new inbox.

        Returns:
            bool: True if the inbox was activated, False otherwise.
        """
        result: dict[str, bool] = await self.post(endpoint=self._url.inbox_url(email=email))
        return cast(bool, result.get("activated", False))

    async def get_messages(self, email: str) -> list[MessagePreview]:
        """
        Retrieve a list of message previews for the given email.

        Args:
            email (str): The email address to retrieve messages for.

        Returns:
            list[MessagePreview]: A list of message previews.
        """
        result = await self.get(endpoint=self._url.inbox_url(email=email))
        return message_preview_list.validate_python(result)

    async def get_message(self, message_id: str) -> Message:
        """
        Retrieve the full message for the given message ID.

        Args:
            message_id (str): The ID of the message to retrieve.

        Returns:
            Message: The full message object.
        """
        result = await self.get(
            endpoint=self._url.message_url(message_id=message_id)
        )
        return Message.model_validate(result)

    async def delete_message(self, message_id: str) -> bool:
        """
        Delete the message with the given message ID.

        Args:
            message_id (str): The ID of the message to delete.

        Returns:
            bool: True if the message was deleted, False otherwise.
        """
        result: dict[str, bool] = await self.delete(
            endpoint=self._url.message_url(message_id=message_id)
        )
        return cast(bool, result.get("deleted", False))

    async def get_attachment(
        self, message_id: str, attachment_id: str
    ) -> MessageAttachment:
        """
        Retrieve an attachment for the given message ID and attachment ID.

        Args:
            message_id (str): The ID of the message containing the attachment.
            attachment_id (str): The ID of the attachment to retrieve.

        Returns:
            MessageAttachment: The attachment object.
        """
        result = await self.get(
            endpoint=self._url.attachment_url(
                message_id=message_id, attachment_id=attachment_id
            )
        )
        return MessageAttachment.model_validate(result)
