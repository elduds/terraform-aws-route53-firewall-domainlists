#!/usr/bin/env bash

./fetch_domains.py

ALLMD5=$(md5sum all_lists.json |awk '{print $1}')
NEWMD5=$(md5sum new_all_lists.json |awk '{print $1}')

if [ "${ALLMD5}" != "${NEWMD5}" ]; then
    