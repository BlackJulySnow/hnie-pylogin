Login() {
  num=$(((RANDOM % 1000000) + 100000))
  url=$(curl "http://1.1.1.1:8000/ext_portal.magi?url=baidu.com&radnum=$num&a.magi" --interface "$3")
  ip=${url#*ip=}
  ip=${ip%%&*}
  echo "$ip"

  mac=${url#*mac=}
  mac=${mac:0:17}

  radnum=${url#*rand=}
  radnum=${radnum%%\"*}
  curl "http://59.71.0.49/portalAuthAction.do" \
    -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
    -H "Accept-Language: zh-CN,zh;q=0.9" \
    -H "Cache-Control: no-cache" \
    -H "Connection: keep-alive" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -H "Origin: http://59.71.0.49" \
    -H "Pragma: no-cache" \
    -H "Referer: http://59.71.0.49/portal.do?wlanuserip=$ip&wlanacname=amnon2&mac=$mac&vlan=0&rand=$radnum" \
    -H "Upgrade-Insecure-Requests: 1" \
    -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" \
    --data-raw "wlanuserip=$ip&wlanacname=amnon2&chal_id=&chal_vector=&auth_type=PAP&seq_id=&req_id=&wlanacIp=59.71.0.47&ssid=&vlan=0&mac=${mac//:/%3A}&message=&bank_acct=&isCookies=&version=0&authkey=amnoon&url=&usertime=0&listpasscode=0&listgetpass=0&getpasstype=0&randstr=4958&domain=&isRadiusProxy=false&usertype=0&isHaveNotice=0&times=12&weizhi=0&smsid=1&freeuser=&freepasswd=&listwxauth=0&templatetype=1&tname=1&logintype=0&act=&is189=false&terminalType=&checkterminal=true&portalpageid=1&listfreeauth=0&viewlogin=1&userid=$1&wisprpasswd=&twocode=0&authGroupId=&alipayappid=&wlanstalocation=&wlanstamac=&wlanstaos=&wlanstahardtype=&smsoperatorsflat=3&reason=&res=&userurl=&challenge=&uamip=&uamport=&useridtemp=$1&passwd=$2&wxuser=" \
    --interface "$3"
}

Logout() {
  curl "http://1.1.1.1:8000/userout.magi" --interface "$1"
}

Check() {
  num=$(((RANDOM % 1000000) + 100000))
  url=$(curl "http://1.1.1.1:8000/ext_portal.magi?url=baidu.com&radnum=$num&a.magi" --interface "$1")
  if [[ "$url" == *"http://1.1.1.1:8000/logout.htm"* ]]; then

    echo 'online'
    return 0
  else
    echo 'not online'
    return -1
  fi
}

usr=("202007020218" "202007020219" "202007020220" "202007020221" "202007020222" "202007020223" "202007020224" "202007020225")
pwd=("020011" "179793" "135361" "178026" "195247" "163863" "190181" "136422")

# Login $usr $pwd $eth

#Login 202009140227 157519 eth10

#exit
for i in {1..10}; do
  #    echo ${usr[i - 1]}
  #    echo ${pwd[i - 1]}
  #    echo eth$i
#  Check eth"$i"
#  if [ $? -eq 0 ]; then
#    echo 123
#  else
#    Login "${usr[i - 1]}" "${pwd[i - 1]}" eth"$i"
#  fi
  Login "${usr[i - 1]}" "${pwd[i - 1]}" "eth$i"
done
