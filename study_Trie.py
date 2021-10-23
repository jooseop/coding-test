# https://youtu.be/7e1b70dTAd4
class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


def add(word, head):
    current = head

    for w in word:
        if w not in current:
            current[w] = {}
        current = current[w]
    current['*'] = True
