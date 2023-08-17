class AgentManager:

    def __init__(self):
        self.agents = []

    def create_agent(self, agent):
        self.agents.append(agent)
        print('Agent created successfully.')

    def delete_agent(self, agent):
        self.agents.remove(agent)
        print('Agent deleted successfully.')

    def update_agent(self, agent):
        for i in range(len(self.agents)):
            if self.agents[i].id == agent.id:
                self.agents[i] = agent
                print('Agent updated successfully.')
                break

    def get_agent(self, agent_id):
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        return None