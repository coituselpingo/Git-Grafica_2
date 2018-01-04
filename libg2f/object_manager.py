from libg2f import GraphData as GD


def generate_dupla(input_list):
    output_carry = []
    counter = 0
    first = True
    index = 0
    length = len(input_list)
    while index < length + 2:
        ref = input_list[index % length]
        if first:
            pair_carry = [ref]
            first = False
        else:
            pass

        if counter == 0:
            pair_carry.pop(0)
            pair_carry.append(ref)
        else:
            pair_carry.append(ref)
            output_carry.append([pair_carry[0], pair_carry[1]])

        counter = (counter + 1) % 2
        index += 1

    output_carry.append([input_list[-1], input_list[0]])
    return output_carry

def read_objt(path, verbose=False):

    if path[-4:] == "objt":
        print("READING-FILE")
        carry_obj = GD.GraphicalObject()
        read_buffer = open(path, 'r')

        counter = 0
        first = True
        for line in read_buffer:
            if first:
                point_carry = [[float(i) for i in line.split("\t")]]
                first = False
            else:
                pass

            if counter == 0:
                point_carry.pop(0)
                point_carry.append([float(i) for i in line.split("\t")])
            else:
                point_carry.append([float(i) for i in line.split("\t")])
                carry_obj.push_edge(GD.Point(point_carry[0][0], point_carry[0][1], point_carry[0][2]),
                                    GD.Point(point_carry[1][0], point_carry[1][1], point_carry[1][2]),
                                    None, None, verbose)

            counter = (counter + 1) % 2

        print("SUCCESS-COMMIT OBJECT")
        return carry_obj
    else:
        return None


def read_obj(path, verbose=False):

    if path[-3:].upper() == "OBJ":
        print("READING-FILE")
        carry_obj = GD.GraphicalObject()
        read_buffer = open(path, 'r')

        point_list = []
        edge_list = []
        for line in read_buffer:
            if line[0:2] == "v ":
                if verbose:
                    print("Point-OBJ")
                    print([float(i) for i in line[2:].split(" ")])
                else:
                    pass
                point_list.append([float(i) for i in line[2:].split(" ")])
            if line[0:2] == "f ":
                edge_points = []
                for i in line[2:].split(" "):
                    edge_points.append([int(j) - 1 for j in i.split("/")][0])

                edge_list = edge_list + generate_dupla(edge_points)

                if verbose:
                    print("Edge-OBJ")
                    print(edge_points)
                else:
                    pass

        for edge in edge_list:
            carry_obj.push_edge(GD.Point(point_list[edge[0]][0], point_list[edge[0]][1], point_list[edge[0]][2]),
                                GD.Point(point_list[edge[1]][0], point_list[edge[1]][1], point_list[edge[1]][2]),
                                None, None, verbose)
        print("SUCCESS-COMMIT OBJECT")

        return carry_obj
    else:
        return None


class EntityManger:
    def __init__(self):
        self.entityList = []

    def readFile(self, path):
        output_object = GS.GraphicalObject()

        read_carry = open(path, 'r')

        is_obj = False
        is_model = False
        active_edge = False
        edge_control = 0

        for line in read_carry:
            line = line[:-1]
            print(line)

            if line[0:2] == "#!":
                if line[2:] == "OBJ":
                    print("OBJ-FILE")
                    is_obj = True
                elif line[2:] == "MDL":
                    print("MDL-FILE")
                    is_model = True
                else:
                    return None
            else:
                pass

            if is_obj:
                if line[0:2] == "N#":
                    print("SETTING NAME \t" + line[2:])
                    output_object.set_name(line[2:])
                else:
                    pass

                if line[0:2] == "E#":
                    print("NEW EDGE - PIPE OPEN")
                    carry_point_1 = GS.Point()
                    carry_point_2 = GS.Point()
                    carry_color = GS.Color()
                    edge_control = 0
                    active_edge = True
                else:
                    pass

                if edge_control < 4 and active_edge:
                    if edge_control == 1:
                        print("PIPE - COLOR")
                        carry_color.set_color([float(i) for i in line[2:].split("\t")])
                    elif edge_control == 2:
                        print("PIPE - FirstPoint")
                        carry_point_1.set_coords([float(i) for i in line[2:].split("\t")])
                    elif edge_control == 3:
                        print("PIPE - SecondPoint")
                        carry_point_2.set_coords([float(i) for i in line[2:].split("\t")])
                        output_object.push_edge(carry_point_1, carry_point_2, carry_color, None, True)
                    else:
                        pass
                else:
                    pass

                edge_control += 1

            elif is_model:
                pass

            else:
                pass

        self.entityList.append(output_object)

        return output_object
