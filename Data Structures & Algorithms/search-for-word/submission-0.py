class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]

        def dfs(row, col, idx):
            # Entire word matched
            if idx == len(word):
                return True

            # Out of bounds or character mismatch
            if (
                row < 0 or row >= n or
                col < 0 or col >= m or
                board[row][col] != word[idx]
            ):
                return False

            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = "#"

            # Explore all four directions
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if dfs(nr, nc, idx + 1):
                    return True

            # Backtrack
            board[row][col] = temp

            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False