from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._current_report = 0

    def __next__(self):
        try:
            print(self._data)
            report = self._data[self._current_report]
        except IndexError:
            raise StopIteration()
        else:
            self._current_report += 1
            return report
