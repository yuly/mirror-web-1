#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import gencontent
import json

OUTFILE = "/mnt/code/mirror-web/_data/mirrors.json"
data = []


def main():
    logger = logging.getLogger('mirrors-genindex')
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
    logger.addHandler(ch)
    repolist = gencontent.genRepoList()
    for i in repolist:
        data.append(
            {
                "folder": i[0],
                "update": i[1]
            }
        )
    logger.info('begin file writing...')
    with open(OUTFILE, 'w') as fout:
        fout.write(json.dumps(data))
        fout.write(os.linesep)
    logger.info('completed! exiting...')


if __name__ == "__main__":
    main()
