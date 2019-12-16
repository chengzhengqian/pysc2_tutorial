import interative_agent as ia
from importlib import reload as re

ia.game.start()
ia.run_one_step(ia.no_action)
fu=ia.obs.observation.feature_units
ru=ia.obs.observation.raw_units
len(fu)
len(ru)

def show_unit(u):
    return units.get_unit_type(u.unit_type) 
[units.get_unit_type(u.unit_type) for u in ru]
ia.obs.observation.__dir__()
show_unit(ia.obs.observation.single_select[0])

[  (u.x, u.y) for u in ru]
[  (show_unit(u),u.x, u.y) for u in ru]

ia.obs.observation.available_actions
ia.obs.observation.single_select
ia.obs.observation.feature_units

# for raw
from pysc2.lib import actions, features,units
from importlib import reload as re
ir=re(ir)

import interative_agent_raw as ir
ir.game.start()
for i in range(100):ir.run_one_step(ir.no_action)
ir.run_one_step(ir.no_action)
ru=ir.obs.observation.raw_units
len(ru)
[ units.get_unit_type(u.unit_type) for u in ru]
[( units.get_unit_type(u.unit_type),u.x,u.y) for u in ru]

[( units.get_unit_type(u.unit_type),u.x,u.y,features.PlayerRelative(u.alliance),u.tag) for u in ru]

ir.obs.observation.player.minerals


cc=get_my_units_by_type(units.Terran.CommandCenter)[0]
base_pos=(cc.x,cc.y)
supply_pos=(30,40)
scvs=get_my_units_by_type(units.Terran.SCV)
len(scvs)

supply=get_my_units_by_type(units.Terran.SupplyDepot)
supply=get_unit_by_tag(supply.tag)
supply.build_progress



scv_=scvs[np.argmin(get_distances(scvs,supply_pos))]
action_build_supply=actions.RAW_FUNCTIONS.Build_SupplyDepot_pt("now",scv_.tag,supply_pos)

ir.run_one_step(lambda o:action_build_supply)

ir.obs.observation.raw_units
scv_=scv_[0]
scv_=get_unit_type_by_tag(scv_.tag)[0]
scv_._index_names

scv_.build_progress
scv_.order_progress_1
scv_.ideal_harvesters
