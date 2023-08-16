class Subscription:
    def __init__(self, plan, price, max_agents):
        self.plan = plan
        self.price = price
        self.max_agents = max_agents

    def get_plan(self):
        return self.plan

    def get_price(self):
        return self.price

    def get_max_agents(self):
        return self.max_agents


if __name__ == '__main__':
    subscription = Subscription('Premium', 9.99, 6)
    print('Plan:', subscription.get_plan())
    print('Price:', subscription.get_price())
    print('Max Agents:', subscription.get_max_agents())