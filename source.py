class car:
    def __init__(self, x, y, ids, ava):
        self.actual_x = x
        self.actual_y = y
        self.car_id = ids
        self.ava_time = ava


class ride:
    def __init__(self, s_x, s_y, e_x, e_y, s_time, f_time, ids):
        self.start_x = s_x
        self.start_y = s_y
        self.end_x = e_x
        self.end_y = e_y
        self.start_time = s_time
        self.end_time = f_time
        self.ride_id = ids
        self.distance = (abs(self.end_x-self.start_x) + abs(self.end_y - self.start_y))


testCars = list()
testRides = list()


def take_best_ride(x, y):
    act_best_ride_id = testRides[0].ride_id
    act_best_start = testRides[0].start_time
    act_best_finish = testRides[0].end_time
    act_best_distance_to_start = abs( x - testRides[0].start_x) + abs( y - testRides[0].start_y)
    for element in testRides:
        if element.start_time <= act_best_start:
            if element.end_time <= act_best_finish:
                if act_best_distance_to_start <= abs(x - element.start_x) + abs(y - element.start_y):
                    act_best_ride_id = element.ride_id
    return act_best_ride_id


