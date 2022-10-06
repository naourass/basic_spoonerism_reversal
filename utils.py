def load_dict():
    with open('words_list.txt') as f:
        return set(f.read().split())


dict = load_dict()
