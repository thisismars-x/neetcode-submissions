class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False
        

    def addWord(self, word: str) -> None:
        curr = self

        for char in word:
            index = ord(char) - ord('a')

            if not curr.children[index]:
                curr.children[index] = WordDictionary()

            curr = curr.children[index]

        curr.end = True
        

    def search(self, word: str) -> bool:

        def _s(node: WordDictionary, w: str) -> bool:
            if not w:
                return node.end

            if w[0] == '.':
                # if any index matches then yay
                for i in range(26):
                    if node.children[i]:
                        if _s(node.children[i], w[1:]):
                            return True

                return False
            else:
                index = ord(w[0]) - ord('a')
                if not node.children[index]:
                    return False
    
                return _s(node.children[index], w[1:])


        return _s(self, word)