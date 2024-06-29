from pydantic import BaseModel

class FriendRequestMessage:
    def __init__(self, sender_name: str, receiver_name: str):
        self.sender_name = sender_name
        self.receiver_name = receiver_name


class FriendAcceptanceMessage:
    def __init__(self, user_name: str, friend_name: str):
        self.user_name = user_name
        self.friend_name = friend_name


class StatusMessage:
    def __init__(self, username: str, status_text: str):
        self.username = username
        self.status_text = status_text

class MessageResponse(BaseModel):
    message: str
