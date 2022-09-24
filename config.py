# -*- coding: utf-8 -*-
"""
配置类
@author : Shiyang-Li
@time : 2022/9/24 14:35
"""
import os

# 以下参数根据自己的需要进行修改：
SYS_CONFIG = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'wechart.poseidong.com',
    'Accept-Encoding': 'gzip,deflate',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://wechart.poseidong.com/web-wechart/mobile/oa/202103032106xqA5Q7W6/consumer/biaoqi/nearEquip',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; M2012K11AC Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/6046 MicroMessenger/8.0.27.2220(0x28001B59) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    #这里得修改成自己的，一直用我的也不好
    'Cookie': 'SECKEY_ABVK=UFjNg4DYCu8BOdkIgdJDZLxzsx4G+jjdHBlLRMJEDE0%3D; BMAP_SECKEY=BlMUMTYFvVTkcwCfzyxhxL3V0aHRgT4gryyFlsJ9GNiHACK1uxttAXCTgW5rrWDjJxAbRNpkJfHwT-3qHcIc5q36IPS-Mh6gz0iSZgGFYa0HTX7pBsz3chG39jcPWY34E39TFLhSqqUfSRuTiNzShyHpeni8PkHKO0imRVMYzdX2AyozskvT_yDv4ZeM13uE; aliyungf_tc=d50dd8c3863d5316851151416656641869f9c7168f41079f3d07ef85a7ba6c37; token=f5e9b712-420b-41a3-9a24-35275c43a622; psdWxUuid0202103032106xqA5Q7W6=oBfLo1PSzHqkGFDAB66ESdXPwMPc; psdWxAc0=202103032106xqA5Q7W6',
    #教9楼, 教3楼, 国交4, ALL
    'place': '教9楼'
}

def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
