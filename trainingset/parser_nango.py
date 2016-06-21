#!/usr/bin/python
# -*- coding: utf8 -*-
from lxml import etree
import httplib2
import urllib2
from bs4 import BeautifulSoup
import os
import codecs
import time


# flag  0:url   1: filename
# url_filename是访问链接或者html文件绝对路径
# split_left  split_right ：是因为获取的微博正文在script里面，要将其匹配出来，需要前后字符串匹配出来
# soup_find_attr：BeautifulSoup中的find_all的参数，目前只有两个 soup_find_attr[0]='p',soup_find_attr='class_name'
# filename_output 将微博comment写入的文件夹路径
def weibo_parser_hot_url_filename(flag, url_filename, split_left, split_right, soup_find_attr, filename_output):
    content = getHTMLContent(flag, url_filename)

    # 寻找到相应内容
    bpos = content.find(split_left)
    epos = content.rfind(split_right)
    html = content[bpos:epos].replace('\\/', '/')
    html = html.replace('\\n', '\n')
    html = html.replace('\\t', '\t')
    html = html.replace('\\"', '\"')

    soup = BeautifulSoup(html, "lxml")
    blogsouplist = soup.find_all(soup_find_attr[0], class_=soup_find_attr[1])
    fp_raw_hot = codecs.open(filename_output, "a", "utf-8")

    hot_comment = []
    for blogsoup in blogsouplist:
        commment_txt = blogsoup.text
        commment_txt = commment_txt.decode("unicode-escape")
        commment_txt = commment_txt.encode("utf-8")
        commment_txt = commment_txt.strip(' \t\n\r')
        hot_comment.append(commment_txt)
    for each in hot_comment:
        fp_raw_hot.write(each + "\r\n")
    fp_raw_hot.close()


def getHTMLContent(flag, url_filename):
    if flag == 0:
        http = httplib2.Http()
        request = urllib2.Request(url_filename)
        response = urllib2.urlopen(request)
        content = response.read()
        return content
    else:
        fp_raw = codecs.open(url_filename, "r", "utf-8")
        content = fp_raw.read()
        fp_raw.close()
        return content


# flag  0:url   1: filename
# url_filename是访问链接或者html文件绝对路径
# split_left  split_right ：是因为获取的微博正文在script里面，要将其匹配出来，需要前后字符串匹配出来
# soup_find_attr：BeautifulSoup中的find_all的参数，目前只有两个 soup_find_attr[0]='p',soup_find_attr='class_name'
# filename_output 将微博comment写入的文件夹路径
def weibo_parser_user_url_filename(flag, url_filename, split_left, split_right, soup_find_attr, filename_output):
    content = getHTMLContent(flag, url_filename)
    print "content-length", len(content)
    # fp_raw = open("E://rthings//code//python//weibo//others//weibo_parser_hot//content_user2.html", "w+")
    # fp_raw.write(content)
    # fp_raw.close()
    if len(content) < 100 * 1000:
        return

        # 寻找到相应内容
    bpos = content.find(split_left)
    epos = content.rfind(split_right)
    html = content[bpos:epos].replace('\\/', '/')
    html = html.replace('\\n', '\n')
    html = html.replace('\\t', '\t')
    html = html.replace('\\"', '\"')

    soup = BeautifulSoup(html, "lxml")
    blogsouplist = soup.find_all(soup_find_attr[0], class_=soup_find_attr[1])
    if not os.path.exists(filename_output):
        print "create file ", filename_output
        f_test = codecs.open(filename_output, "w", "utf-8")
        f_test.close()
    fp_raw_hot = codecs.open(filename_output, "a", "utf-8")

    hot_comment = []
    for blogsoup in blogsouplist:
        commment_txt = blogsoup.text
        # commment_txt = commment_txt.decode("unicode-escape")
        # commment_txt = commment_txt.encode("utf-8")
        commment_txt = commment_txt.strip(' \t\n\r')
        hot_comment.append(commment_txt)
    for each in hot_comment:
        fp_raw_hot.write(each + "\r\n")
    fp_raw_hot.close()


def test():
    http = httplib2.Http()
    response, content = http.request("http://weibo.com/u/1195622065?refer_flag=1001030103_", "GET")
    # tree = etree.HTML(content)
    # data = tree.xpath(u'/html/body/div/div/div[1]/div/div[2]/ul')  # /html/body/div/div/div[1]/div/div[2]/ul/li[1]/a
    # print len(data)
    fp_raw = codecs.open("E:\\rthings\\code\\python\\aaaa.htm", "w")
    fp_raw.write(content)
    fp_raw.close()


def test3():
    filename_output_file_filename = "E://rthings//code//python//weibo//others//weibo_parser_hot//content_user_out.txt"
    url_test = "http://weibo.com/u/5939923303"
    split_left = '''<div class=\\"WB_feed WB_feed_v3\\" pageNum=\\"\\" node-type='feed_list' module-type=\\"feed\\">'''
    split_right = '''<div class=\\"WB_cardwrap S_bg2\\" node-type=\"lazyload\\">'''
    soup_find_attr = ['div', 'WB_text W_f14']
    weibo_parser_user_url_filename(0, url_test, split_left, split_right, soup_find_attr, filename_output_file_filename)


# 爬取n个用户的微博！
def weibo_parser_users(user_start=3871455746, user_totals=1000,
                       file_dirt_pre='E:\\rthings\\code\\python\\weibo\\output\\user'):
    split_left = '''<div class=\\"WB_feed WB_feed_v3\\" pageNum=\\"\\" node-type='feed_list' module-type=\\"feed\\">'''
    split_right = '''<div class=\\"WB_cardwrap S_bg2\\" node-type=\"lazyload\\">'''
    soup_find_attr = ['div', 'WB_text W_f14']
    filename_output_file_pre = file_dirt_pre + "\\user_weibo_"
    url_head = 'http://weibo.com/u/'
    user_totals = int(user_totals)
    user_start = int(user_start)
    cnt = user_start
    while cnt < user_totals + user_start:
        url_user = url_head + str(cnt)
        filename_output_file_filename = filename_output_file_pre + str(cnt)

        print "ready to load url:", url_user
        try:
            weibo_parser_user_url_filename(0, url_user, split_left, split_right, soup_find_attr,
                                           filename_output_file_filename)
        except Exception:
            time.sleep(3)
        finally:
            cnt = cnt + 1;


def call_weibo_parser(user_start=3871455746, user_totals=5,
                      file_dirt_pre='E:\\rthings\\code\\python\\weibo\\output\\user'):  # 3871455745

    file_dirt_pre = file_dirt_pre.strip()
    if len(file_dirt_pre) < 2:
        file_dirt_pre = 'E:\\rthings\\code\\python\\weibo\\output\\user'
    if int(user_start) < 1000000000:
        user_start = 3871455746
    if int(user_totals) < 1:
        user_totals = 5
    weibo_parser_users(user_start=user_start, user_totals=user_totals, file_dirt_pre=file_dirt_pre)
