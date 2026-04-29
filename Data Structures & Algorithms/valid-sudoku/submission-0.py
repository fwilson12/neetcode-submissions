class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):    
                box_indices = (row // 3 * 3, col // 3 * 3) # col, row indices of top left corner of 3x3 box, used as key for hashmap (tuple: set)
                if (board[row][col] in rows[row]) or (board[row][col] in cols[col]) or (board[row][col] in boxes[box_indices]):
                    return False
                else:
                    if board[row][col] != ".":
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        boxes[box_indices].add(board[row][col])
        return True
