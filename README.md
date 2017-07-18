# weekday
小工具 - 用来告诉老板, 我这周干了啥. 主要是通过电子邮件来发送周报.

## install

```
python setup.py install
```

## configuration

save configuration file to your home dir "~"

```
[global]
editor = vim

[to]
email = leader@service.com
cc = leader@service.com,leader@service.com

[from]
email = my@service.com
password = 123456
nickname = nixon

[SMTP]
host = smtp.exmail.qq.com
```

## usage

```
usage: wp [-h] [-v] [-e] [-a APPEND] [-p] [-l] [-c]

Tell your leader what you did this week

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version information
  -e, --edit            open default editor for editing report
  -a APPEND, --append APPEND
                        what did you do today?
  -p, --post            post the specified report to your leader e-mail
  -l, --list            list all the unpost report
  -c, --clean           clean current report
```

## example

If you just only have one information, do it like this:

```
wp -a "My work is done" -p
```

If you have more infomation, do it like this:

```
wp -e -p
```

If you just record information and won't post mail

```
wp -a "some work"
```
