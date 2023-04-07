from typing import Iterable

from feelings_bot.config import settings


def add_chat(chat_id: int) -> Iterable[int]:
    unique_chat_ids = set(_load_chats())
    unique_chat_ids.add(chat_id)
    _dump_chats(unique_chat_ids)
    return unique_chat_ids


def get_chats() -> Iterable[int]:
    return _load_chats()


def _dump_chats(chat_ids: Iterable[int]) -> None:
    (
        open(settings.CHATS_FILE, 'w')
        .writelines(map(_to_line, chat_ids))
    )


def _load_chats() -> Iterable[int]:
    with open(settings.CHATS_FILE, 'r') as users_file:
        return set(map(int, users_file.readlines()))


def _to_line(chat_id: int) -> str:
    return f'{chat_id}\n'
