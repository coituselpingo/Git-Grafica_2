
def Relate_Objects(ref_object_1, ref_object_2, verbose=False):
    base_point_list = ref_object_1.point_set_collection
    objective_point_list = ref_object_2.point_set_collection

    relational_list = []

    base_index = 0
    for base_ref in base_point_list:
        maximun = 1000000000
        objective_index = 0

        for objective_ref in objective_point_list:
            dist = base_ref.norm(objective_ref)
            if dist <= maximun and not objective_ref.get_queried_state():
                objective_index = objective_ref.get_point_name()
                maximun = dist
        objective_point_list[objective_index].set_queried_state(True)
        relational_list.append([base_index, objective_index])

        base_index += 1

    if verbose:
        print(relational_list)
    else:
        pass

    carry = 0
    for i in relational_list:
        print(i)
        carry += i[1]

    if carry == ((len(relational_list) * (len(relational_list) - 1) ) / 2):
        print("TAKE ALL")

    return relational_list