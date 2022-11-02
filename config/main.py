class MainSettings:
    BOT_TOKEN: str = ''

    # region Recipients
    MY_CHAT_ID: int = 0
    SECOND_CHAT_ID: int = 0
    CHAT_LIST: list[int] = [MY_CHAT_ID, SECOND_CHAT_ID]
    # endregion


__all__ = ('MainSettings', )
