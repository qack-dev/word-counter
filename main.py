#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# テキストファイルを開く
def open_text_file(name):
    # 相対パスを付与
    fileName = os.path.join('text', name)
    try:
        # ファイルを開く
        with open(fileName, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"エラー: {name} が見つかりません。")

# メイン関数
def main():
    args = ['', 'The Adventures of Sherlock Holmes.txt']
    # args = sys.argv # リスト
    text = open_text_file(args[1])
    print(text)

if __name__ == "__main__":
    main()
