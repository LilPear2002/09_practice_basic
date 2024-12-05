
class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        if string == "":
            return True
        count_dict = {}
        for char in string:
            if char in count_dict:
                return False
            else:
                count_dict[char] = 1
        return True