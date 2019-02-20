#!/usr/bin/python


def cal_vat(price,vat):
    return price * (100+vat)/100



print(cal_vat(200,12))
