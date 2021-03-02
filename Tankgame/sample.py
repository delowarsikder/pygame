import random
import os
from tqdm import *
from time import *
from datetime import *
_time=datetime.now()
# print(_time.year)
random.seed(10)
for i in range(5):
    print(random.randint(i,5),sep='-',end=',')

import pygame as pg
if pg.font is None:
    print("font is not available")
    exit()    
    
    

