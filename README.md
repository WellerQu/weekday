# weekday
An easy tool for tell your leader what you did.

## install

```
python setup.py install
```

## configuration

save configuration file to your home dir "~/.weekday/"

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
usage: wp [-h] [-v] [-e] [-a APPEND] [-p] [-l] [-c] [-r | -b]

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
  -r, --restore         restore lastest configuration file
  -b, --backup          backup current configuration file
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

## auto send E-mail

You can also use `wp` with [crontab](http://man.linuxde.net/crontab). It can help you to set a task that to send an E-mail every 18:00 friday like this:

```
SHELL=/bin/zsh
PATH=/usr/local/bin
HOME=/Users/nixon

# run tasks
# minute hour day month week command
0 18 * * 5 wp -p
```

## TODO

- Report template
- Support Windows OS
- Unit Test (with CI)
- Read git log for E-mail content
