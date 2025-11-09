import re
from bs4 import BeautifulSoup
import requests
page = requests.get('https://internshala.com/internships/work-from-home-python-django,web-development-internships').text
soup = BeautifulSoup(page, 'lxml')
internships = soup.find_all('div', class_ = 'internship_meta duration_meta')
for internship in internships:
    internship_title = internship.find('a', class_ = 'job-title-href').text
    if ("Web") in internship_title:
        comp_name = internship.img['alt']
        date_posted = internship.find('div', class_ = re.compile('status')).text
        more_info = internship.h3.a['href']
        skills_ = internship.find_all('div', class_ ='job_skill')
        print(f'Company Name:    {comp_name}')
        print(f'Title:           {internship_title}')
        print(f'Skills Required:',end=" ")
        for skills in skills_:
            skill = skills.text
            print(skill,end=',')
        print('')
        print(f'Date posted:     {date_posted}')
        print(f'More Info:       https://internshala.com{more_info}')
        print(f' ')