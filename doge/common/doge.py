# coding: utf-8


class Response(object):
    def __init__(self, code=0, value=None, exception=None):
        self.value = value
        self.exception = exception
        self.prosess_time = 0


class Request(object):
    def __init__(self, service, method, *args, meta=None):
        self.service = service
        self.method = method
        self.args = args
        self.meta = meta or {}
