#!/usr/bin/env bash
ansible bh3 -m shell -a 'cd /Application/pitaya/ && svn update && sh pitayad'
