# generated by datamodel-codegen:
#   filename:  strict_types.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    StrictBool,
    StrictBytes,
    StrictInt,
    StrictStr,
    confloat,
    conint,
    constr,
)


class User(BaseModel):
    name: Optional[StrictStr] = Field(None, example='ken')
    age: Optional[StrictInt] = None
    salary: Optional[conint(ge=0, strict=True)] = None
    debt: Optional[conint(le=0, strict=True)] = None
    loan: Optional[confloat(le=0.0, strict=True)] = None
    tel: Optional[
        constr(regex=r'^(\([0-9]{3}\))?[0-9]{3}-[0-9]{4}$', strict=True)
    ] = None
    height: Optional[confloat(ge=0.0, strict=True)] = None
    weight: Optional[confloat(ge=0.0, strict=True)] = None
    score: Optional[confloat(ge=1e-08, strict=True)] = None
    active: Optional[StrictBool] = None
    photo: Optional[StrictBytes] = None