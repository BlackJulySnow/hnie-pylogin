import os
import time
import random


def login(ip, mac, rand, user, passwd, lan):
    s = "curl 'http://59.71.0.49/portalAuthAction.do' \\\n" \
        "  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp," \
        "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \\\n" \
        "  -H 'Accept-Language: zh-CN,zh;q=0.9' \\\n" \
        "  -H 'Cache-Control: max-age=0' \\\n" \
        "  -H 'Connection: keep-alive' \\\n" \
        "  -H 'Content-Type: application/x-www-form-urlencoded' \\\n" \
        "  -H 'Origin: http://59.71.0.49' \\\n" \
        "  -H 'Referer: http://59.71.0.49/portal.do?wlanuserip=" + ip + "&wlanacname=amnon2&mac=" + mac + \
        "&vlan=0&rand=" + rand + "' \\\n" \
                                 "  -H 'Upgrade-Insecure-Requests: 1' \\\n" \
                                 "  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                                 "Chrome/100.0.4896.88 Safari/537.36' \\\n" \
                                 "  --data 'wlanuserip=" + ip + "&wlanacname=amnon2&chal_id=&chal_vector=&auth_type=PAP&seq_id" \
                                                                "=&req_id=&wlanacIp=59.71.0.47&ssid=&vlan=0&mac=" + mac.replace(
        ":", "%3A") + "&message=&bank_acct" \
                      "=&isCookies=&version=0&authkey=amnoon&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0" \
                      "&randstr=2843&domain=&isRadiusProxy=false&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=1" \
                      "&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=1&logintype=0&act=&is189=false" \
                      "&terminalType=&checkterminal=true&portalpageid=1&listfreeauth=0&viewlogin=1&userid=" + user + \
        "&wisprpasswd=&twocode=0&authGroupId=&alipayappid=&wlanstalocation=&wlanstamac=&wlanstaos" \
        "=&wlanstahardtype=&smsoperatorsflat=3&reason=&res=&userurl=&challenge=&uamip=&uamport=&useridtemp" \
        "=" + user + "&passwd=" + passwd + "&wxuser=' \\\n" \
                                           "  --interface " + lan + " \\\n" \
                                                                    "  --insecure"
    os.system(s)
    # print(s)


def get(user, passwd, wan):
    r = os.popen('curl http://1.1.1.1:8000/ext_portal.magi?url=220.181.38.148 --interface ' + wan)
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


def check(wan):
    cmd = "curl 220.181.38.148 --interface " + wan
    # print(cmd)
    res = os.popen(cmd)
    content = str(res.read())
    # print(content)
    res.close()
    if content.find("http://1.1.1.1:8000/") == -1:
        return True
    else:
        return False


passwds = ["350504200105071526",
           "430111200211180322",
           "430223200209184229",
           "430224200211237226",
           "430482200207301568",
           "430502200303055524",
           "430511200208084518",
           "430703200210309588",
           "430723200212076525",
           "430902200204295022",
           "432522200109151886",
           "433125200110200022",
           "43312720011030502X",
           "433127200106031214",
           "43022420020710181X",
           "431027200304064044",
           "430423200207080021",
           ]
users = ["202007290103",
         "202007290104",
         "202007290105",
         "202007290106",
         "202007290107",
         "202007290108",
         "202007290109",
         "202007290110",
         "202007290111",
         "202007290112",
         "202007290114",
         "202007290115",
         "202007290116",
         "202007290117",
         "202007290118",
         "202007290119",
         "202007290120",
         ]

if __name__ == '__main__':
    # print(passwds[len(passwds)])
    n = 15
    for i, (user, passwd) in enumerate(zip(users, passwds), 1):
        if i > n:
            break
        # print(i, user, passwd)
        if not check("eth" + str(i)):
            print("eth" + str(i) + " is Disconnected")
            if passwd[-1] == 'X':
                passwd = passwd[:-1]
            get(user, passwd[-6:], "eth" + str(i))
            time.sleep(random.randint(1, 3))
        else:
            print("eth" + str(i) + " is Connected")
