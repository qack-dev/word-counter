#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# グローバル定数を宣言（慣習としてすべて大文字）
TEXT_DIR = 'text'
PRINT_CNT = 20

# テキストファイルを開く
def open_text_file(name):
    # 相対パスを付与
    fileName = os.path.join(TEXT_DIR, name)
    words = {}
    try:
        # ファイルを開く
        with open(fileName, 'r', encoding='utf-8') as f:
            # 1行ずつメモリに読み込み
            for line in f:
                # 大文字を小文字へ変換
                line = line.lower()
                # 不要な文字列を削除
                targets = ['\n', '.', ',', '!', '?', ':', '(', ')', '*']
                for target in targets:
                    line = line.replace(target, '')
                # スペースで分割しリストを作成
                l = line.split(' ')
                # 単語を辞書へ登録・更新（インクリメント）
                for item in l:
                    if item != '':
                        if item in words:
                            words[item] += 1
                        else:
                            words[item] = 1
        # 辞書のitems()を、valueを基準（キー）としてソートする
        # - `key=lambda item: int(item[1])` は、valueを整数に変換してソートの基準に
        # - `reverse=True` で降順（多い順）にソート
        # - 各要素が「(key, value)のタプル」のリストが返される
        sorted_items = sorted(words.items(), key=lambda item: int(item[1]), reverse=True)
        # 上位PRINT_CNT件を表示
        for i in range(PRINT_CNT):
            print(f"{i + 1:2d}: {sorted_items[i][0]:15s} {sorted_items[i][1]:5d}")
    except FileNotFoundError:
        print(f"エラー: {name} が見つかりません。")

# メイン関数
def main():
    # args = ['', 'The Adventures of Sherlock Holmes.txt']
    args = sys.argv # リスト
    open_text_file(args[1])

if __name__ == "__main__":
    main()
