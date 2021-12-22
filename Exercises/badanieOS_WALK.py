# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:48:23 2020

@author: 9
"""

import os
        
def give_me_file_name(path_to_dir):
    for f in os.walk(path_to_dir):
        yield(f)
        
for f in give_me_file_name('c:/temp'):
    print(f)
    input('press enter')