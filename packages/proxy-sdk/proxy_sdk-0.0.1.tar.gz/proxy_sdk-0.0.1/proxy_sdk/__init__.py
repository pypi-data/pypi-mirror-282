from enum import Enum, auto
from typing import Optional


class ProxyType(Enum):
    
    socks4  = auto()
    socks5  = auto()
    http    = auto()

class Proxy:

    toString: str = None

    def __new__(cls, type: ProxyType, host: str = None, port: int = None, username: Optional[str] = None, password: Optional[str] = None) -> 'Proxy':
        if username is not None and password is not None:
            build = '{0}:{1}@{2}:{3}'.format(username, password, host, port)
        else:
            if host is not None and port is not None:
                build = '{0}:{1}'.format(host, port)
            else:
                build = None      
        if not build:
            setattr(Proxy, 'toString', build)
        else: 
            if type == ProxyType.http:
                setattr(Proxy, 'toString', f'http://{build}')
            elif type == ProxyType.socks5:
                setattr(Proxy, 'toString', f'socks5://{build}')
            elif type == ProxyType.socks4:
                setattr(Proxy, 'toString', f'socks4://{build}')
        return cls