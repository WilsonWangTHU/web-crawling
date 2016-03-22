# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib

html = urllib.urlopen('http://www.baidu.com')
print(html.read())
