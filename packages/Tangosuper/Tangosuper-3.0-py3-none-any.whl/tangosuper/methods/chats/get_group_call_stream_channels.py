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

from typing import Union

import tangosuper
from tangosuper import raw


class GetGroupCallStreamChannels:
    async def get_group_call_stream_channels(
            self: "tangosuper.Client",
            call: Union[int, str],
            chat_id: Union[int, str]
    ):
        call = await self.invoke(raw.functions.channels.GetFullChannel(channel=await self.resolve_peer(chat_id)))
        try:
            result = await self.invoke(
                raw.functions.phone.GetGroupCallStreamChannels(
                    call=call.full_chat.call
                )
            )
            return result
        except Exception as e:
            return Exception(e)
