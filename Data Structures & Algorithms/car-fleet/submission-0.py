class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        fleets = 0
        while cars:
            curr_pos, curr_speed = cars.pop()
            target_time = float(target - curr_pos) / curr_speed
            fleets += 1
            while cars and float(target - cars[-1][0]) / cars[-1][1] <= target_time:
                cars.pop()

        return fleets

        