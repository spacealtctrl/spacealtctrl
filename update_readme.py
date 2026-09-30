import re
import requests

# Get GitHub stats
try:
    repos = requests.get('https://api.github.com/users/spacealtctrl/repos?per_page=100').json()
    stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    forks = sum(repo.get('forks_count', 0) for repo in repos)
except:
    stars = 194
    forks = 10

stats_html = f"""
  <p align="center">
    <a href="https://github.com/spacealtctrl">
      <img src="https://img.shields.io/badge/Total%20Stars-{stars}-7afcff?style=flat-square&logo=github&logoColor=black" alt="Profile Stars" />
    </a>
    <a href="https://github.com/spacealtctrl">
      <img src="https://img.shields.io/badge/Total%20Forks-{forks}-7afcff?style=flat-square&logo=github&logoColor=black" alt="Profile Forks" />
    </a>
  </p>
"""

with open('README.md', 'r') as file:
    readme = file.read()

new_readme = re.sub(
    r'(?<=<!-- START_STATS -->\n).*?(?=\n<!-- END_STATS -->)',
    stats_html.strip() + '\n',
    readme,
    flags=re.DOTALL
)

with open('README.md', 'w') as file:
    file.write(new_readme)
