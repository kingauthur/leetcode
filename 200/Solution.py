def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    island = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # first element
            if grid[i][j] == '1':
                island = island + 1
                dfs(grid,i,j)

    return island

def dfs(grid,rowIndex,columIndex):
    if rowIndex < 0 or rowIndex >= len(grid):
        return
    if columIndex < 0 or columIndex >= len(grid[0]):
        return


    #print(rowIndex,columIndex)
    if grid[rowIndex][columIndex] == '1':
        grid[rowIndex] = grid[rowIndex][:columIndex] + '2' + grid[rowIndex][columIndex+1:]
        dfs(grid,rowIndex - 1, columIndex)
        dfs(grid,rowIndex + 1, columIndex)
        dfs(grid,rowIndex, columIndex - 1)
        dfs(grid,rowIndex, columIndex + 1)


grid=["11000","11000","00100","00011"]
#print(grid[2][1])
print(numIslands(grid))
#print(len(grid[0]))
