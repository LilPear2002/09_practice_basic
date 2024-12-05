class Permutations(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if str1 == "" or str2 == "":
            return False
        count_dict = {}
        for char in str1:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
        for char in str2:
            if char in count_dict:
                count_dict[char] -= 1
            else:
                return False
        for count in count_dict.values():
            if count != 0:
                return False
        return True
