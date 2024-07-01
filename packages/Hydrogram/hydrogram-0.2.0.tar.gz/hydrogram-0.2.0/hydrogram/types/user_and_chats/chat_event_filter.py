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

from hydrogram import raw
from hydrogram.types.object import Object


class ChatEventFilter(Object):
    """Set of filters used to obtain a chat event log.

    Parameters:
        new_restrictions (``bool``, *optional*):
            True, if member restricted/unrestricted/banned/unbanned events should be returned.
            Defaults to False.

        new_privileges (``bool``, *optional*):
            True, if member promotion/demotion events should be returned.
            Defaults to False.

        new_members (``bool``, *optional*):
            True, if members joining events should be returned.
            Defaults to False.

        chat_info (``bool``, *optional*):
            True, if chat info changes should be returned. That is, when description, linked chat, location, photo,
            sticker set, title or username have been modified.
            Defaults to False.

        chat_settings (``bool``, *optional*):
            True, if chat settings changes should be returned. That is, when invites, hidden history, message
            signatures, default chat permissions have been modified.
            Defaults to False.

        invite_links (``bool``, *optional*):
            True, if invite links events (edit, revoke, delete) should be returned.
            Defaults to False.

        deleted_messages (``bool``, *optional*):
            True, if deleted messages events should be returned.
            Defaults to False.

        edited_messages (``bool``, *optional*):
            True, if edited messages events, including closed polls, should be returned.
            Defaults to False.

        pinned_messages (``bool``, *optional*):
            True, if pinned/unpinned messages events should be returned.
            Defaults to False.

        leaving_members (``bool``, *optional*):
            True, if members leaving events should be returned.
            Defaults to False.

        video_chats (``bool``, *optional*):
            True, if video chats events should be returned.
            Defaults to False.
    """

    def __init__(
        self,
        *,
        new_restrictions: bool = False,
        new_privileges: bool = False,
        new_members: bool = False,
        chat_info: bool = False,
        chat_settings: bool = False,
        invite_links: bool = False,
        deleted_messages: bool = False,
        edited_messages: bool = False,
        pinned_messages: bool = False,
        leaving_members: bool = False,
        video_chats: bool = False,
    ):
        super().__init__()

        self.new_restrictions = new_restrictions
        self.new_privileges = new_privileges
        self.new_members = new_members
        self.chat_info = chat_info
        self.chat_settings = chat_settings
        self.invite_links = invite_links
        self.deleted_messages = deleted_messages
        self.edited_messages = edited_messages
        self.pinned_messages = pinned_messages
        self.leaving_members = leaving_members
        self.video_chats = video_chats

    def write(self) -> "raw.base.ChannelAdminLogEventsFilter":
        join = False
        invite = False
        ban = False
        unban = False
        kick = False
        unkick = False
        promote = False
        demote = False
        delete = False
        group_call = False
        invites = False

        if self.new_restrictions:
            ban = True
            unban = True
            kick = True
            unkick = True

        if self.new_privileges:
            promote = True
            demote = True

        if self.new_members:
            join = True
            invite = True

        info = bool(self.chat_info)
        settings = bool(self.chat_settings)
        if self.invite_links:
            invites = True

        if self.deleted_messages:
            delete = True

        edit = bool(self.edited_messages)
        pinned = bool(self.pinned_messages)
        leave = bool(self.leaving_members)
        if self.video_chats:
            group_call = True

        return raw.types.ChannelAdminLogEventsFilter(
            join=join,
            leave=leave,
            invite=invite,
            ban=ban,
            unban=unban,
            kick=kick,
            unkick=unkick,
            promote=promote,
            demote=demote,
            info=info,
            settings=settings,
            pinned=pinned,
            edit=edit,
            delete=delete,
            group_call=group_call,
            invites=invites,
        )
