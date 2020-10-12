from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Post:
    id: int
    headline: str
    text: str
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class ContactMe:
    name: str
    email: str
    message: str
