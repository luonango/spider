#!/usr/bin/python
# -*- coding: utf8 -*-

# 关键字写入封装成utl(微博搜索中的utl)
# http://s.weibo.com/weibo/...
def conver2url(args):
    url_suffix_ = ""
    if len(args) == 0:
        return "baby"

    print args
    for each in args:
        url_suffix_ += each
        url_suffix_ += "%20"
    url_suffix_ += "&Refer=STopic_box"
    return url_suffix_


# test
def test():
    a = ["baby", "奶粉"]
    b = conver2url(a)
    print b


# test()
