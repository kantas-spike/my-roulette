import argparse
import sys
from random import randint
import time
from math import ceil

# デフォルト設定値
DEFAULT_START_NUM = 1
DEFAULT_END_NUM = 6
DEFAULT_SPIN_DURATION = 1.5

# スリープ時間(秒)
SLEEP_SEC = 0.1

# スピナー
SPINNER_LETTERS = ["|", "/", "-", "\\"]
SPINNER_LETTERS_SIZE = len(SPINNER_LETTERS)

# ターミナル制御用シーケンス
CS_CSI = "\033["  # エスケープ
CS_ERASE_LINE = f"{CS_CSI}2K"  # 行クリア
CS_HEAD_OF_LINE = f"{CS_CSI}1G"  # 行頭移動
CS_INVERT_COLORS = f"{CS_CSI}7m"  # 文字・背景色反転
CS_RESET_COLORS = f"{CS_CSI}0m"  # 色リセット


def get_spin_count(spin_duration: float) -> int:
    """
    スピナーの表示回数

    :param spin_duration: スピナーを表示する時間
    """
    return int(ceil(spin_duration / SLEEP_SEC))


def pick_number(start: int, end: int) -> int:
    """
    数値を取得する

    :param start: ルーレットの開始番号
    :param end: ルーレットの終了番号
    """
    return randint(start, end)


def print_with_spinner(num: int, sleep_idx: int) -> None:
    """
    1つ分のスピナーを表示する

    :param num: ルーレットの番号
    :param sleep_idx: スリープ番号
    """
    sys.stderr.write(f"{CS_ERASE_LINE}{CS_HEAD_OF_LINE}{CS_INVERT_COLORS}")
    sys.stderr.write(
        f"{num}{CS_RESET_COLORS} {SPINNER_LETTERS[sleep_idx % SPINNER_LETTERS_SIZE]}"
    )
    sys.stderr.write(f"{CS_HEAD_OF_LINE}")
    sys.stderr.flush()


def print_selected(num: int) -> None:
    """
    ルーレットで選択された番号を表示する

    :param num: 選択された番号
    """
    sys.stderr.write(f"{CS_ERASE_LINE}{CS_HEAD_OF_LINE}")
    sys.stderr.flush()
    sys.stdout.write(f"{num}")
    sys.stdout.write("\n")
    sys.stdout.flush()


def sleep(sec: float):
    """time.sleepのラッパー

    :param sec: スリープする秒数
    """
    time.sleep(sec)


def show_spinner(start: int, end: int, spin_times: int) -> None:
    """
    指定されたスピン回数分のスピナーを表示する

    :param start: ルーレットの開始番号
    :param end: ルーレットの終了番号
    :param sleep_times: スリープ回数
    """
    for i in range(spin_times):
        picked = pick_number(start, end)
        print_with_spinner(picked, i)
        sleep(SLEEP_SEC)


def parse_args() -> argparse.Namespace:
    """
    CLI引数をパースする
    """
    parser = argparse.ArgumentParser(
        prog="my-roulette",
        description="指定された範囲の数値または文字列をランダムに表示する。",
    )
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        metavar="START_NUM",
        default=DEFAULT_START_NUM,
        help=f"ランダムに表示する数値範囲の開始番号. (デフォルト値: {DEFAULT_START_NUM})",
    )

    parser.add_argument(
        "-e",
        "--end",
        type=int,
        metavar="END_NUM",
        default=DEFAULT_END_NUM,
        help=f"ランダムに表示する数値範囲の終了番号. (デフォルト値: {DEFAULT_END_NUM})",
    )

    parser.add_argument(
        "-d",
        "--spin-duration",
        type=float,
        metavar="SPIN_DURATION",
        default=DEFAULT_SPIN_DURATION,
        help=f"ルーレットが回る秒数. (デフォルト値: {DEFAULT_SPIN_DURATION})",
    )
    return parser.parse_args()


def main() -> None:
    """
    main関数

    スピン回数分スピナーを表示後、
    ルーレットで選択された番号を表示する
    """

    # CLI引数を解析
    args = parse_args()

    # ルーレットの数値の範囲を取得
    start, end = args.start, args.end
    if start > end:
        start, end = end, start

    # スピナーの表示回数を取得
    spin_count = get_spin_count(args.spin_duration)

    # スピナーを表示
    show_spinner(start, end, spin_count)

    # ランダムな数値を取得
    picked = pick_number(start, end)
    # 数値を表示
    print_selected(picked)
