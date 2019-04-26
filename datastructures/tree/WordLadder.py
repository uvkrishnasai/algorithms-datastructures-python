class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if not wordList or endWord not in wordList:
            return 0

        d = self.build_map(beginWord, wordList)

        q, visited = [], []
        q.append((beginWord, 1))

        while q:

            elem, level = q.pop()
            visited.append(elem)

            # print(elem, level)

            nextWords = d[elem]
            if endWord in nextWords:
                return level + 1

            for elem1 in nextWords:
                if elem1 not in visited:
                    q.insert(0, (elem1, level + 1))

        return 0

    def build_map(self, beginWord, wordList):
        d1, d2 = {}, {}

        wordset = set([beginWord] + wordList)

        for elem in wordset:
            for i in range(len(elem)):
                var = elem[:i] + '_' + elem[i + 1:]

                if var not in d1:
                    d1[var] = []
                if elem not in d2:
                    d2[elem] = []

                d1[var].append(elem)
                d2[elem].append(var)

        d3 = {}
        for elem, arr in d2.items():
            d3[elem] = set([])
            for elem1 in arr:
                d3[elem].update(d1[elem1])
            d3[elem].remove(elem)

        return d3

soln = Solution()

# input
wordList = ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]
beginWord = "kiss"
endWord = "tusk"
expectedOutput = 5

actualOutput = soln.ladderLength(beginWord, endWord, wordList)

assert(expectedOutput == actualOutput)

print((3+2)/2)
