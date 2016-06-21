#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs


# 用户
# 含有用户微博总数、微博分词后结果、分词后统计结果
class user(object):
    def __init__(self, user_id=0):
        self.segment_result_set = {}
        self.segment_result_list = []
        self.comments_all = []
        self.user_id = user_id  # 字符串

    def set_comments_all(self):
        pass

    def set_segment_result_list(self, filename_segment=None):
        fp_weibo_comment = codecs.open(filename_segment, "r", "utf-8")
        list = fp_weibo_comment.readlines()
        if len(list) == 1:
            self.segment_result_list = list[0].split(' ')
        else:
            self.segment_result_list = []

    def set_result_set(self):
        if len(self.segment_result_list) > 0:
            for each in self.segment_result_list:
                if each not in self.segment_result_set:
                    self.segment_result_set[each] = 1
                else:
                    self.segment_result_set[each] += 1
        else:
            self.segment_result_set = {}
