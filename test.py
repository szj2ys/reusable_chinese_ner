# *_*coding:utf-8 *_*
from __future__ import absolute_import, division, print_function
import re


def delete_tag(s):
    s = re.sub('\{IMG:.?.?.?\}', '', s)  # 图片
    s = re.sub(re.compile(r'[a-zA-Z]+://[^\s]+'), '', s)  # 网址
    s = re.sub(re.compile('<.*?>'), '', s)  # 网页标签
    s = re.sub(re.compile('&[a-zA-Z]+;?'), ' ', s)  # 网页标签
    s = re.sub(re.compile('[a-zA-Z0-9]*[./]+[a-zA-Z0-9./]+[a-zA-Z0-9./]*'),
               ' ', s)
    s = re.sub("\?{2,}", "", s)
    s = re.sub("\r", "", s)
    s = re.sub("\n", ",", s)
    s = re.sub("\t", ",", s)
    s = re.sub("（", ",", s)
    s = re.sub("）", ",", s)
    s = re.sub("\u3000", "", s)
    s = re.sub(" ", "", s)
    r4 = re.compile('\d{4}[-/]\d{2}[-/]\d{2}')  # 日期
    s = re.sub(r4, "", s)
    time = re.compile('\d{1,2}:\d{1,2}:\d{1,2}')  # 时间点，如12:24:34
    s = re.sub(time, "", s)
    time2 = re.compile('\d{1,2}:\d{1,2}')  # 时间点，如12:24
    s = re.sub(time, "", s)
    return s
