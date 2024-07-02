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


class UpdateColor(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``621A201F``

    Parameters:
        channel (:obj:`InputChannel <tangosuper.raw.base.InputChannel>`):
            N/A

        color (``int`` ``32-bit``):
            N/A

        background_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <tangosuper.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "color", "background_emoji_id"]

    ID = 0x621a201f
    QUALNAME = "functions.channels.UpdateColor"

    def __init__(self, *, channel: "raw.base.InputChannel", color: int, background_emoji_id: Optional[int] = None) -> None:
        self.channel = channel  # InputChannel
        self.color = color  # int
        self.background_emoji_id = background_emoji_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateColor":
        
        flags = Int.read(b)
        
        channel = TLObject.read(b)
        
        color = Int.read(b)
        
        background_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return UpdateColor(channel=channel, color=color, background_emoji_id=background_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.background_emoji_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.color))
        
        if self.background_emoji_id is not None:
            b.write(Long(self.background_emoji_id))
        
        return b.getvalue()
