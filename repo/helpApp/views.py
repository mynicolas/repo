#-*- coding: utf-8 -*-
from django.http import HttpResponse
from getHelp import Help

# 将post数据处理之后返回对应repo的help文档
def getHelpContent(request):
    if request.method == "POST":
        repoItem = request.POST.keys()[0]
        helpItem = Help(repoItem).getHelpItem()
        return HttpResponse(helpItem)
    else:
        return HttpResponse('Opps, no help document!')
