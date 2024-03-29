FROM python:3.8.11
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

COPY requirements.txt .

RUN apt-get install -y vim less

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY applications applications/

CMD ["python", "applications/app.py"]
