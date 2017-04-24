!Znodes

Znodes is currently being developed to estimate the size of the Zcash network by finding all the reachable nodes in the network. The current methodology involves sending [getaddr](https://en.bitcoin.it/wiki/Protocol_specification#getaddr) messages recursively to find all the reachable nodes in the network, starting from a set of seed nodes. Znodes uses Zcash protocol version 170002 (i.e. >= /MagicBean:1.0.0/), so nodes running an older protocol version will be skipped.

* [Network Snapshot](https://bitnodes.21.co/nodes/)

* [24-hour Charts](https://bitnodes.21.co/dashboard/)

* [Live Map](https://bitnodes.21.co/nodes/live-map/)

* [Network Map](https://bitnodes.21.co/nodes/network-map/)

* [New Transactions](https://bitnodes.21.co/dashboard/transactions/)

* [Leaderboard](https://bitnodes.21.co/nodes/leaderboard/)

Znodes is a fork of Bitnodes for Zcash
See [Provisioning Bitnodes Network Crawler](https://github.com/ayeowch/bitnodes/wiki/Provisioning-Bitcoin-Network-Crawler) for steps on setting up a machine to run Znodes. The [Redis Data](https://github.com/ayeowch/bitnodes/wiki/Redis-Data) contains the list of keys and their associated values that are written by the scripts in this project.
In the near future we will be able to grant access to the data, e.g. network snapshots, collected using this project, in a way that's compatible with [Bitnodes API v1.0](https://bitnodes.21.co/api/).
