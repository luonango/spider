#!/usr/bin/python
# -*- coding: utf8 -*-
import jieba

file_name_jieba_dict = 'E:\\Downloads\\Edge\\movice\\weibo_freshdata.2016-05-01\\jieba_dict.txt'
jieba.load_userdict(file_name_jieba_dict)


# 对传入的列表（多条文本）["string", ...] 进行结巴分词
# 然后返回分词后的结果["string", ...]
def segmentation_jieba(args):
    # print "start segmentation_jieba..._____________ "
    result = []
    for each in args:
        # print "each :" + str(each)
        seg_list = list(jieba.cut(each, cut_all=True))  # 匹配所有词
        result.extend(segmentation_fresh(seg_list))
    # for each in result:
    #     pass
    #     # print each,
    # print ""
    # print "end segmentation_jieba...___________ "
    return result


# 对分词后的列表["string",...]进行清洗：
#   1. 去掉单字符
#
# 返回清洗后的列表["string","string",...]
def segmentation_fresh(args):
    # print "start segmentation_fresh...____ "
    result = []
    for each in args:
        if len(each) > 1:
            result.append(each)
    # print "end segmentation_fresh..._____ "
    return result


# 对传入的列表（多条文本）["string", ...] 进行结巴分词、清洗
# 然后返回结果["string", ...]
def segmentation(args):
    # print "start segmentation..._______________________"
    if len(args) == 0:
        return []
    result = segmentation_jieba(args)
    return result


# test
def test():
    args = ["小明硕士是宝贝男女宝宝毕业男宝女宝宝于中国科学院计算所，后在日本京都大学深造，计算机科学与工程学院", "宝宝开始吃奶粉了，又要上淘宝买奶粉了，母乳不够"]

    # args = ['我家的女宝宝要吃饭啦']
    result = segmentation(args)
    for each in result:
        print each,
    print ""
    print result


# test()
