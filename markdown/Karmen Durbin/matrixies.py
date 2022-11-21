###########（っ＾▿＾）Templates for Matrixes ###########

##### ( ≖.≖) EASY ######

####### ʕ•́ᴥ•̀ʔっ DFS Matrix Easy Sudo ######
#? build graph, 2 nested for loops
#? call helper function for flagging visited nodes
#? build the helper function _____ 
#? flag nodes
#? recursively visit neighboring cells


from collections import deque

def count_islandsDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_islands = 0 #* counter to return res
    for r in range(rows):
            for c in range(cols):
                if (matrix[r][c] == 1):  # only if the cell is a land
                    # we have found an island
                    total_islands += 1
                    visitIslandDFS(matrix, r, c)
    return total_islands


def visitIslandDFS(matrix,  x,  y):
    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
        return  # return, if it is not a valid cell
    if (matrix[x][y] == 0):
        return  # return, if it is a water cell

    matrix[x][y] = 0  # mark the cell visited by making it a water cell

    #! recursively visit all neighboring cells (horizontally & vertically)
    visitIslandDFS(matrix, x + 1, y)  # lower cell
    visitIslandDFS(matrix, x - 1, y)  # upper cell
    visitIslandDFS(matrix, x, y + 1)  # right cell
    visitIslandDFS(matrix, x, y - 1)  # left cell


def main(): #* ask about the size of the matrix before writing testcases
    print(countIslandsDFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
main()

######### ʕ•́ᴥ•̀ʔっ BFS Matrix Easy Sudo ########

from collections import deque

def countIslandsBFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for r in range(rows):
        for c in range(cols):
            if (matrix[r][c] == 1):  # only if the cell is a land
                # we have found an island
                totalIslands += 1
                visitIslandBFS(matrix, r, c)
    return totalIslands


def visitIslandBFS(matrix,  x,  y):
    neighbors = deque([(x, y)])
    while neighbors:
        row, col = neighbors.popleft() #! if you change the "popleft" to "pop" you will have a DFS iterative approach...

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue  # continue, if it is not a valid cell
        if matrix[row][col] == 0:
            continue  # continue if it is a water cell

        matrix[row][col] = 0  # mark the cell visited by making it a water cell

        #* insert all neighboring cells to the queue for BFS
        neighbors.extend([(row + 1, col)])  # lower cell
        neighbors.extend([(row - 1, col)])  # upper cell
        neighbors.extend([(row, col + 1)])  # right cell
        neighbors.extend([(row, col - 1)])  # left cell


def main():
    print(countIslandsBFS([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]))
    print(countIslandsBFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]))
main()


