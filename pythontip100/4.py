class CompressString(object):

    def compress(self, string):
        if string is None:
            return None
        if string == '':
            return ''
        result = ''
        current_char = string[0]
        count = 1
        for char in string[1:]:
            if char == current_char:
                count += 1
            else:
                result += current_char + (str(count) if count > 1 else '')
                current_char = char
                count = 1
        result += current_char + (str(count) if count > 1 else '')
        if len(result) < len(string):
            return result
        return string

compressSting = CompressString()
print(compressSting.compress('aabcccccaaa'))