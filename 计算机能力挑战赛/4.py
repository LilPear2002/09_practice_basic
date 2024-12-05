def is_safe(board, row, col, n):
    # 检查这一列是否有其他皇后
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n):
    # 如果已经放置了n个皇后，则找到一个解决方案
    if row == n:
        return 1

    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            count += solve_n_queens_util(board, row + 1, n)
    return count

def solve_n_queens(n):
    board = [-1] * n  # 初始化棋盘，-1表示没有放置皇后
    return solve_n_queens_util(board, 0, n)

# 读取输入
n = int(input().strip())

# 计算并输出结果
print(solve_n_queens(n))