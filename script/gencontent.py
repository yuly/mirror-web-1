#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import fnmatch

HTTPDIR = '/mnt/mirror'

EXCLUDE = ("tmpfs", ".*")
"""Directories match these glob will be ignored."""


def genRepoList():
    for d in sorted(os.listdir(HTTPDIR), key=str.lower):
        fpath = os.path.join(HTTPDIR, d)

        if not os.path.isdir(fpath) or \
                any(fnmatch.fnmatch(d, p) for p in EXCLUDE):
            continue

        ctime = os.stat(fpath).st_ctime

        yield (d,
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ctime)))


if __name__ == '__main__':
    for i in genRepoList():
        print(i)
