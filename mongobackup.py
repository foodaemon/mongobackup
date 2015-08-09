#!/usr/bin/env python3

import os
import argparse
import datetime


__author__ = 'Robin Tiwari'
__version__ = '0.1.0'
__description__ = 'MongoDB backup and restore utility'
__license__ = 'MIT'


backup_path = os.getcwd()

parser = argparse.ArgumentParser(description='backup/restore mongodb')
parser.add_argument('-t', '--target-dir',
                    type=str,
                    required=False,
                    default=None,
                    help='target directory')
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


def backup():
    now = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
    backup_name = os.path.join(backup_path, now)
    os.mkdir(backup_name)


def restore():
    pass


if __name__ == '__main__':
    args = parser.parse_args()

