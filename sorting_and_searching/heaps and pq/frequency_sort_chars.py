class Solution:
    # def frequencySort(self, s: str) -> str:
    #     count = Counter(s)
    #     res = []
    #     reverse_count = sorted(count.items(), key = operator.itemgetter(1), reverse = True)
    #     for c, count in reverse_count:
    #         res.extend([c]*count)
    #     return ''.join(res)
            
    def frequencySort(self, s: str) -> str:
        if not s: return s

        # Determine the frequency of each character.
        counts = collections.Counter(s)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)
        
        print(buckets)
        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)