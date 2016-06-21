#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import codecs
import parser_nango
from utils.jieba_tools import *


# 循环读取本地html文件，解析里面的微博
def getweibo_from_file():
    file_max_size = 4 * 1000  # 一个文件最大4K
    rootdir = "E:\\rthings\\code\\python\\weibo\\weibo_parser_hot"
    split_left = '<!--\u7528\u5fae\u535a\u521b\u5efa\u65f6\u95f4\u5224\u65ad\u5fae\u535a\u662f\u5426\u88ab\u5220\u9664-->'
    split_right = split_left
    soup_find_attr = ['p', 'comment_txt']

    filename_output_file_pre = "E:\\rthings\\code\\python\\weibo\\output\\weibo_hot"
    filename_output_file_cnt = 1

    for parent_, dirnames_, filenames_ in os.walk(rootdir):
        parent = parent_.decode('gbk').encode('utf-8')
        for dirname_ in dirnames_:  # 输出文件夹信息
            dirname = dirname_.decode('gbk').encode('utf-8')
            dirnamefull = os.path.join(parent, dirname)
            # print dirnamefull
            # print "dirname is: " + dirname

        for filename_ in filenames_:  # 输出文件信息
            # print "parent is：" + parent
            filename = filename_.decode('gbk').encode('utf-8')
            # print "filename is:" + filename
            # print "the full name of the file is:" +
            filenamefull = os.path.join(parent, filename)
            # print filenamefull


            # 寻找后缀为html的即为所求
            if filenamefull.endswith(".htm"):
                # 如果文件存在且小于4k，写入；否则创建新文件写入
                # 如果文件存在但不是file，则换
                # 如果文件不存在，创建并写入
                while 1:
                    filename_output_file_filename = filename_output_file_pre + str(filename_output_file_cnt)
                    # filename_output_file_filename_ = filename_output_file_filename.decode('utf-8').encode('gbk')
                    if os.path.exists(filename_output_file_filename):
                        if os.path.isfile(filename_output_file_filename) and (
                                    os.path.getsize(filename_output_file_filename) < file_max_size):
                            print "write into ", filename_output_file_filename
                            parser_nango.weibo_parser_hot_url_filename(1, filenamefull, split_left, split_right,
                                                                       soup_find_attr,
                                                                       filename_output_file_filename)
                            break
                        else:
                            filename_output_file_cnt = filename_output_file_cnt + 1
                    else:
                        print "create file ", filename_output_file_filename
                        f_test = codecs.open(filename_output_file_filename, "w", "utf-8")
                        f_test.close()


# getweibo_from_file()


def getweibo_segment_from_file():
    file_max_size = 32 * 1000  # 一个文件最大32K
    rootdir = "E:\\rthings\\code\\python\\weibo\\output"

    filename_output_file_pre = "E:\\rthings\\code\\python\\weibo\\output\\jieba\\weibo_segment_hot"
    filename_output_file_cnt = 1
    print
    for parent_, dirnames_, filenames_ in os.walk(rootdir):
        parent = parent_.decode('gbk').encode('utf-8')
        for dirname_ in dirnames_:  # 输出文件夹信息
            dirname = dirname_.decode('gbk').encode('utf-8')
            dirnamefull = os.path.join(parent, dirname)
            # print dirnamefull
            # print "dirname is: " + dirname

        for filename_ in filenames_:  # 输出文件信息
            # print "parent is：" + parent
            filename = filename_.decode('gbk').encode('utf-8')
            # print "filename is:" + filename
            # print "the full name of the file is:" +
            filenamefull = os.path.join(parent, filename)
            # print filenamefull


            # 寻找前缀是weibo_hot的文件
            if filename.startswith("weibo_hot"):
                # 读取weibo_hot文件，然后写入semgment文件
                # 如果semgment文件存在且小于4k，写入；否则创建新文件写入
                # 如果semgment文件存在但不是file，则换
                # 如果semgment文件不存在，创建并写入

                fp_weibo_comment = codecs.open(filenamefull, "r", "utf-8")

                segment_all = []
                while 1:
                    lines = fp_weibo_comment.readlines(32 * 1000)
                    if not lines:
                        break
                    for line_ in lines:
                        line = line_.decode("utf-8")
                        segment_all.append(line)
                        # print line

                print len(segment_all)
                fp_weibo_comment.close()
                result = segmentation(segment_all)

                # for each in result:
                #     print each,
                while 1:
                    filename_output_file_filename = filename_output_file_pre + str(filename_output_file_cnt)
                    # filename_output_file_filename_ = filename_output_file_filename.decode('utf-8').encode('gbk')
                    if os.path.exists(filename_output_file_filename):
                        if os.path.isfile(filename_output_file_filename) and (
                                    os.path.getsize(filename_output_file_filename) < file_max_size):
                            print "write into ", filename_output_file_filename
                            fp_raw_hot = codecs.open(filename_output_file_filename, "a", "utf-8")
                            result_txt = ""
                            for each_ in result:
                                each = each_.encode("utf-8")
                                result_txt = result_txt + each + " "
                            print result_txt
                            fp_raw_hot.write(result_txt)
                            fp_raw_hot.close()
                            break
                        else:
                            filename_output_file_cnt = filename_output_file_cnt + 1
                    else:
                        print "create file ", filename_output_file_filename
                        f_test = codecs.open(filename_output_file_filename, "w", "utf-8")
                        f_test.close()


def get_users_weibo_segment_from_file(rootdir="E:\\rthings\\code\\python\\weibo\\output\\user",
                                      filename_output_file_pre="E:\\rthings\\code\\python\\weibo\\output\\jieba\\user"):
    filename_output_file_pre += '\\user_segment_'

    file_max_size = 32 * 1000  # 一个文件最大32K
    filename_output_file_cnt = 1
    print
    for parent_, dirnames_, filenames_ in os.walk(rootdir):
        parent = parent_.decode('gbk').encode('utf-8')
        # for dirname_ in dirnames_:  # 输出文件夹信息
        #     dirname = dirname_.decode('gbk').encode('utf-8')
        #     dirnamefull = os.path.join(parent, dirname)
        #     # print dirnamefull
        #     # print "dirname is: " + dirname

        for filename_ in filenames_:  # 输出文件信息
            # print "parent is：" + parent
            filename = filename_.decode('gbk').encode('utf-8')
            # print "filename is:" + filename
            # print "the full name of the file is:" +
            filenamefull = os.path.join(parent, filename)
            # print filenamefull


            if filename.startswith("user_weibo_"):

                fp_weibo_comment = codecs.open(filenamefull, "r", "utf-8")

                segment_all = fp_weibo_comment.readlines()
                # while 1:
                #     lines = fp_weibo_comment.readlines(1 * 1000)
                #     if not lines:
                #         break
                #     for line_ in lines:
                #         segment_all.append(line_)

                print len(segment_all)
                fp_weibo_comment.close()

                result = segmentation(segment_all)
                # for each in result:
                #     print each,
                filename_output_file_filename = filename_output_file_pre + filename
                # filename_output_file_filename_ = filename_output_file_filename.decode('utf-8').encode('gbk')
                if not os.path.exists(filename_output_file_filename):
                    print "create file ", filename_output_file_filename
                    f_test = codecs.open(filename_output_file_filename, "w", "utf-8")
                    f_test.close()  # getweibo_segment_from_file()

                if os.path.isfile(filename_output_file_filename) and (
                            os.path.getsize(filename_output_file_filename) < file_max_size):
                    # print "write into ", filename_output_file_filename
                    fp_raw_hot = codecs.open(filename_output_file_filename, "a", "utf-8")
                    result_txt = ""
                    for each_ in result:
                        each = each_  # .encode("utf-8")
                        result_txt = result_txt + each + " "
                    # print result_txt
                    fp_raw_hot.write(result_txt)
                    fp_raw_hot.close()


def call_weibo_segment(rootdir="E:\\rthings\\code\\python\\weibo\\output\\user",
                       filename_output_file_pre="E:\\rthings\\code\\python\\weibo\\output\\jieba\\user"):
    rootdir = rootdir.strip()
    filename_output_file_pre = filename_output_file_pre.strip()
    if len(rootdir) < 2:
        rootdir = "E:\\rthings\\code\\python\\weibo\\output\\user"
    if len(filename_output_file_pre) < 2:
        filename_output_file_pre = "E:\\rthings\\code\\python\\weibo\\output\\jieba\\user"

    get_users_weibo_segment_from_file(rootdir=rootdir, filename_output_file_pre=filename_output_file_pre)
