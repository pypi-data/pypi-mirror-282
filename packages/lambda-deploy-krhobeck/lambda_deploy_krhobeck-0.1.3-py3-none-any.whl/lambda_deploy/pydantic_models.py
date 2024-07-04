from typing import List, Optional, Any, Dict

from pydantic import BaseModel
from pydantic.v1 import validator
from pydantic.v1.fields import ModelField


class CorsConfig(BaseModel):
    allowed_origin: str = "*"
    allowed_headers: str = "*"
    allowed_methods: str = "GET,POST,PUT,PATCH,DELETE"


class ResourcePermission(BaseModel):
    resource_type: str
    resource_name: str
    actions: List[str]


class IAMConfig(BaseModel):
    permissions: List[ResourcePermission]
