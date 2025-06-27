from typing import Optional
import uuid

from ninja import Schema


class CategorySchema(Schema):
    id: uuid.UUID
    name: str
    slug: str
    icon: Optional[str]
