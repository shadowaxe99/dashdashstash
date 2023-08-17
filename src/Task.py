class Task:
    def __init__(self, id, agent_id, description):
        self.id = id
        self.agent_id = agent_id
        self.description = description

    def get_id(self):
        return self.id

    def get_agent_id(self):
        return self.agent_id

    def get_description(self):
        return self.description