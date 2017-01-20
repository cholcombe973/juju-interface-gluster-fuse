from charmhelpers.core.hookenv import (
    relation_set,
)
from charms.reactive import hook, RelationBase, scopes

class GlusterClientProvider(RelationBase):
    scope = scopes.UNIT

    @hook('{provides:gluster-fuse}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    def provide_mount(self, service, volumes, auth_supported, public_address):
        """
        Provide mount information to a requesting service.
        :param str volumes: The current volumes available for mounting
        :param str auth_supported: Supported auth methods
        :param str public_address: Gluster's public address
        """
        conversation = self.conversation(scope=service)
        relation_set(
            relation_id=conversation.namespace,
            relation_settings={'volumes': volumes})
        opts = {
            'auth': auth_supported,
            'gluster-public-address': public_address,
        }
        conversation.set_remote(**opts)
