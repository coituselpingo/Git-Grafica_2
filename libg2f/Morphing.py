import multiprocessing as MP
from libg2f import OBJobject_manager as OBJM


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


def kernel_closest_pair(base_list, objetive_list, start_index, end_index, output_dict, id, verbose=False):
    relational_list = []

    for base_ref in base_list[start_index:end_index]:
        maximun = 1000000000
        objective_index = 0

        for objective_ref in objetive_list:
            dist = base_ref.norm(objective_ref)
            if dist <= maximun and not objective_ref.get_queried_state():
                objective_index = objective_ref.get_point_name()
                maximun = dist
        objetive_list[objective_index].set_queried_state(True)
        relational_list.append([base_ref.get_point_name(), objective_index])

    if verbose:
        print(len(relational_list), "\t", start_index, "\t", end_index)
    else:
        pass

    output_dict[id] = relational_list


def advance_relate_objects(ref_object_1, ref_object_2, threads=16, verbose=False):
    base_point_list = ref_object_1.point_set_collection
    objective_point_list = ref_object_2.point_set_collection

    len_base_point_list = len(base_point_list)

    index_headers_pairs = OBJM.split_range_index(len_base_point_list, threads)

    jobs = []

    manager = MP.Manager()
    output_dict = manager.dict()

    for id in range(0, threads, 1):
        p = MP.Process(target=kernel_closest_pair, args=(base_point_list, objective_point_list,
                                                         index_headers_pairs[id][0],
                                                         index_headers_pairs[id][1],
                                                         output_dict, id, verbose))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

    if verbose:
        print("ALL FINISH")
    else:
        pass

    output_point_pair_list = []
    for i in range(0, threads, 1):
        output_point_pair_list += output_dict[i]

    return output_point_pair_list


def kernel_morph_points(base_list, objetive_list, pair_list, step, start_index, end_index, output_dict, id, verbose=False):
    relational_list = []

    operations = 0
    for pair_ref in pair_list[start_index:end_index]:
        base_list[pair_ref[0]].step_to_point(objetive_list[pair_ref[1]], step)

    if verbose:
        print(operations, "\t", start_index, "\t", end_index)
    else:
        pass


def parallel_morph(ref_object_1, ref_object_2, pair_list, step, threads=16, verbose=False):
    base_point_list = ref_object_1.point_set_collection
    objective_point_list = ref_object_2.point_set_collection

    len_pair_list = len(pair_list)

    index_headers_pairs = OBJM.split_range_index(len_pair_list, threads)

    jobs = []

    for id in range(0, threads, 1):
        p = MP.Process(target=kernel_closest_pair, args=(base_point_list, objective_point_list,
                                                         pair_list, step,
                                                         index_headers_pairs[id][0],
                                                         index_headers_pairs[id][1],
                                                         verbose))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

    if verbose:
        print("ALL FINISH")
    else:
        pass