from irlc import Agent

class FixedPuppetAgent(Agent):
    actions = None

    def __init__(self, agent, actions):
        self.agent = agent
        self.actions = actions

    def pi(self, s, k, info=None):
        a = self.actions[k]
        self.agent.pi(s,k,info)
        return a

    def train(self, *args, **kwargs):
        self.agent.train(*args, **kwargs)

    def __getattr__(self, name):
        return getattr(self.agent, name)


class PuppetAgent(Agent):
    def __init__(self, trainer, actor):
        self.trainer = trainer
        self.actor = actor

    def pi(self, s, k, info=None):
        self.trainer.pi(s, k, info) # We let it act to set values and generally think it is doing something normal.
        return self.actor.pi(s, k)

    def train(self, *args, **kwargs):
        self.trainer.train(*args, **kwargs)

    def __getattr__(self, name):
        a = 234
        return getattr(self.trainer, name)

