class WordDictionary:
        def __init__(self):

            self.words = defaultdict(list)


        def addWord(self, word: str) -> None:

            self.words[len(word)].append(word)


        def search(self, word: str) -> bool:

            n = len(word)

            if '.' in word:
                
                for w in self.words[n]:
                    if all(word[i] in (w[i], '.') for i in range(n)):
                        return True

                else: return False

            return word in self.words[n]