import pickle

from src.controller.controller import Controller
from src.model.test import Test


def main() -> None:
    Controller().control()


if __name__ == '__main__':
    # with open('test.txt', 'wb') as handle:
    #     pickle.dump([Test('a', 'b')], handle, protocol=pickle.HIGHEST_PROTOCOL)

    main()
