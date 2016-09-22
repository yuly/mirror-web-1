#!/usr/bin/env bash
source /root/.bashrc
cd /mnt/code/mirror-web && git pull
/root/.pyenv/shims/python3 /mnt/code/mirror-web/script/genindex.py
nvm use stable && /usr/local/bin/jekyll build -s /mnt/code/mirror-web -d /mnt/web  && cp -r /mnt/web/* /mnt/mirror
