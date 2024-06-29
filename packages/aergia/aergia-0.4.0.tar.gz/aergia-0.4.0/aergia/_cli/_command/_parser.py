import argparse

from rich_argparse import ArgumentDefaultsRichHelpFormatter

from aergia._cli._command._chat import add_chat_subcommand
from aergia._cli._command._image import add_image_subcommand
from aergia._cli._command._models import add_models_subcommand
from aergia._cli._command._role import add_role_subcommand
from aergia._cli._command._session import add_session_subcommand


def make_parser():
    # fmt: off
    parser = argparse.ArgumentParser(
        prog="ae[rgia]", formatter_class=ArgumentDefaultsRichHelpFormatter
    )
    parser.add_argument(
        "-b", "--backend", type=str, default="openai", help="select backend type"
    )
    parser.add_argument("--version", action="store_true", help="print the version")
    parser.add_argument("--debug", action="store_true", help="enable debug mode")
    parser.add_argument(
        "--log-level",
        default=None,
        choices=["debug", "info", "warn", "error", "critical"],
        help="configure the log-level of the application",
    )
    # fmt: on
    subparsers = parser.add_subparsers(dest="subcommand")

    add_chat_subcommand(subparsers)
    # add_tui_subcommand(subparsers)
    # add_repl_subcommand(subparsers)
    # add_code_subcommand(subparsers)
    add_image_subcommand(subparsers)
    # add_execute_subcommand(subparsers)
    add_session_subcommand(subparsers)
    add_role_subcommand(subparsers)
    # add_info_subcommand(subparsers)
    add_models_subcommand(subparsers)

    return parser
