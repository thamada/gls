#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from tabulate import tabulate
from colorama import Fore, Style
import pandas as pd
import sys
import subprocess
import argparse
from gls.database import gpu_data # database.pyからgpu_dataをimport

def change_df(dataFrame):
    # 特定のキーを持つ列を削除
    df = dataFrame
    df = df.drop(columns=['url'])
    df = df.drop(columns=['vram_ecc'])

    # 列の並びを変更したDataFrameを作成
    new_column_order = ['product', 'tflops_fp32', 'tflops_fp16', 'vram_bw', 'tdp', 'vram_size', 'n_sp_core', 'n_mp', 'gpu_clock', 'system_interface', 'n_tensor_core', 'tflops_fp8_tensor', 'gpu_chip', 'gpu_arch']
    df = df[new_column_order]

    # FP32列でソート
    df = df.sort_values(by='tflops_fp32', ascending=False)

    # ------------------
    # 'product' 列を左寄せにするスタイルを適用(少々ややこしいので注意)
    # 'product'列の幅を求める
    max_product_length = df['product'].apply(len).max()
    # 'product'列を左寄せで整形
    df['product'] = df['product'].apply(lambda x: f"{x:<{max_product_length}}")
    # ------------------

    # 該当列を小数点表記のフォーマット指定(%.1fなど)
    df['tflops_fp16'] = df['tflops_fp16'].apply(lambda x: '%.1f' % x if pd.notna(x) else x)
    df['tflops_fp32'] = df['tflops_fp32'].apply(lambda x: '%.1f' % x if pd.notna(x) else x)
    df['tflops_fp8_tensor'] = df['tflops_fp8_tensor'].apply(lambda x: '%.1f' % x if pd.notna(x) else x)
    df['vram_bw'] = df['vram_bw'].apply(lambda x: '%.1f' % x if pd.notna(x) else x)
    df['gpu_clock'] = df['gpu_clock'].apply(lambda x: '%.2f' % (x/1000.0) if pd.notna(x) else x)

    # 列の文字数を最大7文字に制限
    df['gpu_chip'] = df['gpu_chip'].apply(lambda x: x[:7] if pd.notna(x) else x)


    # 列の名前を変更
    df = df.rename(columns={'tflops_fp16': 'FP16'})
    df = df.rename(columns={'tflops_fp32': 'FP32'})
    df = df.rename(columns={'vram_size': 'GB'})
    df = df.rename(columns={'vram_bw': 'GB/s'})
    df = df.rename(columns={'n_sp_core': 'SPs'})
    df = df.rename(columns={'n_mp': 'MPs'})
    df = df.rename(columns={'gpu_clock': 'GHz'})
    df = df.rename(columns={'system_interface': 'interface'})
    df = df.rename(columns={'n_tensor_core': 'TCs'})
    df = df.rename(columns={'tflops_fp8_tensor': 'FP8_TC'})
    df = df.rename(columns={'tdp': 'TDP'})
    df = df.rename(columns={'gpu_chip': 'ASIC'})
    df = df.rename(columns={'gpu_arch': 'arch'})

    return df


# 説明
#   dataFieldのタイトル行を整形した文字列に変換する:
#   tabulateを使って表を整形し、coloramaを使ってタイトル行をカラー表示にする。
#   styled_headerで各カラム名にカラーを設定してから、tabulate関数で出力することで、タイトル行のみ色付きで表示します。
def set_title_colored(dataField): 
    df = dataField
    styled_header_0 = [Fore.GREEN + Style.BRIGHT + col + Style.RESET_ALL for col in change_df(df).columns]
    styled_header_1 = [Fore.MAGENTA + Style.BRIGHT + col + Style.RESET_ALL for col in change_df(df).columns]
    str_output = tabulate(change_df(df), headers=styled_header_1, tablefmt="plain", showindex=False)
    return str_output

# 説明
#   table_string自体を書き換えてタイトル行の直下に下線を挿入する。
#   re.sub(r'\x1b\[[0-9;]*m', '', header_line)を使用して、ANSIカラーコード
#   （Fore.CYANやStyle.BRIGHTなどのカラーコード）を除去し、純粋なテキスト
#   のみのタイトル行を作成する。
#   このクリーンなタイトル行に基づいてheader_line_lengthを計算し、適切な長
#   さの下線を生成する。
def set_title_underline(table_string: str) -> str:
    # タイトル行の長さを取得して、下線を生成
    header_line = table_string.splitlines()[0]
    header_line_length = len(header_line)
    underline = "=" * header_line_length

    # タイトル行の長さを取得し、下線を生成
    header_line = table_string.splitlines()[0]
    plain_header_line = re.sub(r'\x1b\[[0-9;]*m', '', header_line)  # ANSIカラーコードを除去
    underline = "=" * len(plain_header_line)

    # タイトル行と下線をtable_stringに挿入
    lines = table_string.splitlines()
    table_string_with_underline = "\n".join([lines[0], underline] + lines[1:])

    return table_string_with_underline


# 説明
# set_title_underline関数で、タイトル行に下線を追加しています。
# apply_row_colors関数で、各行に交互に色を適用しています。
# 偶数行にFore.LIGHTBLACK_EX（グレー）を、奇数行にFore.WHITE（白）を適用しています。
# 最後にfinal_table_stringを出力することで、タイトル行の下に下線が引かれ、各行が交互に色付けされたテーブルが表示されます。
def apply_row_colors(table_string: str) -> str:
    # 各行に色を交互に適用
    lines = table_string.splitlines()
    styled_lines = []
    styled_lines.append(lines[0]) # ヘッダー行はそのまま追加
    styled_lines.append(lines[1]) # underline行もそのまま

    for i, line in enumerate(lines[2:]):
        if i % 2 == 0:
            styled_lines.append(Fore.LIGHTGREEN_EX + line + Style.RESET_ALL)  # 偶数行をグレーに
        else:
            styled_lines.append(Fore.LIGHTCYAN_EX + line + Style.RESET_ALL)  # 奇数行を白に

    return "\n".join(styled_lines)



def create_cache_directory(path: str) -> None:
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)

def main():
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description='GLS Command Tool')
    parser.add_argument('--upgrade', '--update', action='store_true', help='Upgrade the gls command to the latest version')
    parser.add_argument('--remove', '--uninstall', action='store_true', help='Uninstall the gls command')
    args = parser.parse_args()

    # '--upgrade' オプションが指定された場合の処理
    if args.upgrade:
        print('Upgrading gls to the latest version...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'git+https://github.com/thamada/gls.git'])
            print('gls has been upgraded to the latest version.')
        except subprocess.CalledProcessError as e:
            print('An error occurred while upgrading gls:', e)
        sys.exit(0)

    # '--remove' オプションが指定された場合の処理
    if args.remove:
        print('Uninstalling gls...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', 'gls'])
            print('gls has been uninstalled.')
        except subprocess.CalledProcessError as e:
            print('An error occurred while uninstalling gls:', e)
        sys.exit(0)


    # 辞書gpu_dataをDataFrameに変換
    gpu_df = pd.DataFrame(gpu_data)

    # CSV/HTML形式で出力
    # index=False を指定することで、行番号（インデックス）を CSV ファイルに含めません。
    create_cache_directory('/tmp/gls.cache')
    gpu_df.to_csv('/tmp/gls.cache/output.csv', index=False)
    gpu_df.to_html('/tmp/gls.cache/output.html', index=False)

    # 各種整形後に標準出力
    table_str1 = set_title_colored(gpu_df) # タイトル行に色付け
    table_str2 = set_title_underline(table_str1) # 下線行を挿入
    table_str3 = apply_row_colors(table_str2) # 行に色付け
    print(table_str3)

if __name__ == '__main__':
    main()
