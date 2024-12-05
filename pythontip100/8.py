class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError("参数不能为空")
        if num < 1:
            raise ValueError("参数必须大于1")
        my_list = []
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                my_list.append("FizzBuzz")
            elif i % 3 == 0:
                my_list.append("Fizz")
            elif i % 5 == 0:
                my_list.append("Buzz")
            else:
                my_list.append(str(i))
        return my_list
