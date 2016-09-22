#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import fnmatch

HTTPDIR = '/mnt/mirror'

EXCLUDE = ("tmpfs", ".*")
"""Directories match these glob will be ignored."""


def CTimeWA(dirpath):
    """A unreliable workaround for nested repos.
    See comments in main program.
    """
    ctime = 0
    for subd in os.listdir(dirpath):
        subdirpath = os.path.join(dirpath, subd)
        if not os.path.isdir(subdirpath):
            continue

        _ctime = os.stat(subdirpath).st_ctime
        if _ctime > ctime:
            ctime = _ctime

    return ctime

def genRepoList():
    for d in sorted(os.listdir(HTTPDIR), key=str.lower):
        fpath = os.path.join(HTTPDIR, d)

        if not os.path.isdir(fpath) or \
                any(fnmatch.fnmatch(d, p) for p in EXCLUDE):
            continue

        # Change time is lastsync time if sync destination is exactly the same
        # top-level dir of http. However, some repos are divided to several
        # sub-dirs which are actually sync-ed instead of top-level directory.
        # We need to check these sub-dirs to find correct lastsync time.
        ctime = os.stat(fpath).st_ctime

        # Since checking all sub-dirs wastes much time, the script just check
        # repos whose top-level dirs have a old change time.
        if time.time() - ctime > 3600 * 24 * 2:
            _ctime = CTimeWA(fpath)
            if _ctime > ctime:
                ctime = _ctime

        yield (d,
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ctime)))


if __name__ == '__main__':
    for i in genRepoList():
        print(i)
