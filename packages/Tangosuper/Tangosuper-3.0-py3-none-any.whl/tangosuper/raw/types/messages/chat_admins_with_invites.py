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


class ChatAdminsWithInvites(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tangosuper.raw.base.messages.ChatAdminsWithInvites`.

    Details:
        - Layer: ``166``
        - ID: ``B69B72D7``

    Parameters:
        admins (List of :obj:`ChatAdminWithInvites <tangosuper.raw.base.ChatAdminWithInvites>`):
            N/A

        users (List of :obj:`User <tangosuper.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: tangosuper.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAdminsWithInvites
    """

    __slots__: List[str] = ["admins", "users"]

    ID = 0xb69b72d7
    QUALNAME = "types.messages.ChatAdminsWithInvites"

    def __init__(self, *, admins: List["raw.base.ChatAdminWithInvites"], users: List["raw.base.User"]) -> None:
        self.admins = admins  # Vector<ChatAdminWithInvites>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminsWithInvites":
        # No flags
        
        admins = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatAdminsWithInvites(admins=admins, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.admins))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
