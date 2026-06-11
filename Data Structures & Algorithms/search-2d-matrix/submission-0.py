class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        loRow = 0
        hiRow = len(matrix) - 1


        while loRow <= hiRow:
            midRow = loRow + (hiRow - loRow) // 2

            # entire row is greater than our target, look above
            if matrix[midRow][0] > target:
                hiRow = midRow - 1
                continue
            # entire row is less than target, look below
            elif matrix[midRow][-1] < target:
                loRow = midRow + 1
            # otherwise, target is in this row if it exists, perform simply binary search
            else:
                lo = 0
                hi = len(matrix[0]) - 1
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    
                    if matrix[midRow][mid] > target:
                        hi = mid - 1
                        continue
                    elif matrix[midRow][mid] < target:
                        lo = mid + 1
                        continue
                    elif matrix[midRow][mid] == target:
                        return True
                return False # target wasn't in the row :(
            
        return False




            
