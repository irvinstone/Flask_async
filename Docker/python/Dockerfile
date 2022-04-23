FROM python:3.7-slim

RUN mkdir -p /opt/oracle
RUN apt-get update \
    && apt-get -y install libaio-dev \
    && apt-get -y install unzip

ADD ./Docker/python/oracle-instantclient/ /opt/
ADD ./Docker/python/install-instantclient.sh /opt/

COPY ./app /opt/app/

WORKDIR /opt/

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
ENV OCI_HOME=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
# ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

EXPOSE 3000

RUN ./install-instantclient.sh \
&& cd ./app \
&& pip install -r requirements.txt

CMD ["python", "./app/app.py"]