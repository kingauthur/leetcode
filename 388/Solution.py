class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        baseLevel = 1
        maxPath = 0
        leftPointer = 0
        dist = {}
        input = input + "\n"
        while True:
            rightPointer = input.index('\n',leftPointer)

            currentLevel = baseLevel
            for i in range(leftPointer,len(input)):
                if input[i] == '\t':
                    currentLevel += 1
                    leftPointer += 1
                else:
                    break
            filestr = input[leftPointer:rightPointer]
            #print(filestr)
            if '.' in filestr:
                path = len(filestr)
                for i in range(currentLevel-1,0,-1):
                    path += dist[i]
                if path > maxPath:
                    maxPath = path
            else:
                dist[currentLevel] = len(filestr) + 1

            leftPointer = rightPointer + 1
            if leftPointer >= len(input):
                break

        return maxPath



strs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
solution = Solution()
print(solution.lengthLongestPath(strs))
