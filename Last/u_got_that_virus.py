import sys
import queue
import threading
from concurrent.futures import ThreadPoolExecutor


class Trie:
    def __init__(self, terminal=False, letter=None, parent=None):
        self.letter = letter
        self.is_terminal = terminal
        self.action = dict()
        self.parent = parent
        self.suf = None
        self.color = 0

    def add_word(self, word: str):
        cur_node = self
        for letter in word:
            if cur_node.action.get(letter, None) is None:
                cur_node.action.update({letter: Trie(letter=letter, parent=cur_node)})
            cur_node = cur_node.action.get(letter)
        cur_node.is_terminal = True

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
    min_node = Trie()
    my_trie = Trie(parent=min_node)
    my_trie.suf = min_node
    for sym in ['0', '1']:
        min_node.action.update({sym: my_trie})

    for _ in range(int(sys.stdin.readline().rstrip())):
        word = sys.stdin.readline().rstrip()
        my_trie.add_word(word)

    q = queue.Queue()

    q.put(my_trie)

    while not q.empty():
        item = q.get()
        for value in item.action.values():
            q.put(value)
            if value.parent:
                vertex = value.get_suf_link()
                if vertex.is_terminal:
                    value.is_terminal = True

    def dfs(vert):
        vert.color = 1
        for i in ['0', '1']:
            vertex = vert.move(i)
            if not vertex.is_terminal:
                if vertex.color == 0:
                    dfs(vertex)
                elif vertex.color == 1:
                    print('TAK')
                    sys.exit(0)
        vert.color = 2

    dfs(my_trie)

    print('NIE')


if __name__ == '__main__':
    sys.setrecursionlimit(30000)
    threading.stack_size(1000000)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(main)
        future.result()
