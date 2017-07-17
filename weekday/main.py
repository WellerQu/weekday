#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import os
import datetime
import ConfigParser
from pydash.objects import defaults

APP_DESC = '''
Author:         Nix
Github:         https://github.com/WellerQu/weekday
Version:        1.0.0
'''


def main():
    parser = argparse.ArgumentParser(
        description='Tell your leader what you did this week')

    # define command line parameters
    parser.add_argument('-v', '--version',
                        action='store_true',
                        help='show the version information')
    parser.add_argument('-e', '--edit',
                        action='store_true',
                        help='open default editor for editing report')
    parser.add_argument('-a', '--append',
                        help='what did you do today?')
    parser.add_argument('-p', '--post',
                        action='store_true',
                        help='post the specified report to your leader e-mail')
    parser.add_argument('-l', '--list',
                        action='store_true',
                        help='list all the unpost report')

    args = parser.parse_args()

    tmpFileName = ('%s/.weekday/current.rp' % os.environ['HOME'])
    confFileName = ('%s/.weekday/conf' % os.environ['HOME'])

    conf = loadConfig(confFileName)

    dir = os.path.dirname(tmpFileName)
    if not os.path.exists(dir):
        os.mkdir(dir)

    if args.version:
        print APP_DESC

    if args.append:
        append(tmpFileName, args.append)

    if args.edit:
        edit(tmpFileName, editor=conf.editor)

    if args.post:
        os.remove(tmpFileName)
        print datetime.now().strftime('%Y-%m-%d')

    if args.list:
        listContent(tmpFileName)


def loadConfig(configName):
    conf = {}

    if os.path.exists(configName):
        with open(configName, 'rb') as r:
            config = ConfigParser.ConfigParser()
            config.readfp(r)
            conf['editor'] = config.get('global', 'editor')

    return defaults(conf, {'editor': 'vim'})


def append(fileName, text):
    with open(fileName, 'a') as w:
        w.write('- %s\r\n' % text)


def edit(fileName, **conf):
    os.system('%s %s' % (conf['editor'], fileName))


def listContent(fileName):
    with open(fileName, 'r') as r:
        line = r.readline().rstrip('\r\n')
        while line:
            print line
            line = r.readline().rstrip('\r\n')

if __name__ == '__main__':
    main()
