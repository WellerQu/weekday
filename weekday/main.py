#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import os
import datetime

APP_DESC = '''
Author:         Nix
Github:         https://github.com/WellerQu/weekday
Report Bugs:    xiaoyao.ning@gmail.com
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
    parser.add_argument('-d', '--date',
                        help='specified date, like YYYY-mm-dd')

    args = parser.parse_args()
    print args

    if args.date is None:
        args.date = datetime.now().strftime('%Y-%m-%d')

    tmpFileName = '~/.weekday/%s.rp' % args.date

    if args.version:
        print APP_DESC

    if args.edit:
        os.system('vim %s' % tmpFileName)
        with open(tmpFileName) as r:
            content = r.read()
            print content


if __name__ == '__main__':
    main()
