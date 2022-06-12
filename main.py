import os
import sys
import time
import random


def login(ip, mac, rand, user, passwd, lan):
    s = "curl 'http://59.71.0.49/portalAuthAction.do' \\\n"\
                  "  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"\
                  "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \\\n"\
                  "  -H 'Accept-Language: zh-CN,zh;q=0.9' \\\n"\
                  "  -H 'Cache-Control: max-age=0' \\\n"\
                  "  -H 'Connection: keep-alive' \\\n"\
                  "  -H 'Content-Type: application/x-www-form-urlencoded' \\\n"\
                  "  -H 'Origin: http://59.71.0.49' \\\n"\
                  "  -H 'Referer: http://59.71.0.49/portal.do?wlanuserip=" + ip + "&wlanacname=amnon2&mac=" + mac +\
                  "&vlan=0&rand=" + rand + "' \\\n"\
                  "  -H 'Upgrade-Insecure-Requests: 1' \\\n"\
                  "  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "\
                  "Chrome/100.0.4896.88 Safari/537.36' \\\n"\
                  "  --data 'wlanuserip=" + ip + "&wlanacname=amnon2&chal_id=&chal_vector=&auth_type=PAP&seq_id"\
                  "=&req_id=&wlanacIp=59.71.0.47&ssid=&vlan=0&mac=" + mac.replace(":", "%3A") + "&message=&bank_acct"\
                  "=&isCookies=&version=0&authkey=amnoon&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0"\
                  "&randstr=2843&domain=&isRadiusProxy=false&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=1"\
                  "&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=1&logintype=0&act=&is189=false"\
                  "&terminalType=&checkterminal=true&portalpageid=1&listfreeauth=0&viewlogin=1&userid=" + user +\
                  "&wisprpasswd=&twocode=0&authGroupId=&alipayappid=&wlanstalocation=&wlanstamac=&wlanstaos"\
                  "=&wlanstahardtype=&smsoperatorsflat=3&reason=&res=&userurl=&challenge=&uamip=&uamport=&useridtemp"\
                  "=" + user + "&passwd=" + passwd + "&wxuser=' \\\n"\
                  "  --interface " + lan + " \\\n"\
                  "  --insecure"
    os.system(s)
    # print(s)


def get(user, passwd, wan):
    r = os.popen('curl http://1.1.1.1:8000/ext_portal.magi?url=baidu.com --interface ' + wan)
    content = str(r.read())
    r.close()
    macAndIP = content[content.find('("') + 2:content.find('")')]
    mac = macAndIP[macAndIP.find("mac=") + 4:macAndIP.find("&vlan")]
    ip = macAndIP[macAndIP.find("ip=") + 3:macAndIP.find("&wlanacname")]
    rand = macAndIP[macAndIP.find("&rand=") + 6:]
    # print(content)
    print(ip)
    print(mac)
    # print(rand)
    # print(mac.replace(":", "%3A"))
    login(ip, mac, rand, user, passwd, wan)


def logout(wan):
    cmd = "curl 'http://1.1.1.1:8000/userout.magi' \\\n"\
                "-H 'Connection: keep-alive' \\\n"\
                "-H 'Cache-Control: max-age=0' \\\n"\
                "-H 'Upgrade-Insecure-Requests: 1' \\\n"\
                "-H 'Origin: http://1.1.1.1:8000' \\\n"\
                "-H 'Content-Type: application/x-www-form-urlencoded' \\\n"\
                "-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \\\n"\
                "-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \\\n"\
                "-H 'Referer: http://1.1.1.1:8000/logout.htm' \\\n"\
                "-H 'Accept-Language: zh-CN,zh;q=0.9' \\\n"\
                "--data 'imageField.x=131&imageField.y=14' \\\n"\
                "--interface " + wan + " \\\n"\
                "--insecure"
    os.system(cmd)


def check(wan):
    cmd = "curl baidu.com --interface " + wan
    # print(cmd)
    res = os.popen(cmd)
    content = str(res.read())
    # print(content)
    res.close()
    if content.find("http://1.1.1.1:8000/") == -1:
        return True
    else:
        return False


passwds = ["52213020010096010",
           "420802200112100657",
           "421123200309251218",
           "42112520020422067X",
           "511502200301248446",
           "431122200209016312",
           "432524200210171913",
           "431021200201093514",
           "430523200209280014",
           "433127200205245816",
]


if __name__ == '__main__':
    # loginout("eth0")
    # get("202009140201", "096010", "eth0")
    parms = sys.argv
    if parms[1] == "login":
        for i in range(1, 11):
            if str(i) not in parms[2:] and parms[2] != "all":
                continue
            user = "2020091402" + "{:02}".format(i)

            passwd = passwds[i - 1][-6:]
            if passwd[-1] == 'X':
                passwd = passwds[i - 1][-7:-1]
            print(user)
            print(passwd)
            print("eth" + str(i))
            get(user, passwd, "eth" + str(i))
            time.sleep(random.randint(1, 10))
    elif parms[1] == "logout":
        for i in range(1, 11):
            if str(i) not in parms[2:] and parms[2] != "all":
                continue
            print("eth" + str(i))
            logout("eth" + str(i))
    elif parms[1] == "check":
        flag = []
        for i in range(1, 11):
            if str(i) not in parms[2:] and parms[2] != "all":
                continue
            # print("eth" + str(i))
            flag.append(("eth" + str(i), check("eth" + str(i))))
        for i in range(1, 11):
            print(flag[i - 1][0] + " is " + ("Connected" if flag[i - 1][1] else "Disconnected"))

