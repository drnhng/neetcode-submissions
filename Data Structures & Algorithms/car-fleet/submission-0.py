class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        position_speed = [[a, b] for a,b in zip(position, speed)]
        position_duration = [[a, math.ceil((target-a)/b)] for a, b in position_speed]
        
        position_duration = sorted(position_duration, reverse=True)

        car_fleets = 0
        curr_dur = -1
        for i, tup in enumerate(position_duration):
            pos, dur = tup
            if i == 0:
                car_fleets += 1
                curr_dur = dur
                continue
            if dur <= curr_dur:
                continue
            else:
                curr_dur = dur
                car_fleets+=1
        return car_fleets