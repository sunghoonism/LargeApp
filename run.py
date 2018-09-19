# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 10:00:45 2018

@author: csh
"""

#Run a test server.
from app import app
app.run(host='0.0.0.0', port=8050, debug=True)

# 출처: http://hamait.tistory.com/864 [HAMA 블로그]