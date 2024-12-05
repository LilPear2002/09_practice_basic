
class Rotation(object):

    def is_substring(self, s1: str, s2: str) -> bool:
        # 如果s1是空字符串，或者s2是空字符串，或者s1为None，则返回False
        if not s1 or not s2:
            return False
        # 检查s2是否是s1的子字符串
        return s2 in s1

    def is_rotation(self, s1: str, s2: str) -> bool:
        if s1 == "" and s2 == "":
            return True
        # 如果s1或s2为None，或者长度不相等，则直接返回False
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        # 检查s2是否是s1的旋转
        # 通过判断s1+s1中是否包含s2来实现
        return self.is_substring(s1 + s1, s2)