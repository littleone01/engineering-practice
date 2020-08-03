class TypeNotSupportError(Exception):
    def __init__(self, *args):
        self.msg = args[0] if args else 'available data is not enough'

    def __str__(self):
        return self.msg
