#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2023 Dan <https://github.com/delivrance>
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

import re
from datetime import datetime
from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from .exceptions.all import exceptions

if TYPE_CHECKING:
    from hydrogram import raw
    from hydrogram.raw.core import TLObject


class RPCError(Exception):
    ID = None
    CODE = None
    NAME = None
    MESSAGE = "{value}"

    def __init__(
        self,
        value: int | str | raw.types.RpcError = None,
        rpc_name: str | None = None,
        is_unknown: bool = False,
        is_signed: bool = False,
    ):
        super().__init__(
            "Telegram says: [{}{} {}] - {} {}".format(
                "-" if is_signed else "",
                self.CODE,
                self.ID or self.NAME,
                self.MESSAGE.format(value=value),
                f'(caused by "{rpc_name}")' if rpc_name else "",
            )
        )

        try:
            self.value = int(value)
        except (ValueError, TypeError):
            self.value = value

        if is_unknown:
            with Path("unknown_errors.txt").open("a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}\t{value}\t{rpc_name}\n")

    @staticmethod
    def raise_it(rpc_error: raw.types.RpcError, rpc_type: type[TLObject]):
        error_code = rpc_error.error_code
        is_signed = error_code < 0
        error_message = rpc_error.error_message
        rpc_name = ".".join(rpc_type.QUALNAME.split(".")[1:])

        if is_signed:
            error_code = -error_code

        if error_code not in exceptions:
            raise UnknownError(
                value=f"[{error_code} {error_message}]",
                rpc_name=rpc_name,
                is_unknown=True,
                is_signed=is_signed,
            )

        error_id = re.sub(r"_\d+", "_X", error_message)

        if error_id not in exceptions[error_code]:
            raise getattr(import_module("hydrogram.errors"), exceptions[error_code]["_"])(
                value=f"[{error_code} {error_message}]",
                rpc_name=rpc_name,
                is_unknown=True,
                is_signed=is_signed,
            )

        value = re.search(r"_(\d+)", error_message)
        value = value[1] if value is not None else value

        raise getattr(import_module("hydrogram.errors"), exceptions[error_code][error_id])(
            value=value, rpc_name=rpc_name, is_unknown=False, is_signed=is_signed
        )


class UnknownError(RPCError):
    CODE = 520
    """:obj:`int`: Error code"""
    NAME = "Unknown error"
