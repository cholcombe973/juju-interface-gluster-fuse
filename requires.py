from charms.reactive import hook, RelationBase, scopes


class GlusterRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:gluster-nfs}-relation-{joined,changed}')
    def changed(self):
        conv = self.conversation()
        if conv.get_remote('gluster-public-address'):
            # this unit's conversation has a public-address, so
            # it is part of the set of available units
            conv.set_state('{relation_name}.available')

    @hook('{requires:http}-relation-{departed}')
    def departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.available')

    @hook('{provides:gluster-fuse}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')

    def volumes(self):
        """
        Return a list of available volumes
        :return: list of volume names
        """
        conv = self.conversation()
        vols = conv.get_remote('volumes')
        return vols.split(" ")
