import csv

import requests
from bs4 import BeautifulSoup

date = input("Enter date: ")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#days")
def main(page):
    """This function will get the data from the website and save it in a csv file"""
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    match_date = []
    championships = soup.find_all("div", {'class':'matchCard'})
    def get_match_data(championships):
        """This function will get the match data"""
        championship_tile = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("li")
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            # get teams names
            team_a = all_matches[i].find("div", {'class':'teamA'}).text.strip()
            team_b = all_matches[i].find("div", {'class':'teamB'}).text.strip()
            # get teams scores
            results = all_matches[i].find("div", {'class':'MResult'}).find_all("span",{'class':'score'})
            score = f"{results[0].text.strip()} - {results[1].text.strip()}"
            print(team_a, team_b , score)
    get_match_data(championships[0])
main(page)
