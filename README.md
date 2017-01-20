# Overview

This interface layer handles the communication between Gluster 
and a client that requires an admin key. The expectation here is 
that the client will mount the volume using the gluster native fuse 
client.  Please see here: [gluster native client](https://gluster.readthedocs.io/en/latest/Administrator Guide/Setting Up Clients) for more 
information on the fuse client.

# Usage

## Requires

This interface layer will set the following states, as appropriate:

  * `{relation_name}.available` The gluster client has been related to a provider.
  The following accessors will be available:
   - volumes - The available volume names that can be mounted
   - gluster-public-address - The public address of one of the Gluster servers. 
     The fuse client knows how to discover the rest of them.


