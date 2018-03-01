import source

file_name = 'b_should_be_easy.in'
file = open(file_name, "r")
first_line = file.readline()
first_line_split = first_line.split(" ")


def get_bonus():
    return first_line_split[4]


def get_ride_list():
    rides = list()
    x = 0
    for line in file:
        line_split = line.split(" ")
        rides.append(source.ride(int(line_split[0]), int(line_split[1]), int(line_split[2]), int(line_split[3]), int(line_split[4]), int(line_split[5]), x))
        x += 1
    return rides


def get_cars():
    cars = list()
    for x in range(int(first_line_split[2])):
        cars.append(source.car(0, 0, x, 0))
    return cars


def get_final_step():
    return first_line_split[5]


def save(cars):
    s_file = open("results_"+file_name, "w")
    for car in cars:
        for ride in car.rides:
            s_file.write(str(ride) + " ")
        s_file.write("\n")



