import random

# Sample projects and skills
projects = [
    {"title": "Robotic Arm Control System", "description": "Developed a robotic arm control system using Arduino and Python.", "skills": ["Python", "Arduino", "Robotics"]},
    {"title": "Solar-Powered Water Pump", "description": "Designed and implemented a solar-powered water pump system for agricultural irrigation.", "skills": ["Renewable Energy", "System Design", "Project Management"]},
    {"title": "E-commerce Website Development", "description": "Built an e-commerce website from scratch using Django framework.", "skills": ["Python", "Django", "Web Development"]}
]

all_skills = ["Python", "Arduino", "Robotics", "Renewable Energy", "System Design", "Project Management", "Django", "Web Development"]

# AI-powered functions
def generate_project_highlights(projects):
    return "\n".join(f"<li>{project['title']}: {project['description']}</li>" for project in projects)

def generate_personalized_skill_recommendations(projects, all_skills):
    common_skills = {}
    for project in projects:
        for skill in project['skills']:
            common_skills[skill] = common_skills.get(skill, 0) + 1
    common_skills_sorted = sorted(common_skills.items(), key=lambda x: x[1], reverse=True)
    recommended_skills = [skill for skill, _ in common_skills_sorted[:3] if skill not in all_skills]
    return ", ".join(recommended_skills)

# Generate HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Engineering Portfolio</title>
</head>
<body>
    <h1>Engineering Portfolio</h1>
    <h2>Project Highlights:</h2>
    <ul>{generate_project_highlights(projects)}</ul>
    <h2>Recommended Skills:</h2>
    <p>{generate_personalized_skill_recommendations(projects, all_skills)}</p>
</body>
</html>
"""

# Write HTML content to a file
with open("engineering_portfolio.html", "w") as file:
    file.write(html_content)

print("Portfolio webpage generated successfully!")
