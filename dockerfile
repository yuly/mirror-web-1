FROM ubuntu:16.04
MAINTAINER Xuanwo <xuanwo.cn@gmail.com>
RUN locale-gen en_US.UTF-8 && export LC_ALL=en_US.UTF-8 && export LANG=en_US.UTF-8
RUN sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update -y && apt-get install openssh-client ruby ri ruby-dev bundler zlib1g-dev nodejs -y
RUN bundle config build.nokogiri --use-system-libraries

