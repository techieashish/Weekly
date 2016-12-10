#!/usr/bin/env python
__author__ = 'ASHISH'
from Weekly import Weekly


def weeky():
    while True:
        try:
            global  us_show, us_se , us_ep
            us_show = input('\nEnter the show name :')
            us_se = input('\nEnter season: ')
            us_ep = input('\nEnter episode to be downloaded: ')
        except ValueError:
            print('\nPlease enter the details correctly')
            continue
        else:
            break
    run = Weekly(us_show, us_se, us_ep)
    input()


weeky()
