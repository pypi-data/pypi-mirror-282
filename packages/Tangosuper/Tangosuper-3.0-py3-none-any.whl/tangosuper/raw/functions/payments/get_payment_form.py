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


class GetPaymentForm(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``37148DBB``

    Parameters:
        invoice (:obj:`InputInvoice <tangosuper.raw.base.InputInvoice>`):
            N/A

        theme_params (:obj:`DataJSON <tangosuper.raw.base.DataJSON>`, *optional*):
            N/A

    Returns:
        :obj:`payments.PaymentForm <tangosuper.raw.base.payments.PaymentForm>`
    """

    __slots__: List[str] = ["invoice", "theme_params"]

    ID = 0x37148dbb
    QUALNAME = "functions.payments.GetPaymentForm"

    def __init__(self, *, invoice: "raw.base.InputInvoice", theme_params: "raw.base.DataJSON" = None) -> None:
        self.invoice = invoice  # InputInvoice
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPaymentForm":
        
        flags = Int.read(b)
        
        invoice = TLObject.read(b)
        
        theme_params = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetPaymentForm(invoice=invoice, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))
        
        b.write(self.invoice.write())
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        return b.getvalue()
