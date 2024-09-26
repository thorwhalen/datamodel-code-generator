# generated by datamodel-codegen:
#   filename:  discriminator_enum.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Literal, Union

from pydantic import BaseModel, Field, RootModel


class RequestVersionEnum(Enum):
    v1 = 'v1'
    v2 = 'v2'


class RequestBase(BaseModel):
    version: RequestVersionEnum


class RequestV1(RequestBase):
    request_id: str = Field(..., description='there is description', title='test title')
    version: Literal['v1'] = 'v1'


class RequestV2(RequestBase):
    version: Literal['v2'] = 'v2'


class Request(RootModel[Union[RequestV1, RequestV2]]):
    root: Union[RequestV1, RequestV2] = Field(..., discriminator='version')
