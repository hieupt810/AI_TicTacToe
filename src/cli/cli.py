from app.base.engine import TicTacToe

from cli.args import parse_args
from client.console.renderers import ConsoleRenderer


def main() -> None:
    player1, player2, starting_mark = parse_args()
    TicTacToe(player1, player2, ConsoleRenderer()).play(starting_mark)
