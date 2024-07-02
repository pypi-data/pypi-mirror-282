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

from uuid import uuid4

import tangosuper
from tangosuper import types
from ..object import Object


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~tangosuper.types.InlineQueryResultCachedAudio`
    - :obj:`~tangosuper.types.InlineQueryResultCachedDocument`
    - :obj:`~tangosuper.types.InlineQueryResultCachedAnimation`
    - :obj:`~tangosuper.types.InlineQueryResultCachedPhoto`
    - :obj:`~tangosuper.types.InlineQueryResultCachedSticker`
    - :obj:`~tangosuper.types.InlineQueryResultCachedVideo`
    - :obj:`~tangosuper.types.InlineQueryResultCachedVoice`
    - :obj:`~tangosuper.types.InlineQueryResultArticle`
    - :obj:`~tangosuper.types.InlineQueryResultAudio`
    - :obj:`~tangosuper.types.InlineQueryResultContact`
    - :obj:`~tangosuper.types.InlineQueryResultDocument`
    - :obj:`~tangosuper.types.InlineQueryResultAnimation`
    - :obj:`~tangosuper.types.InlineQueryResultLocation`
    - :obj:`~tangosuper.types.InlineQueryResultPhoto`
    - :obj:`~tangosuper.types.InlineQueryResultVenue`
    - :obj:`~tangosuper.types.InlineQueryResultVideo`
    - :obj:`~tangosuper.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "tangosuper.Client"):
        pass
