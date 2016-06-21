#!/usr/bin/env python
# -*- coding: utf-8 -*-
def weibo_login():
    from utils.weibo_login import weiboLogin
    wblogin = weiboLogin()
    print '新浪微博模拟登陆:'
    username = raw_input(u'用户名：')
    password = raw_input(u'密码：')
    # username = "@qq.com"
    # password = "l770160905"
    return wblogin.login(username, password)


def test():
    print "-----------test--------------"
    # url = 'http://s.weibo.com/weibo/幼儿&Refer=STopic_box'
    # split_left = '<!--\u7528\u5fae\u535a\u521b\u5efa\u65f6\u95f4\u5224\u65ad\u5fae\u535a\u662f\u5426\u88ab\u5220\u9664-->'
    # cnt = 1
    # filename_output = "E://rthings//code//python//weibo_parser_hot//hot" + str(cnt) + ".txt"
    #
    # trainingset.parser.weibo_parser_hot_url_filename(0, url, split_left, split_left, ['p', 'comment_txt'],
    #                                                  filename_output)
    # start_id = 3871455744  # 1686579080  # 3871483428  # 3871457621

    # trainingset.parser_nango.test4(user_start=start_id)


    # import trainingset.pre_data_url_file
    # trainingset.pre_data_url_file.test4()


def test_trainingset():
    import trainingset.pre_data_url_file
    trainingset.pre_data_url_file.test5()


# 1.爬取微博页面
def loop_op1():
    # 先登录才能爬取
    if weibo_login() == 0:
        return 0
    # 进行网页爬取。先传入爬取首id
    start_id = int(raw_input(u'起始爬取id (如: 3871455746 )：'))
    range_id = int(raw_input(u'遍历的ID数目 (如: 100 )：'))
    file_dirt_pre = raw_input(u'数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\user)：')
    from trainingset.parser_nango import call_weibo_parser
    call_weibo_parser(user_start=start_id, user_totals=range_id,
                      file_dirt_pre=file_dirt_pre)
    print "爬取完毕"
    return 1


#
# # 2.将微博分词分析
# def loop_op2():
#     from trainingset.pre_data_url_file import call_weibo_segment
#     rootdir = raw_input(u'源数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\user)：')
#     output_file = raw_input(u'目标数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\jieba\\user)：')
#     call_weibo_segment(rootdir=rootdir, filename_output_file_pre=output_file)
#     print "分词完毕"


# 2.数据向量化
def loop_op2():
    output_hint_2 = u'''
命令：输入向量化的方法:
        1. 通过每条微博进行向量化
        2. 通过每个用户微博进行向量化
        3. 退出
    '''

    while 1:
        print output_hint_2
        op = raw_input(u'输入指令：(如 1) ')
        op=str(op)
        if len(op) < 1:
            continue
        if op == '2':
            # 先分词
            op2 = raw_input(u'需要进行分词吗？（yes no）：(如 yes)')
            if op2 == 'yes':
                from trainingset.pre_data_url_file import call_weibo_segment
                rootdir = raw_input(u'源数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\user)：')
                output_file = raw_input(u'目标数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\jieba\\user)：')
                call_weibo_segment(rootdir=rootdir, filename_output_file_pre=output_file)
                print "分词完毕"

            from user.users import test_users

            rootdir = raw_input(u'源数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\user)：')
            count_max = raw_input(u'清洗数据，去掉出现次数少的词汇，count_max为： (如: 10 )：')
            last_num_max = raw_input(u'预测结果的数字范围为0-x，x为： (如: 10 )：')
            filename = raw_input(u'词汇向量化输出的存放位置 (如: E:\\rthings\\code\\python\\weibo\\output\\list_num)：')

            test_users(rootdir=rootdir, count_max=count_max, last_num_max=last_num_max, filename=filename)

            print "数据向量化完毕"
            break
        elif op == '1':
            # add label to file
            while 1:
                op3 = raw_input(u'对文件添加0标注？（yes no）：(如 yes)')
                if op3 == 'yes':
                    from weibo_data.condense import add_label_to_file
                    filename_src = raw_input(
                        u'源数据存放位置 (如: "E:\\rthings\\code\\python\\weibo\\bigdata\\weibo_num")：')
                    filename_des = raw_input(
                        u'目标数据存放位置 (如: "E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num")：')
                    add_label_to_file(filename_src=filename_src, filename_des=filename_des)
                    break
                if op3 == 'no':
                    break
            while 1:
                op4 = raw_input(u'进行数据向量化？（yes no）：(如 yes)')
                if op4 == 'yes':
                    print ''' 开始进行数据向量化...'''
                    from weibo_data.condense import data_to_vector
                    filename_src = raw_input(
                        u'源数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num)：')
                    filename_des = raw_input(
                        u'目标数据存放位置 (如: E:\\rthings\\code\\python\\weibo\\bigdata\\vector\\vector.html)：')
                    data_to_vector(filename_src=filename_src, filename_des=filename_des)
                    break
                elif op4 == 'no':
                    break
        else:
            break


# 3.数据挖掘分析

def loop_op3():  # file:///E:/rthings/code/python/weibo/output/list_num/list_num.html
    from trainingset.data_analysis import analysis_pre, analysis_method
    url = raw_input(u'源向量存放url位置 (如: file:///E:/rthings/code/python/weibo/bigdata/vector/vector.html)：')
    dimension_num = raw_input(u'总维度： (如: 16 )：')
    if len(url) < 1:
        url = 'file:///E:/rthings/code/python/weibo/bigdata/vector/vector.html'
    if len(dimension_num) < 1:  # 349
        dimension_num = 16
    X, y = analysis_pre(url=str(url), dimension_num=int(dimension_num))
    output_method = u'''
命令：输入机器学习算法类型:
    svm   beyes  cart  knn
    quit (表示退出当前）
    '''
    while 1:
        print output_method
        method_str = raw_input(u'输入： (如: svm )：')
        if len(method_str) < 1:
            method_str = 'svm'
        if method_str == 'quit':
            break
        analysis_method(method=str(method_str), X=X, y=y)
    print "数据向量化完毕"


def loop_main():
    output_hint_main = '''
指令选项:
    1.爬取微博页面
    2.数据向量化
    3.数据挖掘分析
    4.退出
    '''

    while 1:
        print output_hint_main

        op = raw_input(u'输入指令：')
        if len(op) < 1:
            continue
        op = int(op)

        if op == 1:
            loop_op1()
            continue
        if op == 2:
            loop_op2()
            continue
        if op == 3:
            loop_op3()
            continue

        if op == 4:
            print"--------------------\n欢迎再次使用！ 再见\n--------------------"
            return 0


if __name__ == "__main__":
    loop_main()
