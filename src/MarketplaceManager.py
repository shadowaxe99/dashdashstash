class MarketplaceManager:

    def __init__(self):
        self.jobs = []
        self.agents = []

    def post_job(self, job):
        self.jobs.append(job)
        print('Job posted successfully.')

    def delete_job(self, job):
        self.jobs.remove(job)
        print('Job deleted successfully.')

    def update_job(self, job):
        for i in range(len(self.jobs)):
            if self.jobs[i].id == job.id:
                self.jobs[i] = job
                print('Job updated successfully.')
                break

    def get_job(self, job_id):
        for job in self.jobs:
            if job.id == job_id:
                return job
        return None

    def register_agent(self, agent):
        self.agents.append(agent)
        print('Agent registered successfully.')

    def unregister_agent(self, agent):
        self.agents.remove(agent)
        print('Agent unregistered successfully.')