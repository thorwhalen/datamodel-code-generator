# generated by datamodel-codegen:
#   filename:  test.yml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from msgspec import Meta, Struct
from typing_extensions import Annotated


class Test(Struct):
    uid: Annotated[
        str,
        Meta(
            description='ulid of this object',
            pattern='[0-9ABCDEFGHJKMNPQRSTVWXYZ]{26,26}',
        ),
    ]