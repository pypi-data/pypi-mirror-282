from typing import List, Optional, Any, Dict

from pydantic import BaseModel
from pydantic.v1 import validator
from pydantic.v1.fields import ModelField


class CorsConfig(BaseModel):
    allowed_origin: str = "*"
    allowed_headers: str = "*"
    allowed_methods: str = "GET,POST,PUT,PATCH,DELETE"


class AuthorizerConfig(BaseModel):
    type: Optional[str] = None
    authorizer_id: Optional[str] = None
    identity_source: Optional[str] = None

    @validator("type", "authorizer_id", pre=True)
    def check_required_fields(
        cls, value: Any, values: Dict[str, Any], field: ModelField
    ) -> Any:
        type = values.get("type", None)
        authorizer_id = values.get("authorizer_id", None)
        if field.name in ["type", "authorizer_id"] and (
            not type or not authorizer_id
        ):
            raise ValueError(
                "Both 'type' and 'authorizer_id' must be provided for "
                "AuthorizerConfig"
            )
        return value


class ResourcePermission(BaseModel):
    resource_type: str
    resource_name: str
    actions: List[str]


class IAMConfig(BaseModel):
    permissions: List[ResourcePermission]
