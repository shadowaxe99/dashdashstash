from SkillManager import SkillManager
from Skill import Skill

if __name__ == '__main__':
    skill_manager = SkillManager()

    skill1 = Skill(1, 'Programming', 'Ability to write code')
    skill2 = Skill(2, 'Problem Solving', 'Ability to solve complex problems')
    skill3 = Skill(3, 'Communication', 'Ability to effectively communicate')

    skill_manager.add_skill(skill1)
    skill_manager.add_skill(skill2)
    skill_manager.add_skill(skill3)

    print(skill_manager.list_skills())