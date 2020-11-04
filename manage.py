"""Django's command-line utility for administrative tasks."""
import os
import sys

from nickcan_bot.systemconfig import System

def django_main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nickcan_bot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def discord_main():
    from extdiscord import run_server

    run_server()


def ping_spam():
    from extutils import activate_ping_spam

    activate_ping_spam(System.PingSpamWaitSeconds)


if __name__ == '__main__':
    if sys.argv[1] == "runserver":
        discord_main()
        ping_spam()
    django_main()
