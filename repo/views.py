#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import os
import re

LogDir = '/var/www/html/repo/log'
LockDir = '/var/run/repo'

def repo_index(request):
    context = []                                    # 构建模板内容
    for repo in os.listdir(LogDir):                 # 获取logDir中的所有文件或目录,用于渲染首页
        logDictTmp = {}                                # 构建logDict临时字典变量

        logDictTmp['repo'] = repo                      # 将logDir中的目录或文件存入logDict字典

        f = LogDir + "/%s/%s_status.log" % (repo, repo)     # 构建logDir子路径
        output = os.popen('sed /^$/d %s | tail -n 1' % f)   # 修改logDir子文件的最后一行
        if os.path.isfile(LockDir + '/' + repo + '.lock'):  # 如果在lockDir目录中存在和以上做修改的log文件同名的lock文件
            startSync = output.read()                       # 读取被修改的log文件
            if not startSync:                               # 如果该log文件不为空
                logDictTmp['stopTime'] = '-'                   # 添加logDict的stopTime键值为‘-’
                logDictTmp['status'] = 'unknown'               # 添加logDict的status键值为‘unknown’
                context.append(logDictTmp)                     # 将logDict添加到模板内容中
                continue                                        # 不执行以下for循环并从for循环开始继续循环

            startTime = re.split(r' ', startSync)[0] + ' ' + re.split(r' ', startSync)[1]
            logDictTmp['stopTime'] = '-'           # 如果存在lock文件，则说明文件正在同步或使用
            logDictTmp['status'] = 'syncing'       # 设置文件的状态
            context.append(logDictTmp)
        else:                                               # 如果lockDir目录中不存在和log文件同名的lock文件
            stopSync = output.read()                        # 读取log文件
            if not stopSync:                                # 如果log文件不为空
                logDictTmp['stopTime'] = '-'                   # 设置logDict的stopTime键值为‘-’
                logDictTmp['status'] = 'unknown'               # 设置logDict的status键值为‘unknown'
                context.append(logDictTmp)                     # 模板内容添加logDict
                continue                                    # 不执行以下for循环并从for循环开始继续循环

            stopTime = re.split(r' ', stopSync)[0] + ' ' + re.split(r' ', stopSync)[1]
            logDictTmp['stopTime'] = stopTime

            if re.search(r'finished', stopSync):        # 在stopSync中查找finished
                logDictTmp['status'] = 'finished'       # 如果找到finished则将logDict键值设置为‘finished’
            else:
                logDictTmp['status'] = 'error'          # 如果没有找到finished则将logDict的键值设置为‘error’
            context.append(logDictTmp)

    return render_to_response('repo_index.html', {'contextlist': context})

