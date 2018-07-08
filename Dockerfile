#FROM ubuntu:latest

# Build essentials
#RUN apt-get update
#RUN apt-get install -y curl build-essential
#RUN apt-get install -y wget

# Mecab
#RUN wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
#RUN tar zxvf mecab-0.996.tar.gz
#RUN cd mecab-0.996; ./configure --enable-utf8-only; make; make install; ldconfig

# Ipadic
#RUN wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM"
#RUN tar zxvf mecab-ipadic-2.7.0-20070801.tar.gz
#RUN cd mecab-ipadic-2.7.0-20070801
#RUN ./configure --with-charset=utf8
#RUN make
#RUN make install
#RUN echo "dicdir = /usr/local/lib/mecab/dic/ipadic" > /usr/local/etc/mecabrc

# Clean up
#RUN apt-get remove -y build-essential
#RUN rm -rf mecab-0.996.tar.gz*
#RUN rm -rf mecab-ipadic-2.7.0-20070801*


# FROM python:3-alpine
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/

FROM python:3.6.4-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get -y install sudo \
    git \
    gcc \
    g++ \
    make \
    curl \
    xz-utils \
    liblzma-dev \
    file \
    mecab-ipadic \
    mecab-ipadic-utf8

RUN mkdir -p /opt/downloads && \
    cd /opt/downloads && \
    git clone https://github.com/taku910/mecab.git && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git

RUN cd /opt/downloads/mecab/mecab && \
    ./configure  --enable-utf8-only && \
    make && \
    make check && \
    make install

RUN apt-get -y install
RUN cd /opt/downloads/mecab-ipadic-neologd && \
    ./bin/install-mecab-ipadic-neologd -n -y

RUN pip install gensim mecab-python3
RUN pip install Django
RUN pip install nltk
RUN pip install bs4
RUN pip install PyMySQL
RUN pip install pandas
RUN pip install retry
#RUN pip install -r requirements.txt

WORKDIR /usr/src/app/
COPY . .
EXPOSE 8000
