#!/usr/bin/env python3
import os
import curses

def curses_main(stdscr):
    # Curses setup
    curses.curs_set(0)
    stdscr.clear()

    options = [
        "NVIDIA GH200",
        "NVIDIA GTX1050Ti",
        "NVIDIA H100 SXM x8",
        "NVIDIA H100 NVL x2",
        "NVIDIA RTX 2000 Ada",
        "NVIDIA RTX 4000 Ada",
        "NVIDIA RTX 6000 Ada x8",
        "NVIDIA RTX A6000 x9",
        "NVIDIA RTX 4060 Ti",
        "NVIDIA RTX 4090",
        "NVIDIA L40S",
        "NVIDIA L4",
        "NVIDIA A100 SXM x4",
        "NVIDIA RTX 3090",
        "NVIDIA A40 x10",
        "NVIDIA A10",
        "NVIDIA V100 x8",
        "AMD MI300X"
    ]

    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()


        for idx, option in enumerate(options):
            x = width // 2 - len(options[0]) // 2  # 中央に配置するためのx座標計算（左寄せ）
            y = height // 2 - len(options) // 2 + idx  # 中央に配置するためのy座標計算
            if idx == current_row:
                stdscr.addstr(y, x, option, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord('\n'):
            fname_config = "~/.glsconfig"
            create_file(fname_config, options[current_row])
            break

    stdscr.refresh()

def create_file(filename, content):

    # '~' を展開して絶対パスに変換
    filepath = os.path.expanduser(filename)

    # ファイルのディレクトリが存在するか確認し、存在しない場合は作成
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    '''
    if os.path.exists(filepath):
        overwrite = input(f"ファイル '{filepath}' は既に存在します。上書きしますか？ (y/n): ")
        if overwrite.lower() != 'y':
            print("\nファイル作成をキャンセルしました。")
            return
    '''

    with open(filepath, "w") as f:
        f.write(content)
        f.write("\n")
    print(f"\nファイル '{filepath}' が作成されました。")


def main():
    curses.wrapper(curses_main)

if __name__ == "__main__":
    main()

