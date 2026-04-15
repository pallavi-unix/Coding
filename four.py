def isValidSudoku(board):
    # using sets for each condition makes it easier to look for duplicate, because sets only allows unique elments
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # exploring thorugh each element
    for i in range(9):
        for j in range(9):
            num = board[i][j]

            # passing empty cells
            if num == '.':
                continue

            # checking all the rows
            if num in rows[i]:
                return False
            rows[i].add(num)

            # checking all the columns
            if num in cols[j]:
                return False
            cols[j].add(num)

            # checking all the 3x3 sub boxes
            box_index = (i // 3) * 3 + (j // 3)
            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)

    return True

# time Complexity is O(1) - fixed number of input
# space Complexity is O(1)