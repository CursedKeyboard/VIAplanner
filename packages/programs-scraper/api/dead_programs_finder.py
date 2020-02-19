import requests
from bs4 import BeautifulSoup
from typing import Tuple
from tqdm import tqdm # progress bar magic 


# test if a subject is no longer offered
def subject_exist(url: str) -> bool:
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    exist = soup.find('div', class_='centralpos').find('div', class_='contentpos').find(
        'dl', class_='title2')  # if the there are any program advisors
    return exist is not None

# finds all the subject ids
def all_subject_ids(url: str) -> Tuple[int]:
    ids = []
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    subject_groups = soup.find('div', class_='centralpos').find(
        'div', class_='contentpos').find_all('div', class_='normaltext')[1].find_all('ul')

    for subject_group in subject_groups:
        for subject in subject_group.find_all('li'):
            subject_id = int(subject.a['href'].split('=')[1])
            ids.append(subject_id)
    return tuple(ids)


ids = all_subject_ids("https://student.utm.utoronto.ca/calendar//program_list.pl")

file = open("dead_programs.txt", 'w')
for subject_id in tqdm(ids):
    url = "https://student.utm.utoronto.ca/calendar//program_group.pl?Group_Id=" + str(subject_id)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    all_degrees = ["HBA", "HBSc", "BBA", "BCom"]
    title = soup.find('p', class_='titlestyle')

    if not subject_exist(url):
        file.write(title.text.split(' (')[0] + '\n')
    

file.close();