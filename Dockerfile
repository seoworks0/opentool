FROM python:3.6.4-slim-stretch
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get -y install sudo \
    git \
    gcc \
    g++ \
    make \
    curl \
    vim \
    libnss3-dev \
    libappindicator1 \
    libappindicator3-1 \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxss1 \
    libxtst6 \
    lsb-release \
    xdg-utils \
    libgconf2-4 \
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

RUN apt-get update && apt-get install -y wget

RUN apt-get install unzip

RUN wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip \
  && rm chromedriver_linux64.zip \
  && chmod 755 chromedriver \
  && sudo mv /chromedriver /usr/bin/chromedriver

RUN curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get install -f

#RUN sh -c 'wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && \
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
#RUN apt-get update && apt-get install -y google-chrome-stable

RUN pip install gensim mecab-python3
RUN pip install Django
RUN pip install nltk
RUN pip install bs4
RUN pip install PyMySQL
RUN pip install pandas
RUN pip install retry
RUN pip install selenium==3.8.0
#RUN pip install -r requirements.txt

WORKDIR /usr/src/app/
COPY . .
EXPOSE 8000
