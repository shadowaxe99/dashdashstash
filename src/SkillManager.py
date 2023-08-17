from Skill import Skill

class SkillManager:

    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

    def remove_skill(self, skill):
        self.skills.remove(skill)

    def get_skill(self, skill_id):
        for skill in self.skills:
            if skill.id == skill_id:
                return skill
        return None

    def list_skills(self):
        return self.skills

    def update_skill(self, skill):
        for i in range(len(self.skills)):
            if self.skills[i].id == skill.id:
                self.skills[i] = skill
                break
