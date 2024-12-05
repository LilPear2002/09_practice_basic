
def can_form_target(list_of_lists, target_list):
    count = 0
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if list_of_lists[i][j] not in target_list:
                return False
            else:
                count += 1
    if count == len(target_list):
        return True
    return False


# 获取用户输入
user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
user_target_list = list(map(int, input().split()))