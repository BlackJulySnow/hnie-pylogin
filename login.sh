#!/bin/bash
IP=""
MAC=""
RAND=""
USERNAME=""
PASSWD=""
curl 'http://59.71.0.49/portalAuthAction.do' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://59.71.0.49' \
  -H 'Referer: http://59.71.0.49/portal.do?wlanuserip=10.0.38.101&wlanacname=amnon2&mac=65:26:00:0a:00:00&vlan=0&rand=6285a971' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36' \
  --data 'wlanuserip=10.0.38.101&wlanacname=amnon2&chal_id=&chal_vector=&auth_type=PAP&seq_id=&req_id=&wlanacIp=59.71.0.47&ssid=&vlan=0&mac=65%3A26%3A00%3A0a%3A00%3A00&message=&bank_acct=&isCookies=&version=0&authkey=amnoon&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0&randstr=2843&domain=&isRadiusProxy=false&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=1&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=1&logintype=0&act=&is189=false&terminalType=&checkterminal=true&portalpageid=1&listfreeauth=0&viewlogin=1&userid=学号&wisprpasswd=&twocode=0&authGroupId=&alipayappid=&wlanstalocation=&wlanstamac=&wlanstaos=&wlanstahardtype=&smsoperatorsflat=3&reason=&res=&userurl=&challenge=&uamip=&uamport=&useridtemp=学号&passwd=密码&wxuser=' \
  --insecure
