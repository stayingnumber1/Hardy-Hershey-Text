# -*- coding: utf-8 -*-
# hershey font test

import hardyhersheydata


def test_eval():
    textFont = "music"
    font = eval('hardyhersheydata.' + textFont)
    print font


def test_ord():
    # unicode 基本拉丁字母共有126-32个 编码区间:
    # [0:31] : 操作系统特殊字符
    # [32:47]: 标点符号
    # [48:57]: 数字区
    # [58:64]: 标点符号
    # [65:90]: 拉丁字母大写
    # [91:96]: 标点符号
    # [97:122]: 拉丁字母小写
    # [123:126]: 标点符号

    # 这里hersheydata编码了94个常用的字符
    baseLatinValue = 32
    letter = 'a'
    letterVals = [ord(q) - 32 for q in unicode(letter, 'utf-8')]

    # 计算字符在unicode表中的实际顺序
    print  letterVals[0] + 32


if __name__ == '__main__':
    test_ord()
