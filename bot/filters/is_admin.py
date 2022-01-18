from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsAdmin(BoundFilter):
    """
    Filter for checking user for having administrative status
    """

    def __init__(self, is_admin: bool):
        """
        Initializes self
        :param is_admin: Is admin or not?
        """
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        admins = map(lambda admin: admin.user.id, await message.chat.get_administrators())

        return self.is_admin is (message.from_user.id in admins)