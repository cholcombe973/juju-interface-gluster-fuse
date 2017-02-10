# Overview

This interface layer handles the communication between Gluster 
and a client. The expectation here is 
that the client will mount the volume using the NFS client.  Please see here: [gluster nfs client](http://gluster.readthedocs.io/en/latest/Administrator%20Guide/Setting%20Up%20Clients/#using-nfs-to-mount-volumes) for more information using the NFS mount.

# Usage

## Requires

This interface layer will set the following states, as appropriate:

  * `{relation_name}.available` The gluster client has been related to a provider.
  The following accessors will be available:
   - volumes - The available volume names that can be mounted
   - gluster-public-address - The public address of one of the Gluster servers. 
     The fuse client knows how to discover the rest of them.


