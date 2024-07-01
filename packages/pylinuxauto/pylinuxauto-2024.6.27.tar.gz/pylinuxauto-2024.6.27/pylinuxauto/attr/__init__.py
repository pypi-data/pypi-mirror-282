#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from funnylog import logger
from youqu_dogtail.install_depends import install_depends

# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
# pylint: disable=C0114,C0103

install_depends()

from youqu_dogtail.dogtail.tree import SearchError
from youqu_dogtail.dogtail.tree import root
from youqu_dogtail.dogtail.tree import config
from youqu_dogtail.dogtail.tree import Node

config.childrenLimit = 10000
# config.logDebugToStdOut = False
config.logDebugToFile = False
config.searchCutoffCount = 2


class ElementNotFound(Exception):
    """未找到元素"""

    def __init__(self, name):
        """
        未找到元素
        :param name: 命令
        """
        err = f"====未找到“{name}”元素！===="
        logger.error(err)
        Exception.__init__(self, err)


class ApplicationStartError(Exception):
    """
    应用程序未启动
    """

    def __init__(self, result):
        """
        应用程序未启动
        :param result: 结果
        """
        err = f"应用程序未启动,{result}"
        logger.error(err)
        Exception.__init__(self, err)


class Attr():
    __author__ = "mikigo<huangmingqiang@uniontech.com>"

    def __init__(self, appname=None):
        config.logDebugToStdOut = False
        self.appname = appname
        if appname:
            self.obj = root.application(self.appname)
        else:
            self.obj = root

    def find_element_by_attr_name(
            self,
            name='',
            roleName='',
            description='',
            label='',
            recursive=True,
            retry=False,
            debugName=None,
            showingOnly=None
    ) -> Node:
        try:
            logger.debug(f"获取元素对象f【{name}】")
            element = self.obj.child(
                name=name,
                roleName=roleName,
                description=description,
                label=label,
                recursive=recursive,
                retry=retry,
                debugName=debugName,
                showingOnly=showingOnly
            )
            return element
        except SearchError:
            raise ElementNotFound(name) from SearchError


if __name__ == '__main__':
    dog = Attr().find_element_by_attr_name("Btn_文件管理器").click()
