# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:51:53 2021

@author: Home
"""

from pyspark import SparkContext as sc


rdd = sc.parallelize(["b", "c", "a"])
output = sorted(rdd.map(lambda x: (x,1))).collect()
print(output)
