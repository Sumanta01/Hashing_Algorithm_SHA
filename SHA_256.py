# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:57:58 2023

@author: KIIT
"""

import hashlib 

str="Sumanta Swain"
hashedval=hashlib.sha256(str.encode())
print(hashedval)
print(hashedval.hexdigest())