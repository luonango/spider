#!/usr/bin/env python
# -*- coding: utf-8 -*-


class FeatureWeiboItem(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        label: 标注信息（是否为相关，1 or 0）
        id：全局ID
        user_id：取第一个数字
        user_type: 会员 3；达人 2；普通用户 1
        is_retweet：是 2；否 1
        weibo_content：关键数量（母婴，奶粉等）
        pic_num：图片数量
        time：凌晨 0:00-5:59 1；上午6:00-11:59 2；下午12:00-17:59 3；晚上 18:00-23:59 4
        r_user_id：取第一个数字
        r_user_type：黄V 5；蓝V 4；会员 3；达人 2；普通用户 1  (被转发）

    """

    def __init__(self, weibo_line=None):
        """Inits FeatureWeiboItem with blah."""
        self.label = 0
        self.user_id = 0
        self.user_type = 0
        self.is_retweet = 0
        self.time = 0
        self.r_user_id = 0
        self.r_user_type = 0
        self.phone_name = 0

        self.mombaby = 0.1
        self.dried_milk = 0.1
        self.breast_milk = 0.1
        self.gbaby = 0.1
        self.bbaby = 0.1
        self.diaper = 0.1
        self.feeder = 0.1
        self.nipple = 0.1

    def getItemString(self):
        """Performs operation blah."""

        item_str = ''
        item_str += str(self.label) + "\t"
        item_str += str(self.user_id) + "\t"
        item_str += str(self.user_type) + "\t"
        item_str += str(self.is_retweet) + "\t"
        item_str += str(self.time) + "\t"
        item_str += str(self.r_user_id) + "\t"
        item_str += str(self.r_user_type) + "\t"
        item_str += str(self.phone_name) + "\t"
        item_str += str(self.mombaby) + "\t"
        item_str += str(self.dried_milk) + "\t"
        item_str += str(self.breast_milk) + "\t"
        item_str += str(self.gbaby) + "\t"
        item_str += str(self.bbaby) + "\t"
        item_str += str(self.diaper) + "\t"
        item_str += str(self.feeder) + "\t"
        item_str += str(self.nipple) + "\n"

        return item_str

    def set_feature_weibo_item(self, weibo_line_dict=None):
        """set_feature_weibo_item.
        通过传入包含FeatureWeiboItem的所有属性的字典，（重新）设置该类的属性

        Args:
            weibo_line_dict: 包含FeatureWeiboItem的所有属性的字典
                example：{'label':1,'id':0,'user_id':2,......} 共11个

        Returns:
            A number identify the statement. For example:

            0: success
            -1: weibo_line_dict is None
            -2: no such Key in weibo_line_dict. check it again

        Raises:
            Nothing.
        """
        if weibo_line_dict == None:
            print 'this Item init error'
            return -1
        try:
            self.label = weibo_line_dict['label']
            self.user_id = weibo_line_dict['user_id']
            self.user_type = weibo_line_dict['user_type']
            self.is_retweet = weibo_line_dict['is_retweet']
            self.time = weibo_line_dict['time']
            self.r_user_id = weibo_line_dict['r_user_id']
            self.r_user_type = weibo_line_dict['r_user_type']
            self.phone_name = weibo_line_dict['phone_name']

            self.mombaby = str(weibo_line_dict['mombaby'])
            self.dried_milk = weibo_line_dict['dried_milk']
            self.breast_milk = weibo_line_dict['breast_milk']
            self.gbaby = weibo_line_dict['gbaby']
            self.bbaby = weibo_line_dict['bbaby']
            self.diaper = weibo_line_dict['diaper']
            self.feeder = weibo_line_dict['feeder']
            self.nipple = weibo_line_dict['nipple']

        except KeyError as e:
            print "error htera"
            print e
            return -2
        return 0
