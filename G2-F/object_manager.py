import graph_data_struct as GS

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


m = EntityManger()

m.readFile("./tetraedro.tpg")