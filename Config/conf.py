# -*- coding: utf-8 -*-
'''
@Time    : 2020/4/7 14:22
@Author  : amay
@File    : conf.py
'''
def server_ip():#访问ip参数化
    dev_ip='http://10.10.10.132:12000/'
    test_ip='http://qnn-testing-api.maxrupees.com/'
    sit_ip='https://m.maxrupees.com/client/app/business/index.html#/login'
    return dev_ip
def sql_conf():#sql参数化
    host = '10.10.10.132'
    user = 'qsq'
    password = 'BstK3nP5jeu29jvy'
    port = 3306
    database = 'maxrupees'
    charset = 'utf8'
    return host,user,password,port,database,charset
#print('host','user','password','port','database','charset')

