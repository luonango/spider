#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from feature_weibo import FeatureWeiboItem


def add_label_0_to_file_from_file(
        filename_src="E:\\rthings\\code\\python\\weibo\\bigdata\\weibo_num",
        filename_des="E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num"):
    """add_label_0_to_file_from_file.

    爬取文件，设置标注（1是手动标注，0是需要标注的）
    即将文本文件中，每行的第一个，如果不是1而是ID，则添加标注1

    Args:
        filename_src: 需要添加标注的文件地址（绝对地址）.
        filename_des: 标注完后的输出文件的文件地址（绝对地址）.

    Returns:
        A number identify the statement. For example:

        0: success
        -1: filename didn't given or too short
        -2: no such file path (can't open it)
        -3: while writting or readding some error occur

    Raises:
        Nothing.
    """

    if len(filename_src) < 1 or len(filename_des) < 1:
        return -1
    cnt = 0
    while 1:
        filename_src_name = filename_src + str(cnt)
        filename_des_name = filename_des + str(cnt)
        try:
            fp_src = codecs.open(filename_src_name, "r", "utf-8")
            fp_des = codecs.open(filename_des_name, "w", "utf-8")
        except IOError as e:
            print e
            return -2
        cnt_tmp = 0
        try:
            while 1:
                try:
                    line = fp_src.readline()
                    if line == "" or len(line) < 1:
                        break
                    split_line_list = line.split('\t')
                    try:
                        num = int(split_line_list[0])
                        if num != 1:
                            cnt_tmp += 1
                            if cnt_tmp % 1000 == 0:
                                line = "0" + '\t' + line
                                fp_des.write(line)
                                cnt_tmp = 0
                        else:
                            fp_des.write(line)
                    except:
                        continue
                except IOError as e:
                    print e
        except IOError as e:
            print e
            return -3
        finally:
            fp_src.close()
            fp_des.close()
        cnt += 1
    return 0  # means succeed


def add_label_to_file(filename_src=None, filename_des=None):
    if filename_src is None or len(filename_src) < 1:
        filename_src = "E:\\rthings\\code\\python\\weibo\\bigdata\\weibo_num"
    if filename_des is None or len(filename_des) < 1:
        filename_des = "E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num"
    add_label_0_to_file_from_file(filename_src=filename_src, filename_des=filename_des)


weibo_line_dict_keys = ['label', 'user_id', 'user_type', 'is_retweet', 'time', 'r_user_id', 'r_user_type', 'phone_name',
                        'content']

weibo_line_dict_keys_word = ['mombaby', 'dried_milk', 'breast_milk', 'gbaby', 'bbaby', 'diaper', 'feeder', 'nipple', ]
weibo_line_dict_keys_word_set = {
    'mombaby': u"母婴", 'dried_milk': u'奶粉', 'breast_milk': u'母乳', 'gbaby': u'女宝', 'bbaby': u'男宝', 'diaper': u'尿布',
    'feeder': u'奶瓶', 'nipple': u'奶嘴'}


# feature 对应于readme文件中的位置。如user_id（处于第二）对应着reademe中的第六个（split）
# 最后一个是 pic_num，对于11，而再后面的是关键词，这些内容均在 11对应的weibo_content中判断出来，所以存一个就行
split_line_list_reflect = [0, 5, 8, 4, 17, 19, 21, 15, 10]


def get_weibo_line_dict_line(line_str=None, split_str='\t'):
    if line_str == None or len(line_str) < 2 or len(split_str) < 1:
        return -1  # line_str is None or too short , or split_str error
    split_line_list = []
    split_line_list = line_str.split(split_str)

    list_str_dict = {}

    for (key, each_split) in zip(weibo_line_dict_keys, split_line_list_reflect):
        list_str_dict[key] = split_line_list[each_split]
    try:
        # 处理里面的数据，使之变成数值,存放到dict_des中（尤其是picnum 9，即之后的关键词)
        #  user_id
        user_id = str(list_str_dict['user_id'])
        user_id = int(user_id[:1])
        list_str_dict['user_id'] = user_id

        # user_type
        user_type = list_str_dict['user_type']
        if user_type == u'会员':
            user_type = 3
        elif user_type == u'达人':
            user_type = 2
        else:
            user_type = 1
        list_str_dict['user_type'] = user_type

        # is_retweet:
        is_retweet = int(list_str_dict['is_retweet'])
        is_retweet += 1
        list_str_dict['is_retweet'] = is_retweet  # 是 2；否 1

        # time
        time_weibo = str(list_str_dict['time'])
        time_fragment = time_weibo.split(' ')[1]
        time_num = 4
        if time_fragment < "05:59:59":
            time_num = 1
        elif time_fragment < "11:59:59":
            time_num = 2
        elif time_fragment < "17:59:59":
            time_num = 3
        elif time_fragment < "23:59:59":
            time_num = 4
        list_str_dict['time'] = time_num

        # r_user_id：
        r_user_id = list_str_dict['r_user_id']
        if r_user_id is None or len(str(r_user_id)) < 2:
            list_str_dict['r_user_id'] = 0
        else:
            list_str_dict['r_user_id'] = int(str(r_user_id)[:1])

        # r_user_type
        r_user_type = list_str_dict['r_user_type']
        if len(r_user_type) < 1:
            r_user_type_num = 0
        elif r_user_type == u'黄V':
            r_user_type_num = 5
        elif r_user_type == u'蓝V':
            r_user_type_num = 4
        elif r_user_type == u'会员':
            r_user_type_num = 3
        elif r_user_type == u'达人':
            r_user_type_num = 2
        else:
            r_user_type_num = 1
        list_str_dict['r_user_type'] = r_user_type_num


        # phone_name
        phone_name = list_str_dict['phone_name']
        phone_name = phone_name.lower()
        if phone_name.find("iphone") > 0 or phone_name.find("ipad") > 0 or phone_name.find(u"苹果") > 0:
            phone_num = 1
        elif phone_name.find('huawei') > 0 or phone_name.find(u'华为') > 0 or phone_name.find(u'荣耀') > 0:
            phone_num = 2
        elif phone_name.find("samsung") > 0 or phone_name.find(u"三星") > 0:
            phone_num = 3
        elif phone_name.find("xiaomi") > 0 or phone_name.find(u"米") > 0:
            phone_num = 4
        elif phone_name.find("weibo") > 0:
            phone_num = 5
        elif phone_name.find("oppo") > 0:
            phone_num = 6
        elif phone_name.find("vivo") > 0:
            phone_num = 7
        elif phone_name.find("meizu") > 0 or phone_name.find(u"魅族") > 0:
            phone_num = 8
        else:
            phone_num = 9
        list_str_dict['phone_name'] = phone_num

        content_str = list_str_dict['content']
        # 先分词
        # 整合
        # 然后判断是否含有那些东西
        from utils.jieba_tools import segmentation
        args = []
        args.append(content_str)
        result = segmentation(args)
        # 查找所有
        # weibo_line_dict_keys_word = ['mombaby', 'dried_milk', 'breast_milk', 'gbaby', 'bbaby', 'diaper', 'feeder', 'nipple', ]
        for key_word in weibo_line_dict_keys_word:
            count = 0.1 + result.count(weibo_line_dict_keys_word_set[key_word])
            list_str_dict[key_word] = count

        del list_str_dict['content']

        return list_str_dict
    except Exception as e:
        print e
    return -1


def read_file_2_vetor_file(
        filename_src="E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num",
        filename_des="E:\\rthings\\code\\python\\weibo\\bigdata\\vector\\vector.html"):
    """read_file_2_vetor_file.


    Args:
        filename_src: 需要添加标注的文件地址（绝对地址）.
        filename_des: 标注完后的输出文件的文件地址（绝对地址）.

    Returns:
        A number identify the statement. For example:

        0: success
        -1: filename didn't given or too short
        -2: no such file path (can't open it)
        -3: while writting or readding some error occur

    Raises:
        Nothing.
    """

    if len(filename_src) < 1 or len(filename_des) < 1:
        return -1

    try:
        fp_des = codecs.open(filename_des, "w", "utf-8")
    except Exception as e:
        print e
        return
    cnt = 0
    while 1:
        filename_src_name = filename_src + str(cnt)
        try:
            fp_src = codecs.open(filename_src_name, "r", "utf-8")
        except IOError as e:
            print e
            return -2
        try:
            while 1:
                try:
                    line = fp_src.readline()
                    if line == "" or len(line) < 1:
                        break
                    try:
                        result_dict = get_weibo_line_dict_line(line_str=line, split_str='\t')
                        feature_item = FeatureWeiboItem()
                    except Exception as e:
                        print e
                        continue
                    try:
                        feature_item.set_feature_weibo_item(weibo_line_dict=result_dict)
                    except Exception as e:
                        print e
                        continue
                    line_str = feature_item.getItemString()
                    fp_des.write(line_str)
                except IOError as e:
                    print e
                    continue
        except IOError as e:
            print e
            return -3
        finally:
            fp_src.close()
        cnt += 1
    fp_des.close()
    return 0  # means succeed


def condense_200(
        filename="E:\\Downloads\\Edge\\movice\\weibo_freshdata.2016-05-01\\test_weibo_num.html",
        filename_out="E:\\Downloads\\Edge\\movice\\weibo_freshdata.2016-05-01\\condense_data_weibo.html"):
    cnt = 1
    fp = codecs.open(filename, "r", "utf-8")
    fp_out = codecs.open(filename_out, "w", "utf-8")
    try:
        while 1:
            try:
                line = fp.readline()
                if line == "" or len(line) < 1:
                    break
                line_list = line.split('\t')
                if int(line_list[0]) == 0:
                    cnt += 1
                    if cnt % 200 == 0:
                        fp_out.write(line)
                    continue
                fp_out.write(line)
            except Exception:
                print "error in write"
    except Exception:
        print "error while"
    finally:
        fp.close()
        fp_out.close()

    print "success!...."


def condense(
        filename="E:\\Downloads\\Edge\\movice\\weibo_freshdata.2016-05-01\\test_weibo_num",
        filename_out="E:\\Downloads\\Edge\\movice\\weibo_freshdata.2016-05-01\\weibo_num"):
    cnt = 1
    cnt_name = 2

    line_pre = ""
    try:
        while 1:
            filename_out_name = filename_out + str(cnt_name)
            filename_name = filename + str(cnt_name)
            fp = codecs.open(filename_name, "r", "utf-8")
            fp_out = codecs.open(filename_out_name, "w", "utf-8")
            while 1:
                try:
                    line = fp.readline()
                    if line == "" or len(line) < 1:
                        break
                    line_list = line.split('\t')
                    print line_list[9]
                    if cnt != 1:
                        if line_list[9] == line_pre:
                            continue
                    else:
                        cnt += 1
                        line_pre = line_list[9]
                    fp_out.write(line)
                except Exception:
                    print "error in write"
            cnt_name += 1
            if cnt_name > 9:
                break
    except Exception:
        print "error while"
    finally:
        fp.close()
        fp_out.close()

    print "success!...."


def data_to_vector(filename_src=None, filename_des=None):
    if filename_src is None or len(filename_src) < 1:
        filename_src = "E:\\rthings\\code\\python\\weibo\\bigdata\\label\\label_weibo_num"
    if filename_des is None or len(filename_des) < 1:
        filename_des = "E:\\rthings\\code\\python\\weibo\\bigdata\\vector\\vector.html"
    read_file_2_vetor_file(filename_src=filename_src, filename_des=filename_des)


def test():
    pass
    # add_label_0_to_file_from_file()
    # read_file_2_vetor_file(
    #     filename_src="E:\\Downloads\\Edge\\Tencent\\FileRecv\\label_200_condense_weibo_freshdata.2016-05-01.txt")
    # test()
