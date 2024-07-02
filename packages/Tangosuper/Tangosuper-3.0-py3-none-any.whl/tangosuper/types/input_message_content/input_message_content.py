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

import tangosuper

from ..object import Object

"""- :obj:`~tangosuper.types.InputLocationMessageContent`
    - :obj:`~tangosuper.types.InputVenueMessageContent`
    - :obj:`~tangosuper.types.InputContactMessageContent`"""


class InputMessageContent(Object):
    """Content of a message to be sent as a result of an inline query.

    Tangosuper currently supports the following types:

    - :obj:`~tangosuper.types.InputTextMessageContent`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: "tangosuper.Client", reply_markup):
        raise NotImplementedError
