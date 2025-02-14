class Solution(object):
    def isRobotBounded(self, instructions): 

        directions = [(0,1), (1,0), (0,-1), (-1,0)]  
        x, y, d = 0, 0, 0  
        for instr in instructions:
            if instr == "G":  # Move forward
                dx, dy = directions[d]
                x, y = x + dx, y + dy
            elif instr == "L":  # Turn left (anti-clockwise)
                d = (d - 1) % 4
            elif instr == "R":  # Turn right (clockwise)
                d = (d + 1) % 4

        return (x == 0 and y == 0) or (d != 0)
