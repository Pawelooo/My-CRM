from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

from base.src.model.config import GET_FILE, FILE_ITEM, \
    FILE_SUBITEM, TODO, INPROGRESS, DONE, STATUS, COLOR_COLUMN, COLOR_TEXT, \
    QUANTITY, SIZE_COLUMN, FONT_SIZE
from base.src.service.jfs import JsonFromService


class Diagram:

    def __init__(self):
        self.items = JsonFromService().read_file(FILE_ITEM, GET_FILE)
        self.subitems = JsonFromService().read_file(FILE_SUBITEM, GET_FILE)
        self.values = {}

    def get_quantity(self):
        cnt = Counter()
        for obj in self.items:
            cnt[obj[STATUS].lower()] += 1
        for obj in self.subitems:
            cnt[obj[STATUS].lower()] += 1
        cnt = dict(cnt)
        cnt = list(cnt.items())
        for i in range(len(cnt)):
            if cnt[i][0] == TODO.lower():
                self.values[cnt[0][0]] = cnt[0][1]
            if cnt[i][0] == INPROGRESS.lower():
                self.values[cnt[1][0]] = cnt[1][1]
            if cnt[i][0] == DONE.lower():
                self.values[cnt[2][0]] = cnt[2][1]

    def create_diagram(self):
        height = self.values.values()
        bars = [text.capitalize() for text in self.values.keys()]
        y_pos = np.arange(len(height))
        plt.figure(figsize=(SIZE_COLUMN, SIZE_COLUMN))
        plt.bar(y_pos, height, color=COLOR_COLUMN)
        plt.xticks(y_pos, bars)
        plt.xlabel(STATUS.capitalize(), fontsize=FONT_SIZE, color=COLOR_TEXT)
        plt.ylabel(QUANTITY, fontsize=FONT_SIZE, color=COLOR_TEXT)
        plt.show()
