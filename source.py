import math
class car:
    def __init__(self, x, y, id, ava):
        self.actual_x = x
        self.actual_y = y
        self.car_id = id
        self.ava_time = ava

class ride:
    #start x y
    #end x y
    #distance
    #start time
    #finish time
    #id
    def __init__(self, s_x, s_y, e_x, e_y, s_time, f_time, id):
        self.start_x = s_x
        self.start_y = s_y
        self.end_x = e_x
        self.end_y = e_y
        self.start_time = s_time
        self.end_time = f_time
        self.distance = (abs(self.end_x-self.start_x) + abs(self.end_y - self.start_y))

