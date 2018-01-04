from libg2f import OBJobject_manager as OBJM
from libg2f import Morphing as MO

young = OBJM.read_obj("./proyect-models/young.obj")
kid = OBJM.read_obj("./proyect-models/kid.obj")

x = MO.advance_relate_objects(young, kid, 32, True)

print(len(x))