class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        currentCarFleetTime = (target - cars[0][0]) / cars[0][1]
        fleets = 1

        for i in range(len(cars)):
            if (target - cars[i][0]) / cars[i][1] > currentCarFleetTime:
                fleets += 1
                currentCarFleetTime = (target - cars[i][0]) / cars[i][1]

        return fleets
