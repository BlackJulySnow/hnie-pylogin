# PyLogin

基于Python的校园网登录
主要用于在Linux环境下无法通过浏览器登陆或者多网卡聚合登陆情况
本项目仅依赖最基本的python或者bash环境即可，但是在Windows上需要进行一定调整


## Python版本
```bash
python getNetwork.py #检测掉线网口并登陆
```

```bash
python main.py login all #登陆所有网口
python main.py login 1 2 3 #登陆1，2，3网口
python main.py logout 1 2 3 #退出1，2，3网口
python main.py check all #检测所有网口是否掉线
```

## Bash版本
```bash
bash login.sh #登陆所有网口
bash logout.sh #退出
```
