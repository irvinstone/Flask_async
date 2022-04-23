#!/usr/bin/env bash

unzip instantclient-basiclite-linux.x64-19.15.0.0.0dbru.zip -d /opt/oracle

mv /opt/oracle/instantclient_19_15 /opt/oracle/instantclient

rm instantclient-basiclite-linux.x64-19.15.0.0.0dbru.zip
rm install-instantclient.sh
