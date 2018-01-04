import math
import numpy

def frange(start, stop, step, DECprec=4):
	i = start
	while i < stop:
		yield round(i,DECprec)
		i += step

def to_seg(value, precs=3):
    seg_value = (360 / (2 * math.pi)) * value
    hour = int(seg_value)
    min_value = (seg_value - hour) * 60
    min = int(min_value)
    sec = round((min_value - min) * 60, precs)

    return [hour, min, sec]


def to_rad(value, precs=3):
    rad_value = ((2 * math.pi) / 360) * value
    return round(rad_value, precs)


def q_product(n_a, n_b, v_a, v_b):
    vector_carry = []

    for element in v_a:
        vector_carry.append(element * n_b)

    index = 0
    for element in v_b:
        vector_carry[index] += element * n_a
        index += 1

    cross_carry = numpy.cross(v_a, v_b)

    index = 0
    for _ in vector_carry:
        vector_carry[index] += cross_carry[index]
        index += 1

    return vector_carry


class Quaternion:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.coef_n = a
        self.coef_i = b
        self.coef_j = c
        self.coef_k = d

    ########################################################################

    def get_coef_n(self):
        return self.coef_n

    def get_coef_i(self):
        return self.coef_i

    def get_coef_j(self):
        return self.coef_j

    def get_coef_k(self):
        return self.coef_k

    def get_vector(self):
        return [self.coef_i, self.coef_j, self.coef_k]

    def get_scalar(self):
        return self.coef_n

    def get_values(self):
        return [self.coef_n, self.coef_i, self.coef_j, self.coef_k]

    ########################################################################

    def be_rotational(self, theta = 90, rad_on=False, precs=3):
        if rad_on:
            theta = theta / 2
        else:
            theta = math.radians(theta) / 2

        self.coef_n = round(math.cos(theta), precs)
        self.coef_i = round(self.coef_i * math.sin(theta), precs)
        self.coef_j = round(self.coef_j * math.sin(theta), precs)
        self.coef_k = round(self.coef_k * math.sin(theta), precs)

    def product(self, ref_quat=None, precs=3):
        if ref_quat is None:
            ref_quat = Quaternion()
        else:
            pass

        mid_result = []

        part_n = self.coef_n * ref_quat.get_coef_n() - numpy.dot(self.get_vector(), ref_quat.get_vector())
        part_v = q_product(self.coef_n, ref_quat.get_coef_n(), self.get_vector(), ref_quat.get_vector())

        mid_result.append(part_n)

        carry_list = mid_result + part_v

        index = 0
        for element in carry_list:
            carry_list[index] = round(element, precs)
            index += 1

        return Quaternion(carry_list[0], carry_list[1], carry_list[2], carry_list[3])

    def conjugate(self):
        return Quaternion(self.coef_n, self.coef_i * -1, self.coef_j * -1, self.coef_k * -1)

    ########################################################################

    def to_string(self):
        output = str(self.coef_n)

        if self.coef_i >= 0:
            output += " + " + str(math.fabs(self.coef_i))
        else:
            output += " - " + str(math.fabs(self.coef_i))

        output += "i"

        if self.coef_j >= 0:
            output += " +" + str(math.fabs(self.coef_j))
        else:
            output += " - " + str(math.fabs(self.coef_j))

        output += "j"

        if self.coef_k >= 0:
            output += " + " + str(math.fabs(self.coef_k))
        else:
            output += " - " + str(math.fabs(self.coef_k))

        output += "k"

        return output


def rotate(point, vector, angle, sign="+", its_unitary=True, verbose=False):
    try:
        vector.encode("ascii")
        axis_mode = True

    except:
        axis_mode = False

    if axis_mode:
        if vector == "x":
            vector = [1, 0, 0]

        elif vector == "-x":
            vector = [-1, 0, 0]

        elif vector == "y":
            vector = [0, 1, 0]

        elif vector == "-y":
            vector = [0, -1, 0]

        elif vector == "z":
            vector = [0, 0, 1]

        elif vector == "-z":
            vector = [0, 0, -1]

        else:
            return None

    if its_unitary:
        pass
    else:
        norm = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

        vector[0] = vector[0]/norm
        vector[1] = vector[1]/norm
        vector[2] = vector[2]/norm

    if sign == "+":
        pass
    elif sign == "-":
        index = 0
        for element in vector:
            vector[index] = -1*element
            index += 1
    else:
        return None

    angle = to_rad(angle)/2
    a = math.cos(angle)
    b = vector[0]*math.sin(angle)
    c = vector[1] * math.sin(angle)
    d = vector[2] * math.sin(angle)

    point = numpy.matrix(point)
    rotational = numpy.matrix([[a**2 + b**2 - c**2 - d**2, 2*(b*c - a*d), 2*(a*c + b*d)],
                              [2*(b*c + a*d), a**2 - b**2 + c**2 - d**2, 2*(-1*a*b + c*d)],
                              [2*(-1*a*c + b*d), 2*(a*b + c*d), a**2 - b**2 - c**2 + d**2]])

    point_prime = rotational*point.T

    return point_prime.T.tolist()[0]

"""
def rotate(point, vector, angle, sign="+", its_unitary=True, verbose=False):
    try:
        vector.encode("ascii")
        axis_mode = True

    except:
        axis_mode = False

    if axis_mode:
        if vector == "x":
            vector = [1, 0, 0]

        elif vector == "-x":
            vector = [-1, 0, 0]

        elif vector == "y":
            vector = [0, 1, 0]

        elif vector == "-y":
            vector = [0, -1, 0]

        elif vector == "z":
            vector = [0, 0, 1]

        elif vector == "-z":
            vector = [0, 0, -1]

        else:
            return None

    if its_unitary:
        pass
    else:
        norm = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)

        vector[0] = vector[0]/norm
        vector[1] = vector[1]/norm
        vector[2] = vector[2]/norm

    if sign == "+":
        pass
    elif sign == "-":
        index = 0
        for element in vector:
            vector[index] = -1*element
            index += 1
    else:
        return None

    h = Quaternion(0, vector[0], vector[1], vector[2])
    h.be_rotational(angle)
    if verbose:
        print(h.to_string())

    h_c = h.conjugate()
    if verbose:
        print(h_c.to_string())

    p = Quaternion(0, point[0], point[1], point[2])
    if verbose:
        print(p.get_vector())
        print(p.to_string())

    partial = h.product(p)
    total = partial.product(h_c)

    if verbose:
        print(total.to_string())
        print(total.get_vector())

    del h, h_c, p, partial

    return total.get_vector()
"""