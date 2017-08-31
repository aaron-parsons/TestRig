class ProcessVariable:
    def __init__(self, name, default_value=0):
        self._name = name
        self._default_value = default_value

    def get_name(self):
        return self._name

    def get_default_value(self):
        return self._default_value