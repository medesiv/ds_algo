class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            print(_id, rest)
            if rest[0].isalpha():
                return (0, rest, _id)
            else:
                return (1, None, None)

        return sorted(logs, key=get_key)