import fileservice as filer


class car:
    def __init__(self, x, y, ids, ava):
        self.actual_x = x
        self.actual_y = y
        self.car_id = ids
        self.ava_time = ava
        self.rides = list()


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


testCars = filer.get_cars()
testRides = filer.get_ride_list()
bonus = filer.get_bonus()
total_points = 0


def take_best_ride(act, x, y):
    act_best_ride_id = testRides[0].ride_id
    act_best_start = testRides[0].start_time
    act_best_finish = testRides[0].end_time
    act_best_distance_to_start = abs(x - testRides[0].start_x) + abs(y - testRides[0].start_y)
    is_bonus = False
    for element in testRides:
        if act > element.start_time:
            continue
        if ((abs(element.start_x - x) + abs(element.start_y - y)) + act) == element.start_time:
            if ((abs(element.start_x - x) + abs(element.start_y - y)) + act) + element.distance < element.end_time:
                return element
            else:
                continue
        elif ((abs(element.start_x - x) + abs(element.start_y - y)) + act) > element.start_time and is_bonus == False:
            if ((abs(element.start_x - x) + abs(element.start_y - y)) + act + element.distance) < element.end_time:
                if act_best_start > element.start_time and act_best_distance_to_start > element.distance:
                    act_best_ride_id = element.ride_id
    for element in testRides:
        if element.ride_id == act_best_ride_id:
            return element


def count_points(s_time, exp_s_time, f_time, exp_f_time, dist):
    global total_points
    if s_time == exp_s_time:
        total_points += bonus
    if f_time <= exp_f_time:
        total_points += dist



#punktowanie: czas na miejscu +B pkt, przejazd w czasie dystans
#parametry stopu: kroki, koniec przejazdow

def ride_menager():
    actual_steps = 0
    while filer.get_final_step() < actual_steps and len(testRides) > 0:
        for cars_element in testCars:
            best_option = take_best_ride(cars_element.ava_time, cars_element.actual_x, cars_element.actual_y)
            arrival_at_start_time = abs(cars_element.actual_x - best_option.start_x) + abs(cars_element.actual_y - best_option.start_y)
            count_points((arrival_at_start_time + cars_element.ava_time), best_option.start_time,
                         (arrival_at_start_time + cars_element.ava_time + best_option.distance),
                         best_option.end_time, best_option.distance)
            cars_element.ava_time += arrival_at_start_time + best_option.distance
            cars_element.actual_x = best_option.end_x
            cars_element.actual_y = best_option.end_y
            actual_steps += arrival_at_start_time + best_option.distance
            testRides.remove(best_option)





