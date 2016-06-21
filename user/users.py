#!/usr/bin/python
# -*- coding: utf8 -*-

import user
import codecs
import os

default_set_ = {u"奶粉", u"baby", u"喂养", u"母乳", u"幼儿",}


def judge_last_num(user_dict_key=None, last_num_max=10, default_set=default_set_):
    if user_dict_key is None:
        return 0
    if len(user_dict_key) < 1:
        return 0
    if len(default_set) < 1:
        default_set = default_set_
    cnt = 0
    for each in user_dict_key:
        if each in default_set_:
            cnt += 1
            if cnt > last_num_max:
                return cnt
    return cnt


class users(object):
    def __init__(self):
        self.users_set = {}  # 所有用户 user_id: user
        self.users_weibo_dict = {}  # 全部分词后的 词语：数量
        self.users_list_num = []  # 全数字数组

    def set_users_set(self, rootdir="E:\\rthings\\code\\python\\weibo\\output\\jieba\\user"):
        for parent_, dirnames_, filenames_ in os.walk(rootdir):
            parent = parent_.decode('gbk').encode('utf-8')
        for filename_ in filenames_:  # 输出文件信息
            filename = filename_.decode('gbk').encode('utf-8')
            if filename.startswith("user_segment_user_weibo_"):
                user_id = filename[-10:-1]
                filenamefull = os.path.join(parent, filename)
                user_item = user.user(user_id=user_id)
                user_item.set_segment_result_list(filename_segment=filenamefull)
                user_item.set_result_set()
                self.users_set[user_id] = user_item

    def get_users_weibo_dict(self):
        if len(self.users_set) < 1:
            self.users_weibo_dict = {}
            return
        # 对于所有用户,查询所有的user 的set  将所有单词放入users的set内
        for user_id in self.users_set:
            user_item = self.users_set[user_id]

            for each in user_item.segment_result_set:

                # 判断是否在users的字典中，如果没有则增加该字典，有则数字相加。
                if each not in self.users_weibo_dict:
                    self.users_weibo_dict[each] = user_item.segment_result_set[each]
                else:
                    self.users_weibo_dict[each] += user_item.segment_result_set[each]

    # 精简总词语词典（数量不足max的删除）
    def set_users_weibo_dict_condense(self, count_max=10):
        if len(self.users_weibo_dict) < 1:
            return
        count_max = int(count_max)
        keys = self.users_weibo_dict.keys()
        for key in keys:
            if self.users_weibo_dict[key] < count_max:
                del (self.users_weibo_dict[key])

                # a={"a":1,"b":2,"aa":11,"bb":22,"aaa":111,"bbb":222,"aaaa":1111,"bbbb":2222,"aaaaa":11111,"bbbbb":22222,}
                #
                # def test():
                #     keys=a.keys()
                #     for k in keys:
                #         print a[k]
                #

    def set_users_list_num(self, last_num_max=10, default_set=default_set_):
        users_keys = self.users_set.keys()
        users_dict_keys = self.users_weibo_dict.keys()

        for user_id in users_keys:
            user_list_num = ''
            user_item = self.users_set[user_id]
            for dict_key in users_dict_keys:
                if dict_key in user_item.segment_result_set:
                    user_list_num += str(user_item.segment_result_set[dict_key]) + ','
                else:
                    user_list_num += '0,'

            # 判断是否为yes  （含有奶粉等为yes）
            last_num = judge_last_num(user_dict_key=user_item.segment_result_set.keys(), last_num_max=last_num_max,
                                      default_set=default_set)

            user_list_num += str(last_num) + '\n'  # 添加换行
            self.users_list_num.append(user_list_num)
            # print self.users_list_num

    def write_users_list_num2file(self, filename="E:\\rthings\\code\\python\\weibo\\output\\list_num"):
        file_name = filename + '\\list_num.html'
        print filename
        if len(self.users_list_num) < 1:
            return
        fp = codecs.open(file_name, "w", "utf-8")
        for eachline in self.users_list_num:
            fp.write(eachline)
        fp.close()


def test_users(rootdir='E:\\rthings\\code\\python\\weibo\\output\\jieba\\user',
               count_max=10, last_num_max=10, default_set=default_set_,
               filename="E:\\rthings\\code\\python\\weibo\\output\\list_num"):
    if len(rootdir) < 2:
        rootdir = 'E:\\rthings\\code\\python\\weibo\\output\\jieba\\user'
    if len(count_max) < 1:
        count_max = 10
    if len(last_num_max) < 1:
        last_num_max = 10
    if len(default_set) < 1:
        default_set = default_set_
    if len(filename) < 2:
        filename = 'E:\\rthings\\code\\python\\weibo\\output\\list_num'
    count_max = int(count_max)
    last_num_max = int(last_num_max)

    print "-----开始进行词语向量化-------"

    users_item = users()
    users_item.set_users_set(rootdir=rootdir)
    # print len(users_item.users_set)
    for each in users_item.users_set:
        user = users_item.users_set[each]
        # print user.segment_result_set
        # break

    users_item.get_users_weibo_dict()
    # print users_item.users_weibo_dict
    # print "--------——————————————————————————————————————————-"
    users_item.set_users_weibo_dict_condense(count_max=count_max)

    print "总维度为", str(len(users_item.users_weibo_dict) + 1)

    # print "--------——————————————————————————————————————————-"
    users_item.set_users_list_num(last_num_max=last_num_max, default_set=default_set)
    # print "--------——————————————————————————————————————————-"
    users_item.write_users_list_num2file(filename=filename)
    # print "--------——————————————————————————————————————————-"

# test_users()
