import json, math, re
import urllib.parse

def convert_to_degrees(angle):
    degrees = math.degrees(angle) - 90

    while degrees < -180:
        degrees += 360
    while degrees > 180:
        degrees -= 360
    return degrees

class Point:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def distance_to(self, other_point):
        return math.sqrt((self.x-other_point.x)**2+(self.z-other_point.z)**2)

    def angle_to(self, other_point):
        return convert_to_degrees(math.atan2(other_point.z - self.z, other_point.x - self.x))

    def snap_to_chunk_center(self):

        chunk_x = round((self.x-8) / 16)
        chunk_z = round((self.z-8) / 16)

        return Point(16*chunk_x+8, 16*chunk_z+8)

    def __str__(self):
        return "{} {}".format(self.x, self.z)

class Function:

    def __init__(self, slope, x_base, y_base):
        self.slope = slope
        self.x_base = x_base
        self.y_base = y_base

    def get_val(self, inp):
        # y = m(x-i) + y

        output = inp - self.x_base
        output *= self.slope
        output += self.y_base

        return output

    def get_inp_for_val(self, val):
        # y = m(x-i) + d
        # y - d = m(x-i)
        # (y - d)/m = x - i
        # (y - d)/m + i = x

        inp = val - self.y_base
        div = self.slope
        if div == 0.0:
            div = 0.0001
        inp /= div
        inp += self.x_base

        return inp


class Ray(Point):
    def __init__(self, x, z, angle):
        super().__init__(x, z)
        self.angle = angle

    def get_as_func(self):

        slope = math.tan(math.radians(90+self.angle))

        func = Function(slope, self.x, self.z)

        return func

    def get_intersection_with(self, other):

        this_func = self.get_as_func()
        diff_func = other.get_as_func()

        this_const = this_func.slope * -1 * this_func.x_base
        this_const += this_func.y_base

        diff_const = diff_func.slope * -1 * diff_func.x_base
        diff_const += diff_func.y_base

        intersect_x = (diff_const - this_const)
        div = this_func.slope - diff_func.slope
        if div == 0:
            div = 0.0001
        intersect_x /= div

        intersect_z = this_func.get_val(intersect_x)

        # print(this_func.slope)
        # print(diff_func.slope)
        # print(self.angle)
        # print("-----")

        return Point(intersect_x, intersect_z)

class ThrowInfo:
    def __init__(self, side, pixel_side, accuracy):
        self.side = side
        self.pixel_side = pixel_side
        self.accuracy = accuracy

    def __str__(self):
        return "acc {:1d} side {} p_side {}".format(self.accuracy, self.side, self.pixel_side)


def guess_left_error(angle):
    return 0.845 - (0.0111*((angle%90.0)-45.0))**2

def guess_right_error(angle):
    return -1*guess_left_error(angle)







def adjust_angle_hitbox(measured, info):

    min_diff = 360
    adjusted = -1000
    target = -1000

    if info.side == "right":
        adjusted = measured + guess_right_error(measured)
    elif info.side == "left":
        adjusted = measured + guess_left_error(measured)
    else:
        

    return adjusted



def parse_coords_txt(line):
    # line = line.split()
    x_coord = float(line[6])
    z_coord = float(line[8])
    angle = float(line[9])

    while angle < -180:
        angle += 360
    while angle > 180:
        angle -= 360

    throw = Ray(x_coord, z_coord, angle)

    return throw


def parse_throw_info(line):

    if line[0] == "L" or line[0] == "l":
        side = "left"
    elif line[0] == "R" or line[0] == "r":
        side = "right"
    accuracy = (int(line[1])-1) // 2
    pixel_side = "right"


    return ThrowInfo(side, pixel_side, accuracy)
    # side = line[2]
    
def parse_structure_coords(line):

    line = line.split()

    x_coord = float(line[2])
    z_coord = float(line[4])

    return Point(x_coord, z_coord)


def get_location_from_input(input_txt):
    # input_txt = "/execute in minecraft:overworld run tp @s 240.93 69.00 -263.42 -87.41 -31.64 2 L /execute in minecraft:overworld run tp @s 242.05 69.00 -246.18 -87.05 -31.89 3 R"

    matched = re.match("^(\/execute.+?)(\/execute.+)$", input_txt)

    throw_1_txt = matched[1]
    throw_1_txt_args = throw_1_txt.split(" ")
    throw_1_coords_txt = throw_1_txt_args[:11]
    throw_1_info_txt = throw_1_txt_args[11:]

    throw_2_txt = matched[2]
    throw_2_txt_args = throw_2_txt.split(" ")
    throw_2_coords_txt = throw_2_txt_args[:11]
    throw_2_info_txt = throw_2_txt_args[11:]

    throw_1 = parse_coords_txt(throw_1_coords_txt)
    throw_2 = parse_coords_txt(throw_2_coords_txt)

    throw_1_info = parse_throw_info(throw_1_info_txt)
    throw_2_info = parse_throw_info(throw_2_info_txt)

    throw_1.angle = adjust_angle_hitbox(throw_1.angle, throw_1_info)
    throw_2.angle = adjust_angle_hitbox(throw_2.angle, throw_2_info)

    intersection_point = throw_1.get_intersection_with(throw_2)

    # loop forwards along the line with better accuracy, score each chunk
    snapped_point = intersection_point.snap_to_chunk_center()
    base_x = snapped_point

    max_range = 128

    better_throw = throw_2
    better_acc = throw_2_info.accuracy
    other_throw = throw_1
    worse_acc = throw_1_info.accuracy
    if throw_1_info.accuracy > throw_2_info.accuracy:
        # print("weird")
        better_throw = throw_1
        better_acc = throw_1_info.accuracy
        other_throw = throw_2
        worse_acc = throw_2_info.accuracy

    stronghold_guess = None
    best_guess_score = -1
    best_primary_score = -1

    if abs(better_throw.get_as_func().slope) > 1:
        snapped_point.x -= max_range
    else:
        snapped_point.z -= max_range

    loops = 2*(max_range // 16)
    ind = 0

    while ind <= loops:
        display = False

        if abs(better_throw.get_as_func().slope) > 1:
            snapped_point.x += 16
            snapped_point.z = better_throw.get_as_func().get_val(snapped_point.x)
        else:
            snapped_point.z += 16
            snapped_point.x = better_throw.get_as_func().get_inp_for_val(snapped_point.z)

        pos_stronghold_loc = snapped_point.snap_to_chunk_center()

        better_angle_error = abs(better_throw.angle_to(pos_stronghold_loc) - better_throw.angle)
        worse_angle_error = abs(other_throw.angle_to(pos_stronghold_loc) - other_throw.angle)

        better_angle_zscore = min(math.sqrt(max((better_angle_error-0.004) / (0.0001*((5-better_acc)**3)),1)),16)
        worse_angle_zscore = min(math.sqrt(max((worse_angle_error-0.004) / (0.0001*((5-worse_acc)**3)),1)),16)

        # print(better_angle_zscore)
        # print(worse_angle_zscore)

        chunk_score = abs((2**better_angle_zscore)*(2**worse_angle_zscore))

        if stronghold_guess is None or chunk_score < best_guess_score:
            display = True
            stronghold_guess = pos_stronghold_loc
            best_guess_score = chunk_score
        
        ind += 1

    return stronghold_guess

def lambda_handler(event, context):
    # print(event)
    # print(context)
    # TODO implement
    # r
    # print(result)
    # result = "idk"
    
    input_txt = urllib.parse.unquote(event["rawQueryString"])
    # print(input_txt)
    result = get_location_from_input(input_txt)
    return {
        'statusCode': 200,
        'body': str(result)
    }


