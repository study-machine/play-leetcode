class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = dict()
        u = set()
        _str = str.split(' ')
        if len(pattern) != len(_str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if _str[i] in u:
                    return False 
                d[pattern[i]] = _str[i]
                u.add(_str[i])
            else:
                if d[pattern[i]] != _str[i]:
                    return False
        return True


if __name__ == '__main__':

    pattern = "abba"
    _str = "dog cat cat dog"
    # pattern = "abba"
    # _str = "dog dog dog dog"
    print Solution().wordPattern(pattern, _str)
