# _*_ coding: utf-8 _/*_
import datetime
import string
from zhon.hanzi import punctuation


def filter_punctuations(text):
    for i in string.punctuation:
        text = text.replace(i, "")
    for i in punctuation:
        text = text.replace(i, "")
    return text
