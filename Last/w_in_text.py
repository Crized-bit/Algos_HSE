import sys
import string


class Trie:
    def __init__(self, terminal=False, letter=None, parent=None):
        self.letter = letter
        self.is_terminal = terminal
        self.action = dict()
        self.parent = parent
        self.suf = None

    def add_word(self, word: str):
        cur_node = self
        for letter in word:
            if cur_node.action.get(letter, None) is None:
                cur_node.action.update({letter: Trie(letter=letter, parent=cur_node)})
            cur_node = cur_node.action.get(letter)
        cur_node.is_terminal = word

    def move(self, letter):
        if (node := self.action.get(letter, None)) is not None:
            return node
        else:
            self.action.update({letter: self.get_suf_link().move(letter)})
            return self.action.get(letter)

    def get_suf_link(self):
        if self.suf is None:
            self.suf = self.parent.get_suf_link().move(self.letter)
        return self.suf


def main():
    text = sys.stdin.readline().rstrip()

    min_node = Trie()
    my_trie = Trie(parent=min_node)
    my_trie.suf = min_node
    for sym in string.ascii_lowercase:
        min_node.action.update({sym: my_trie})

    words_dict = dict()
    for _ in range(int(sys.stdin.readline().rstrip())):
        word = sys.stdin.readline().rstrip()
        my_trie.add_word(word)
        words_dict.update({word: 'No'})

    for symbol in text:
        my_trie = my_trie.move(symbol)
        if my_trie.is_terminal:
            words_dict[my_trie.is_terminal] = 'Yes'

        good_node = my_trie
        while good_node.parent:
            good_node = good_node.get_suf_link()
            if good_node.is_terminal:
                words_dict[good_node.is_terminal] = 'Yes'
    print(*words_dict.values(), sep='\n')


if __name__ == '__main__':
    main()
