from typing import Any, Optional, List, Type
from pydantic import Field, PrivateAttr
from beanie import Document, PydanticObjectId

class InvalidPrefixError(Exception):
    def __init__(self, expected_prefix):
        self.expected_prefix = expected_prefix
        super().__init__(f"Invalid prefix. Expected prefix: {expected_prefix}")

class PrefixedDocument(Document):
    id: Optional[PydanticObjectId] = Field(default_factory=PydanticObjectId, alias="_id")
    _prefix: str = PrivateAttr()

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._prefix = self.__class__.Settings.name
    
    def __repr__(self) -> str:
        return str(self.dict())
    
    @property
    def id_with_prefix(self) -> str:
        return f"{self._prefix}_{self.id}"

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d['id'] = self.id_with_prefix
        return d
    
    @classmethod
    def _strip_prefix(cls, value: Any) -> str:
        if isinstance(value, str) and "_" in value:
            prefix, actual_id = value.split("_", 1)
            if prefix != cls.Settings.name:
                raise InvalidPrefixError(cls.Settings.name)
            return actual_id
        return value
    
    @classmethod
    async def get(cls: Type['PrefixedDocument'], document_id: Any) -> Optional['PrefixedDocument']:
        document_id = cls._strip_prefix(document_id)
        document = await super().get(document_id)
        print(document.dict())
        return document.dict()
    
    @classmethod
    async def find_all(cls: Type['PrefixedDocument']) -> List['PrefixedDocument']:
        documents = await super().find_all().to_list()
        return [doc.dict() for doc in documents]
