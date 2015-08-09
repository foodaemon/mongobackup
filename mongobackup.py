#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import datetime
import subprocess


__author__ = 'Robin Tiwari'
__version__ = '0.1.0'
__description__ = 'MongoDB backup and restore utility'
__license__ = 'MIT'


parser = argparse.ArgumentParser(description='backup/restore mongodb')

parser.add_argument('-d', '--database',
                    type=str,
                    required=False,
                    default=None,
                    help='database')

parser.add_argument('-o', '--output',
                    type=str,
                    required=False,
                    default=None,
                    help='output directory')

parser.add_argument('-u', '--user',
                    type=str,
                    required=False,
                    default=None,
                    help='mongodb user')

parser.add_argument('-p', '--password',
                    type=str,
                    required=False,
                    default=None,
                    help='mongodb password')

parser.add_argument('--port',
                    type=str,
                    required=False,
                    default=None,
                    help='mongodb port')


def backup(args):
    backup_path = os.path.join(os.path.expanduser("~"), 'backup')
    if args.output is not None:
        backup_path = args.output
    now = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
    backup_name = os.path.join(backup_path, now)
    os.mkdir(backup_name)

    if args.output is not None:
        backup_path = args

    stat = subprocess.check_output('mongodump',
                                   '-host', 'localhost',
                                   '-u', '%s' % args.user,
                                   '-p', '%s' % args.password,
                                   '-d', '%s' % args.database,
                                   '--port', '%s' % args.port,
                                   '-o', '%s' % backup_path)

    print(stat)


def restore():
    pass


if __name__ == '__main__':
    args = parser.parse_args()
    backup(args)
