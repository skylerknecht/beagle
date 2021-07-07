## Beagle
### Versions
 * 0.2 : correctly parses frames/datagrams/segments and filters on dstport/srcip
 * 0.0 : initial code base and project structure

### Features
* [x] Regular expression filtering for source ip and destionation port.

### ToDo
* [ ] Add application layer protocol parsing and options.

### Documentation
```
srcip: Filter on the source IP found in the datagram.
dstport: Filter on the destionation port found in the segment.
```

### Using Connect
```sh
sudo ./hunt --interface eth0
```
