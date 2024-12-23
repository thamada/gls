#!/usr/bin/env python3
import os
import curses

def curses_main(stdscr):
    # Curses setup
    curses.curs_set(0)
    stdscr.clear()

    # 色の初期化
    curses.start_color()
    #curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

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
        "NVIDIA RTX 3070",
        "NVIDIA RTX 3090",
        "NVIDIA GTX 1050 Ti",
        "NVIDIA GTX 680",
        "AMD MI300X"
    ]

    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()


        for idx, option in enumerate(options):
            i_text = "%02s: %s" % (idx+1, option)
            x = width // 2 - len(options[0]) // 2  # 中央に配置するためのx座標計算（左寄せ）
            y = height // 2 - len(options) // 2 + idx  # 中央に配置するためのy座標計算
            if idx == current_row:
                stdscr.addstr(y, x, i_text, curses.color_pair(1))
            else:
                stdscr.addstr(y, x, i_text)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == ord('\n'):
            fname_config = "~/.glsconfig"
            content = ""
            content += f"{current_row}\n"
            content += f"{options[current_row]}\n"
            create_file(fname_config, content)
            break

    stdscr.refresh()

def create_file(filename, content):

    # '~' を展開して絶対パスに変換
    filepath = os.path.expanduser(filename)

    # ファイルのディレクトリが存在するか確認し、存在しない場合は作成
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w") as f:
        f.write(content)
    print(f"\nファイル '{filepath}' が作成されました。")


def main():
    curses.wrapper(curses_main)

if __name__ == "__main__":
    main()

