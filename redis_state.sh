#!/bin/bash
echo "crawl:master:state: `redis-cli get crawl:master:state`"
echo "node:* cnt: `redis-cli KEYS 'node:*' | wc -l`"
echo "Pending: `redis-cli scard pending`"
echo "Reachable: `redis-cli scard reachable`"
echo "Open: `redis-cli scard open`"
echo "OpenData: `redis-cli scard opendata`"
