import urllib.parse
from dataclasses import dataclass
from typing import AnyStr, TypeAlias

URLType: TypeAlias = str | "URL"
urljoin = urllib.parse.urljoin
quote_plus = urllib.parse.quote_plus


@dataclass
class URL:
    """
    A class representing a URL, providing methods to join URL parts and generate specific endpoint URLs.

    Attributes:
        base_url (str): The base URL for constructing full URLs.
    """

    base_url: str

    def __post_init__(self) -> None:
        """Ensure the base_url is correctly formatted."""
        self.base_url = "https://" + self.base_url.lstrip("https://")

    def join(self, *parts: str) -> str:
        """
        Join parts of a URL with the base URL.

        Args:
            parts (str): Parts of the URL to join.

        Returns:
            str: The full URL.
        """
        if parts and parts[0].startswith(self.base_url):
            return multi_urljoin(*parts)
        return multi_urljoin(self.base_url, *parts)

    def inbox_url(self, email: str) -> str:
        """
        Generate an inbox URL for the given email.

        Args:
            email (str): The email address for the inbox.

        Returns:
            str: The inbox URL.
        """
        return self.join("inboxes", email)

    def domains_url(self) -> str:
        """
        Generate the domains URL.

        Returns:
            str: The domains URL.
        """
        return self.join("domains")

    def message_url(self, message_id: str) -> str:
        """
        Generate a message URL for the given message ID.

        Args:
            message_id (str): The message ID.

        Returns:
            str: The message URL.
        """
        return self.join("messages", message_id)

    def attachment_url(self, message_id: str, attachment_id: str) -> str:
        """
        Generate an attachment URL for the given message ID and attachment ID.

        Args:
            message_id (str): The message ID.
            attachment_id (str): The attachment ID.

        Returns:
            str: The attachment URL.
        """
        return self.join("attachments", message_id, attachment_id)

    __call__ = join


# Instantiate API_URL
API_URL = URL("https://inboxes-com.p.rapidapi.com")


def multi_urljoin(*parts: str) -> str:
    """
    Join multiple parts of a URL with proper quoting and slashes.

    Args:
        parts (str): Parts of the URL to join.

    Returns:
        str: The full URL.
    """
    base = parts[0]
    for part in parts[1:]:
        base = urljoin(base, quote_plus(part.strip("/"), safe="/"))
    return base


def stringify_url(url: URLType) -> str:
    """
    Convert a URLType to a string.

    Args:
        url (URLType): The URL to stringify.

    Returns:
        str: The string representation of the URL.
    """
    if isinstance(url, (str, bytes)):
        return url
    return url.base_url


def ignore_part(part: str, url: URLType) -> str:
    """
    Remove a specific part from the URL.

    Args:
        part (str): The part of the URL to remove.
        url (URLType): The URL from which to remove the part.

    Returns:
        str: The URL with the specified part removed.
    """
    return stringify_url(url).replace(part, "", 1)


def normalize_url(url: URLType | None) -> URL:
    """
    Normalize the URL to an instance of the URL class.

    Args:
        url (URLType | None): The URL to normalize.

    Returns:
        URL: The normalized URL instance.
    """
    if url is None:
        return API_URL
    if isinstance(url, URL):
        return url
    return URL(url)
