import interative_agent_raw as ir
import numpy as np
from pysc2.lib import actions, features,units

def get_my_units_by_type(unit_type):
    return [unit for unit in ir.obs.observation.raw_units
            if unit.unit_type == unit_type 
            and unit.alliance == features.PlayerRelative.SELF]

def get_distances(units, xy):
    units_xy = [(unit.x, unit.y) for unit in units]
    return np.linalg.norm(np.array(units_xy) - np.array(xy), axis=1)

def get_unit_by_tag(tag):
    units= [unit for unit in ir.obs.observation.raw_units if unit.tag==tag]
    if(len(units)>0):return units[0]
    return None
