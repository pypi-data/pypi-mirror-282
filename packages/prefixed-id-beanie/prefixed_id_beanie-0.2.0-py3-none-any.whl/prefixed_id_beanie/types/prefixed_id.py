from typing import Any, Optional, List, Type
from pydantic import Field, field_validator, PrivateAttr
from beanie import Document, PydanticObjectId

class PrefixedDocument(Document):
    id: Optional[PydanticObjectId] = Field(default_factory=PydanticObjectId, alias="_id")
    _prefix: str = PrivateAttr()

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._prefix = self.__class__.Settings.collection
    
    @field_validator('id', mode='before')
    def set_prefixed_id(cls, v):
        if isinstance(v, str) and "_" in v:
            return v.split("_", 1)[1]
        return v

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d['id'] = self.id_with_prefix
        return d
    
    @property
    def id_with_prefix(self) -> str:
        return f"{self._prefix}_{self.id}"

    def __repr__(self) -> str:
        return str(self.dict())

    @classmethod
    async def get(cls: Type['PrefixedDocument'], document_id: Any) -> Optional['PrefixedDocument']:
        document_id = cls._strip_prefix(document_id)
        document = await super().get(document_id)
        print(document.dict())
        return document.dict()
    
    @classmethod
    async def find_all(cls: Type['PrefixedDocument']) -> List['PrefixedDocument']:
        documents = await super().find({}).to_list()
        return [doc.dict() for doc in documents]
    
    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d['id'] = self.id_with_prefix
        return d

    @staticmethod
    def _strip_prefix(value: Any) -> str:
        if isinstance(value, str) and "_" in value:
            return value.split("_", 1)[1]
        return value

    def json(self, *args, **kwargs) -> str:
        d = self.dict(*args, **kwargs)
        return super().json(*args, **kwargs)
