**INBOXES_API** Simple wrapper over https://inboxes.com API, for generating and work with temporary emails

***Example***

```python
import asyncio
import os

from inboxes_api import InboxesClient


async def main():
    
    example_email = "example@example.com"
    
    client = InboxesClient(access_token=os.environ["INBOXES_ACCESS_TOKEN"])
    
    await client.create_inbox(email=example_email)
    
    email_messages_previews = await client.get_messages(email=example_email)
    
    for message_preview in email_messages_previews:
        message = await client.get_message(message_id=message_preview.id)
        
        sender = message.sender
        reciever = message.reciever
        subject = message.subject
        created_at = message.created_at
        text = message.text
    
    await client.delete_inbox(email=example_email)


if __name__ == "__main__":
    asyncio.run(main())
```