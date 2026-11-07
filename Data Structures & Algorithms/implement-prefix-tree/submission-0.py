class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.end = False
        

    def insert(self, word: str) -> None:
        curr = self

        for char in word:
            index = ord(char) - ord('a')

            if not curr.children[index]:
                tmp = PrefixTree()
                curr.children[index] = tmp
            
            curr = curr.children[index]
        
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self

        for char in word:
            index = ord(char) - ord('a')

            if not curr.children[index]:
                return False

            curr = curr.children[index]

        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for char in prefix:
            index = ord(char) - ord('a')

            if not curr.children[index]:
                return False

            curr = curr.children[index]

        return True
       