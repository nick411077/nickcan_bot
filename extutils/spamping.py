import time
from threading import Thread

import requests

from nickcan_bot.systemconfig import HostUrl


__all__ = ["activate_ping_spam"]


def _spam_ping_(cd_sec: int, retry_sec: int = 60):
    # Prevent from sleep
    while True:
        try:
            requests.get(HostUrl)
            print(f"Ping spammed to {HostUrl}.")
            time.sleep(cd_sec)
        except (requests.exceptions.ConnectionError, ConnectionRefusedError):
            print(f"Ping failed to spam on {HostUrl}. ConnectionError. Retry in {retry_sec} seconds.")
            time.sleep(retry_sec)


def activate_ping_spam(cd_sec: int, retry_sec: int = 60):
    Thread(target=_spam_ping_, args=(cd_sec, retry_sec)).start()
