# ACME Corporation are hiring a new junior developer, as part of their hiring criteria they've created a "coding skill score" based on the specific competencies they require for this role; the more important the skill is for ACME corp, the more points it contributes to the "coding skill score" The skills are weighted as follows:
#  - Python (1)
#  - Ruby (2)
#  - Bash (4)
#  - Git (8)
#  - HTML (16)
#  - TDD (32)
#  - CSS (64)
#  - JavaScript (128)
# ​
#  Write a program that allows a user to input their skills and then tells them 
#  a) Their overall "coding skill score" 
#  b) Skills they may want to learn, and how much each one would improve their score
weighted_skills = {
    "python": 1,
    "ruby": 2,
    "bash": 4,
    "git": 8,
    "html": 16,
    "tdd": 32,
    "css": 64,
    "javascript": 128
}
def skill_score():
    print("Welcome to the Coder Skill Score")
    user_input = [input("Please Enter the skills coding skills you have \n")]
    user_skills = user_input[0].split(" ")
    
    user_score = 0
    
    print(f"Your skills are: {user_skills}")

    for key, value in weighted_skills.items():
        if key in user_skills:
            user_score = user_score + value
        else:
            continue
    print(f"Your Skill Score is: {user_score} Points\n")

    improvements = {}

    for key, value in weighted_skills.items():
        if key not in user_skills:
            improvements[key] = value
        else:
            continue

    print("To Improve your Skill Score you could learn the follow Programming lanuages")
    for key, value in improvements.items():
        print(f"{key} ':' {value} Extra Points")

skill_score()

