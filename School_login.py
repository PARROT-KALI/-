import gzip
import re
import requests

def main():
    url="http://223.2.10.172/eportal/InterFace.do?method=login"
    #url="http://223.2.10.172"
    header={
        "Host": "223.2.10.172",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer":"http://223.2.10.172/eportal/index.jsp?wlanuserip=f02d3ceebe91a66dd8241e8c990bc44f&wlanacname=b58fcda622d8bb5b&ssid=52eefd2d44d14e03&nasip=e54b2b351c575112839c042a61804a4c&snmpagentip=&mac=c333a0ec35dce67de99ed7b4cc6b1043&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=b58fcda622d8bb5b&vid=3bf335ea1f92ea70&port=df97b6a8f945c660&nasportid=f5eb983692924fa26e6431fe9df4835fbbd407254bfc1c2d5eacd01ddf73fc56e7c61abdadb6e3d3",
        "Content-Length":"937",
        "Cookie":"EPORTAL_USER_GROUP=%E6%9C%AC%E7%A7%91%E7%94%9F; EPORTAL_COOKIE_USERNAME=19200340; EPORTAL_COOKIE_PASSWORD=444f2d6fe284cb8df31dd7548a8a3563c6cb3b1cd8616fa9136251a65cd402a275072b7843299896c7e49f04d15d2781de1b44df7aa971bb8e9c04558d15d51677dfe006f8c53166aa550f71be5dbaf542acecf756fab69e0130101d2241234b728cf24c42a2c119130b2be580696a8c4047e5a52616baa1141423eb058f0991; EPORTAL_COOKIE_SERVER=%E7%94%B5%E4%BF%A1%E6%9C%8D%E5%8A%A1; EPORTAL_COOKIE_SERVER_NAME=%E7%94%B5%E4%BF%A1%E6%9C%8D%E5%8A%A1; EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_SAVEPASSWORD=true; servicesJsonStr=19200340%40%25%25username%40%25%25%E6%A0%A1%E5%9B%AD%E7%BD%91%E6%9C%8D%E5%8A%A1%40%E7%94%B5%E4%BF%A1%E6%9C%8D%E5%8A%A1%40%E8%81%94%E9%80%9A%E6%9C%8D%E5%8A%A1; EPORTAL_AUTO_LAND=; JSESSIONID=7A15EE2B8B61A2E3E51B8D08B36FAF50",
        "DNT":'1',
        'Connection': 'close'
    }

    data={
        "userId": "19200340",
        "password": "444f2d6fe284cb8df31dd7548a8a3563c6cb3b1cd8616fa9136251a65cd402a275072b7843299896c7e49f04d15d2781de1b44df7aa971bb8e9c04558d15d51677dfe006f8c53166aa550f71be5dbaf542acecf756fab69e0130101d2241234b728cf24c42a2c119130b2be580696a8c4047e5a52616baa1141423eb058f0991",
        "service": "%25E7%2594%25B5%25E4%25BF%25A1%25E6%259C%258D%25E5%258A%25A1",  # 电信服务url两次
        "queryString":"wlanuserip%253Df02d3ceebe91a66dd8241e8c990bc44f%2526wlanacname%253Db58fcda622d8bb5b%2526ssid%253D52eefd2d44d14e03%2526nasip%253De54b2b351c575112839c042a61804a4c%2526snmpagentip%253D%2526mac%253Dc333a0ec35dce67de99ed7b4cc6b1043%2526t%253Dwireless-v2%2526url%253D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%2526apmac%253D%2526nasid%253Db58fcda622d8bb5b%2526vid%253D3bf335ea1f92ea70%2526port%253Ddf97b6a8f945c660%2526nasportid%253Df5eb983692924fa26e6431fe9df4835fbbd407254bfc1c2d5eacd01ddf73fc56e7c61abdadb6e3d3",
        "operatorPwd":"",
        "operatorUserId": "",
        "validcode": "",
        "passwordEncrypt": "true"
    }
    '''post=requests.session().post(url,data=data,headers=header)
    data=gzip.decompress(requests.session().get("http://223.2.10.172",headers=header).content).decode("gbk") #校园网采用gbk编码。如果登录成功回报中会有“登录成功”四个字
    str=re.findall(r'<title>(.*?)</title>',data)'''
    print(str)

if __name__=="__main__":
    main()