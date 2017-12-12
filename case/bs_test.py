#coding=utf-8
from bs4 import BeautifulSoup
# -*- coding: utf-8 -*
import requests
import unittest
import re
url = "http://localhost/bugfree/site/login"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    #"Cookie": "jenkins-timestamper-offset=-28800000; _ga=GA1.1.1182575328.1489848951; ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE=YWRtaW46MTUxMzg2MDQxMTM0NTo3ZmU0NDM2MjQxMTM1ZWQ2YzE0NTRhMDY4ZDFkZGRiNTAxODMyYmIyOTk4M2ZjMmRlM2U2ZWM0MTZkM2E0ZGRl; PHPSESSID=2ujp3e562c2p1m9b0oidsl4cf7; 0b07747fdb99050c940b5420ca53f01b=ba8d4c08c299b553db8d5c3d240ecdebdcf2c83fs%3A163%3A%2260ee3ab82c4252f1be145c6fcead6daaf75b76a9a%3A4%3A%7Bi%3A0%3Bs%3A1%3A%221%22%3Bi%3A1%3Bs%3A5%3A%22admin%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A2%3A%7Bs%3A8%3A%22realname%22%3Bs%3A15%3A%22%E7%B3%BB%E7%BB%9F%E7%AE%A1%E7%90%86%E5%91%98%22%3Bs%3A8%3A%22username%22%3Bs%3A5%3A%22admin%22%3B%7D%7D%22%3B; language=8c4d7df988bbdad68ff76ee8da57a6f3fe501acas%3A5%3A%22zh_cn%22%3B; 1_product=2328027bff0ba9812cdf8ff788b52288a621ccf0s%3A1%3A%221%22%3B"
    }
body2 = {"LoginForm[username]":"",
        "LoginForm[password]":"123456",
        "LoginForm[language]":"zh_cn",
        "LoginForm[rememberMe]":"0",
        "LoginForm[rememberMe]":"1"
}
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()

    def test_login_usernameisnull(self):

        res = self.s.post(url=url,data=body2, headers = header)
        blog = res.content
        #print blog
        soup = BeautifulSoup(blog, 'html.parser')
        print soup
        r=soup(id="login-error-div")
        v=r[0].string
       # print v
        print type(v)

        result=re.findall('<div id="login-error-div" >(.+?)&nbsp;&nbsp;</div>',res.content)

        #print result
        #print result[0]
        ex = '用户名 不可为空白.'
        #self.assertIn(result[0],ex)
        self.assertEqual(v,ex)

if __name__ == '__main__':
    unittest.main()