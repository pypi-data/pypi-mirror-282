#  Tangosuper - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Tangosuper.
#
#  Tangosuper is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Tangosuper is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Tangosuper.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from tangosuper.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from tangosuper.raw.core import TLObject
from tangosuper import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ChatsSlice(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tangosuper.raw.base.messages.Chats`.

    Details:
        - Layer: ``166``
        - ID: ``9CD81144``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        chats (List of :obj:`Chat <tangosuper.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: tangosuper.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetChats
            messages.GetCommonChats
            channels.GetChannels
            channels.GetAdminedPublicChannels
            channels.GetLeftChannels
            channels.GetGroupsForDiscussion
            stories.GetChatsToSend
    """

    __slots__: List[str] = ["count", "chats"]

    ID = 0x9cd81144
    QUALNAME = "types.messages.ChatsSlice"

    def __init__(self, *, count: int, chats: List["raw.base.Chat"]) -> None:
        self.count = count  # int
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatsSlice":
        # No flags
        
        count = Int.read(b)
        
        chats = TLObject.read(b)
        
        return ChatsSlice(count=count, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.chats))
        
        return b.getvalue()
