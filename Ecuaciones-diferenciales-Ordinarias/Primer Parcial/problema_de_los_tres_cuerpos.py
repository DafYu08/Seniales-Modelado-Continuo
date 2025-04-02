#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:31:18 2024

@author: Estudiante
"""

import random
album = [0,0,0,0,0,0]
contador = 0

while sum(album) < 6:
    mi_figu = random.randint(0,5)
    album[mi_figu] = 1
    contador = contador + 1
    