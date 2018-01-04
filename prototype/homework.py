#! /usr/bin/python3.5

import copy
import os

import graph_data_struct as gs

"""
p1 = Point(5,5,5)

print("Angulo respecto a X - Rad: \t", p1.angle_x() , " - Angulo respecto a Z - Seg", to_seg(p1.angle_z()), "Norma:\t", p1.norm())

v1 = edge(Point(0,0,0), Point(5,5,5))

print ("Angulo respecto a X: \t", v1.angle_x(), " - Angulo respecto a Z - Seg", to_seg(v1.angle_z()), "Norma:\t", v1.norm())
"""




ref_value = 4.3

blanco = gs.Color(1.0, 1.0, 1.0)
rojo = gs.Color(1.0, 0.0, 0.0)
verde = gs.Color(0.0, 1.0, 0.0)
azul = gs.Color(0.0, 0.0, 1.0)

p1 = gs.Point(ref_value, ref_value, ref_value)
p2 = gs.Point(0.0, 0.0, 0.0)
p3 = gs.Point(0.0, ref_value, 0.0)
p4 = gs.Point(0.0, ref_value, ref_value)

tetaedro = gs.GraphicalObject()
tetaedro.set_name("tetraedro")

tetaedro.push_edge(p1, p2, rojo)
tetaedro.push_edge(p1, p3, rojo)
tetaedro.push_edge(p1, p4, rojo)
tetaedro.push_edge(p2, p3, azul)
tetaedro.push_edge(p2, p4, azul)
tetaedro.push_edge(p3, p4, azul)

tetaedro.show_points()
tetaedro.show_edges()


t1 = gs.Point(ref_value, ref_value, 0)
t2 = gs.Point(ref_value, 0, 0)
t3 = gs.Point(0, ref_value, 0)

triangle = gs.GraphicalObject()

triangle.push_edge(t1, t2, verde)
triangle.push_edge(t1, t3, verde)
triangle.push_edge(t2, t3, verde)

triangle.show_points()
triangle.show_edges()
triangle.set_name("Triangulo")



def control(list_of_objects):

    os.system("clear")

    print("LISTA DE OBJETOS DIBUJADOS\n\n")
    index = 0
    for graph_object in list_of_objects:
        print(graph_object.get_color_name(), " \t Indice[", index, "]\n")
        index += 1

    index = input("Opcion >>>:\t")

    try:
        index = int(index)

        if index >= len(list_of_objects):
            return None
        else:
            pass
    except:
        return None

    who_object = list_of_objects[index]

    option = input("""
        [1]Rotar - Sobre si mismo
        [2]Rotar - Respecto a un Vector
        [3]Escalar
        [4]Trasladar
        """)

    try:
        option = int(option)
    except:
        return None

    if option == 1:
        option = input("""
            [1]X
            [2]Y
            [3]Z
            """)
        try:
            option = int(option)
        except:
            return None

        who_object.update_center()
        ref_center = copy.copy(who_object.get_center())

        angle = input("Angulo >>>:\t")

        try:
            angle = float(angle)
        except:
            return None

        if option == 1:
            who_object.translate()
            who_object.rotate(angle, "x", True)
            who_object.translate(ref_center)
        elif option == 2:
            who_object.translate()
            who_object.rotate(angle, "y", True)
            who_object.translate(ref_center)
        elif option == 3:
            who_object.translate()
            who_object.rotate(angle, "z", True)
            who_object.translate(ref_center)
        else:
            return None

    elif option == 2:
        option = input("""
            [1]X
            [2]Y
            [3]Z
            [4]Otro
            """)
        try:
            option = int(option)
        except:
            return None

        angle = input("Angulo >>>:\t")

        try:
            angle = float(angle)
        except:
            return None

        if option == 1:
            who_object.rotate(angle, "x", True)
        elif option == 2:
            who_object.rotate(angle, "y", True)
        elif option == 3:
            who_object.rotate(angle, "z", True)
        elif option == 4:
            vector = eval(input("Vector >>>:\t"))
            try:
                vector[0]
            except:
                return None

            who_object.rotate(angle, vector)

        else:
            return None

    elif option == 3:
        escala = eval(input("Escala >>>:\t"))
        try:
            escala = list(escala)
        except:
            return None

        who_object.scale(None,escala)
    elif option == 4:
        to_point = eval(input("Punto >>>:\t"))
        try:
            to_point == list(to_point)
        except:
            return None

        who_object.translate(gs.Point(to_point[0], to_point[1], to_point[2]))
    else:
        return None
