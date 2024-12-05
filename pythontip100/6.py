class Solution(object):

    def find_diff(self, str1, str2):
        # 如果传入的字符串有 None ，需要使用 raise 语句抛出 TypeError异常
        if str1 is None or str2 is None:
            raise TypeError("参数不能为空")
        count_dict = {}
        if len(str1) > len(str2):
            for char in str1:
                if char in count_dict:
                    count_dict[char] += 1
                else:
                    count_dict[char] = 1
            for char in str2:
                if char in count_dict:
                    count_dict[char] -= 1
            for key,value in count_dict.items():
                if value != 0:
                    return key
        else:
            for char in str2:
                if char in count_dict:
                    count_dict[char] += 1
                else:
                    count_dict[char] = 1
            for char in str1:
                if char in count_dict:
                    count_dict[char] -= 1
                else:
                    return char
            for key,value in count_dict.items():
                if value != 0:
                    return key
