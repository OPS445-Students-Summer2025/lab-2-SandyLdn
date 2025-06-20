#!/usr/bin/env python3

#Author: Sandra Foster
#Author ID: 146466230
#Date Created: 2025/06/06

import sys


if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3
while timer > 0:
    print(timer)
    timer = timer - 1
print('blast off!')
