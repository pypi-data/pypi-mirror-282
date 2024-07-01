#  Hydrogram - Telegram MTProto API Client Library for Python
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

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ResetTopPeerRating(TLObject):  # type: ignore
    """Reset rating of top peer


    Details:
        - Layer: ``181``
        - ID: ``1AE373AC``

    Parameters:
        category (:obj:`TopPeerCategory <hydrogram.raw.base.TopPeerCategory>`):
            Top peer category

        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer whose rating should be reset

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["category", "peer"]

    ID = 0x1ae373ac
    QUALNAME = "functions.contacts.ResetTopPeerRating"

    def __init__(self, *, category: "raw.base.TopPeerCategory", peer: "raw.base.InputPeer") -> None:
        self.category = category  # TopPeerCategory
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetTopPeerRating":
        # No flags
        
        category = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        return ResetTopPeerRating(category=category, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.category.write())
        
        b.write(self.peer.write())
        
        return b.getvalue()
