from pysc2.agents import base_agent
from pysc2.env import sc2_env
from pysc2.lib import actions, features,units
from absl import app
import threading

# we need two locks; when either is locked, indicate obs, or action are not ready
obs_lock=threading.Lock()
action_lock=threading.Lock()
obs=None
action=None
#  func : obs->action
def run_one_step(func):
    global obs,action
    obs_lock.acquire()
    print("get new observation!")
    action=func(obs)
    if(action_lock.locked()):action_lock.release()

def no_action(obs):
    return actions.FUNCTIONS.no_op()

class InteractiveAgent(base_agent.BaseAgent):
    def step(self, obs_):
        global obs,action
        super(InteractiveAgent, self).step(obs_)
        obs=obs_
        if(obs_lock.locked()):obs_lock.release()
        action_lock.acquire()
        print("get corresponding action")
        return action


def start_game(unused_argv):
  agent = InteractiveAgent()
  try:
    while True:
      with sc2_env.SC2Env(
          map_name="Simple64",
          players=[sc2_env.Agent(sc2_env.Race.terran),
                   sc2_env.Bot(sc2_env.Race.random,
                               sc2_env.Difficulty.very_easy)],
          agent_interface_format=features.AgentInterfaceFormat(
              feature_dimensions=features.Dimensions(screen=84, minimap=64),
              use_feature_units=True,
              # use_raw_units=True,
              # use_raw_actions=True
          ),
          step_mul=16,
          game_steps_per_episode=0,
          visualize=True) as env:
          
        agent.setup(env.observation_spec(), env.action_spec())
        
        timesteps = env.reset()
        agent.reset()
        
        while True:
          step_actions = [agent.step(timesteps[0])]
          if timesteps[0].last():
            break
          timesteps = env.step(step_actions)
      
  except KeyboardInterrupt:
    pass
  

class App(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func=func
    def run(self):
        if(not obs_lock.locked()):
            obs_lock.acquire()
        if(not action_lock.locked()):
            action_lock.acquire()
        app.run(self.func)
        

game=App(start_game)
