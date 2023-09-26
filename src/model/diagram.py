from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

from src.model.config import GET_FILE, FILE_STATUS_NAME, FILE_ITEM, \
    FILE_SUBITEM
from src.service.jfs import JsonFromService


class Diagram:

    def __init__(self):
        self.items = JsonFromService().read_file(FILE_ITEM, GET_FILE)
        self.subitems = JsonFromService().read_file(FILE_SUBITEM, GET_FILE)
        self.values = {}


    def get_quantity(self):
        cnt = Counter()
        for obj in self.items:
            cnt[obj['status'].lower()] += 1
        for obj in self.subitems:
            cnt[obj['status'].lower()] += 1
        cnt = dict(cnt)
        cnt = list(cnt.items())
        for i in range(len(cnt)):
            if cnt[i][0] == 'todo':
                self.values[cnt[0][0]] = cnt[0][1]
            if cnt[i][0] == 'inprogress':
                self.values[cnt[1][0]] = cnt[1][1]
            if cnt[i][0] == 'done':
                self.values[cnt[2][0]] = cnt[2][1]


    def create_diagram(self):
        height = self.values.values()
        bars = self.values.keys()
        y_pos = np.arange(len(height))
        plt.figure(figsize=(10, 5))
        plt.bar(y_pos, height, color='#268626')
        plt.xticks(y_pos, bars)
        plt.xlabel('Status', fontsize=15, color='#323232')
        plt.ylabel('Quantity', fontsize=15, color='#323232')
        plt.show()


def main() -> None:
    d1 = Diagram()
    d1.get_quantity()
    d1.create_diagram()


if __name__ == '__main__':
    main()