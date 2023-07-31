from hmac_apitist.hooks import RequestConverterHook, ResponseConverterHook
from hmac_apitist.requests import session


class Session:
    def __init__(self):
        self._s = session()
        self._s.add_hook(RequestConverterHook)
        self._s.add_hook(ResponseConverterHook)
