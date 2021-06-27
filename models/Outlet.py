class Outlet:
    def __init__(self) -> None:
        self._num_outlets = 0

    def set_count(self, count):
        self._num_outlets = count

    def get_count(self):
        return self._num_outlets
