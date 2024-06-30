class CustomerException(Exception):
    def __init__(self):
        Exception.__init__(self)

raise CustomerException