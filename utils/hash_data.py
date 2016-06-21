#!/usr/bin/python
# -*- coding: utf8 -*-

import codecs
import os
import os.path


def qselect(A, k):
    print A
    if len(A) < k:
        return A
    pivot = A[-1]
    right = [pivot] + [x for x in A[:-1] if x[1] >= pivot[1]]
    rlen = len(right)
    print pivot, right, rlen
    if rlen == k:
        return right
    if rlen > k:
        return qselect(right, k)
    else:
        left = [x for x in A[:-1] if x[1] < pivot[1]]
        return qselect(left, k - rlen) + right


class hash_data(object):
    def __init__(self, topK_max=10):

        self.data_set = {}
        self.topK = []
        self.topK_max = topK_max

    def append(self, word=None, cnt=None):
        if cnt is None:
            if word not in self.data_set:
                self.data_set[word] = 1
            else:
                self.data_set[word] += 1
        else:
            cnt = int(cnt)
            if cnt > 0:
                self.data_set[word] = cnt
            else:
                self.data_set[word] = 0

    def writeall(self, filename):
        fp_w = codecs.open(filename, "w+", 'utf-8')
        each_line = ""
        for each in self.data_set:
            if len(each_line) > 4 * 1000:
                fp_w.write(each_line)
                each_line = ""
            each_line += each
            each_line += " "
            each_line += str(self.data_set[each])
            each_line += " "
            each_line += "\r\n"
        fp_w.write(each_line)
        fp_w.close()

    def readall(self, filename):
        fp_r = codecs.open(filename, "r", 'utf-8')
        while 1:
            lines = fp_r.readlines(128 * 1000)
            if not lines:
                break
            for line_ in lines:
                line = line_
                print line
                line_split = line.split(' ')
                self.append(word=line_split[0], cnt=line_split[1])

    def readfromfileofdata2hash(self, rootdir, file_l=None):
        for parent_, dirnames_, filenames_ in os.walk(rootdir):
            parent = parent_.decode('gbk').encode('utf-8')
            # for dirname_ in dirnames_:  # 输出文件夹信息
            #     dirname = dirname_.decode('gbk').encode('utf-8')
            #     dirnamefull = os.path.join(parent, dirname)
            for filename_ in filenames_:  # 输出文件信息
                filename = filename_.decode('gbk').encode('utf-8')
                filenamefull = os.path.join(parent, filename)
                print filenamefull, "+++++++++"
                if file_l is not None:
                    if filename.startswith(file_l):
                        fpr_data = codecs.open(filenamefull, "r", "utf-8")
                        while 1:
                            lines = fpr_data.readlines(32 * 1000)
                            if not lines:
                                break
                            print lines, "_______lines"
                            for line in lines:
                                line_split = line.split(' ')
                                for each in line_split:
                                    self.append(word=each)

    def gettopK(self):
        items = []
        topK_tmp = []
        for each in self.data_set:
            item = []
            item.append(each)
            item.append(self.data_set[each])
            items.append(item)
            if len(items) > 4 * 1000:
                topK_tmp.extend(qselect(items, self.topK_max))
                items = []
        self.topK = qselect(items, self.topK_max)

#
# dataset = hash_data()
# dataset.readfromfileofdata2hash(rootdir="E:\\rthings\\code\\python\\weibo\\output\\jieba", file_l="weibo_segment_hot")
#
# print "------------------"
# print dataset.data_set
# print "------------------"
# dataset.data_set
#
# print "------------------"
#
# dataset.writeall(filename="E:\\rthings\\code\\python\\weibo\\hashdata\\wwwhash_data1.txt")
# dataset.gettopK()
# dataset.topK
# print dataset.topK
# for each in dataset.topK:
#     print each[0], ": ", each[1]

#
# print dataset.data_set[u'\u6838\u529b\u91cf']
# dataset.data_set[u'\u91cf'] = 19
# dataset.data_set[u'\u6838'] = 18
#
# dataset.writeall("E:\\rthings\\code\\python\\weibo\\hashdata\\whash_data1.txt")
# print "______________"
# print dataset.data_set
