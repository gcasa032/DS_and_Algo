"""

You are programming for a self-driving car system. The system is given a 2D map of a city, where each point represents a traffic light. 

All the traffic lights are RED at the beginning, which means the car cannot pass through them. The number of each point represents the time after which a light will turn GREEN, meaning the car can pass through it.

The car is asked to drive from the top-left corner to the right-bottom corner. The car can only drive in the right or down direction. Please find the earliest time that the car can get to the destination.

Sample Input:

1 2 0 3
4 6 5 1
9 2 5 7
5 4 2 2

Sample Output:

5


Explanation: The best route is

1 2 0
    5
    5
    2 2


"""

class ShortestPath:

    def shortest_path(self,city: 'list[list[int]]') -> int:
        return min(self.shortest_path_helper(city, 0, 0, -1))

    def shortest_path_helper(self, city, x, y, maxVal):

        pathVal = []

        if x < len(city[y]) -1:
            pathVal.extend(self.shortest_path_helper(city, x + 1, y, max(maxVal, city[x][y])))
        if y < len(city) -1:
            pathVal.extend(self.shortest_path_helper(city, x , y + 1, max(maxVal, city[x][y])))
        if x == len(city[0]) -1 and y == len(city) -1:
            pathVal.append(max(maxVal, city[x][y]))

        return pathVal

city = [[1,2,0,3],[4,6,5,1],[9,2,5,7],[5,4,2,2]]
test = ShortestPath()
print(test.shortest_path(city))