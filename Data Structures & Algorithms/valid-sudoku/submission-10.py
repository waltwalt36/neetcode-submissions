# Understand:
#   - Given a 9x9 board
#   - Create a function to find a valid board
#   - A valid board has digits 1-9 without duplicates in each row and column
#   - Each of the nine 3x3 boards must contain digits 1-9 without duplicates
#   - Board length and width can only be a size of 9
#   - Board can only contain digits 1-9 or '.'

# Plan:
#   - Initalize a map, coordinates
#   - Store {key = (row, column) : Digit } O(n)
#   - For loop to go through every element in coordinates
#   - Check if there are duplicates in a row or column, check all rows and columns
#   - Logic here is that everything that is on the same row will have the same row, same for column
#   - Dont have to check every element again just the elements in the dictionary, worst case O(n)



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} # {key = row/column : Digit }
        cols = {}
        boxes = {}

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    box = (r // 3) * 3 + (c // 3)

                    if box not in boxes: 
                        boxes[box] = [board[r][c]]
                    else:
                        boxes[box].append(board[r][c])

                    if r not in rows: 
                        rows[r] = [board[r][c]]
                    else:
                        rows[r].append(board[r][c])
                    
                    if c not in cols:
                        cols[c] = [board[r][c]]
                    else:
                        cols[c].append(board[r][c])

        if self.check(rows) and self.check(cols) and self.check(boxes):
            return True
        else:
            return False

    def check(self, dictionary) -> bool:
        duplicates = False

        for value in dictionary.values():
            duplicates = len(value) != len(set(value))

            if duplicates == True:
                return False

        return True















