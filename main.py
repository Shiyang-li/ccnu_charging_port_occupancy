import requests
import config

place = config.get("place")

headers = {
    'Accept': config.get("Accept"),
    'Host': config.get("Host"),
    'Accept-Encoding': config.get("Accept-Encoding"),
    'Connection': config.get('Connection'),
    'Referer': config.get('Referer'),
    'User-Agent': config.get('User-Agent'),
    'Cookie': config.get('Cookie')
}

url0 = 'https://wechart.poseidong.com/web-wechart/mobile/oa/202103032106xqA5Q7W6/consumer/biaoqi/nearEquip/load?t=1663991357096&pageSize=45&longitude=114.357407&latitude=30.520992&range=10000&name=&recordStart=1&recordEnd=45&page=1&_=1663991356675'

url = 'https://wechart.poseidong.com/web-wechart/mobile/oa/202103032106xqA5Q7W6/consumer/biaoqi/nearEquip/port?deviceNo=%s&equipId=199869&_=1663991356676'

def get_info():
    r0 = requests.get(url0,headers=headers)
    res_r0 = r0.json()
    result_r0 = res_r0["records"]
    return result_r0

def output_result(ID, headers):
    print(name," ",end="")
    r = requests.get(url % (ID), headers=headers)
    res_r = r.json()
    result_r = res_r["data"]
    for j in result_r:
        if j["statusStr"] == "可用":
            print("port:",j["port"],"Status:","\33[0;36m",j["statusStr"],"\33[0m"," ",end="") 
    print()

if __name__ == '__main__':
    result_r0 = get_info()
    for i in result_r0:
        name = i["equipCache"]["name"]
        ID = i["equipCache"]["cd"]
        if  name.encode("utf-8").decode("utf-8")[0:3] == place.encode("utf-8").decode("utf-8"):    
            output_result(ID, headers)
        if place == "ALL":
            output_result(ID, headers)
