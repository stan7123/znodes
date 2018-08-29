#!/bin/bash
echo "crawl:master:state: `redis-cli get crawl:master:state`"
echo "Pending: `redis-cli scard pending`"
echo "Reachable: `redis-cli scard reachable`"
echo "Open: `redis-cli scard open`"
echo "OpenData: `redis-cli scard opendata`"
