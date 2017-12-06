#!/bin/bash

sudo netstat -ntu |  awk '/^tcp/{ print $5 }' | sed -r 's/:[0-9]+$//' | sort | uniq -c | sort -n | tail -1

