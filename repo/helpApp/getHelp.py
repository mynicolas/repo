#-*- coding: utf-8 -*-

class Help:
    def __init__(self, repoItem):
        self.repoItem = repoItem
        self.helpContent = ""
        self.helpFile = "/var/help/help.txt"

    def getHelpItem(self):
        with open(self.helpFile) as f:
            helpFileTmp = f.read()
            helpDict = dict(item.split('|') for item in helpFileTmp.split('\n\n'))
        helpItem = helpDict[self.repoItem].strip()

        return helpItem


