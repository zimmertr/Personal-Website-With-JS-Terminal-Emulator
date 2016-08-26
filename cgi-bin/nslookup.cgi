#!/bin/bash

echo "Content-type: text"
echo
nslookup $QUERY_STRING | sed '1,4d' | sed '$d'
