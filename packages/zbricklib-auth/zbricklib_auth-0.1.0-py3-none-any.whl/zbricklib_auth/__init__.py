from zbricklib.extension import zExtension

class zAuthManager(zExtension):
    _ext_name = 'auth'

    def _install_into(self, app):
        raise NotImplementedError("Not implemented yet")


__all__ = [
    'zAuthManager', 
]