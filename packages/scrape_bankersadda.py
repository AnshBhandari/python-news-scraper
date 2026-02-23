import requests
from bs4 import BeautifulSoup, Tag

from packages.current_date import date as current_date, month as current_month, year as current_year
from packages.current_date import ordinal, normalize_date
from packages.save_to_file import save_to_file


def scrape_bankersadda(date=None, month=None, year=None, save_result=False):
    if date is None or month is None or year is None:
        date, month, year = current_date, current_month, current_year
        print(f"Using current date: {date} {month} {year}")
    else:
        date = normalize_date(date)
        month = month.strip().lower()
        year = str(year).strip()
        
        print(f"Using provided date: {date} {month} {year}")

    print(f"Scraping data for {date} {month} {year}...")

    url=f"https://www.bankersadda.com/daily-current-affairs-and-gk-updates-{date}-{month}-{year}/"

    response=requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        res={"data": None, "message":  "Failed to retrieve the webpage.",  "status_code": response.status_code}
    
    else:
        html_content=response.content
        
        soup=BeautifulSoup(html_content,'html.parser')
        
        data={}
        for h2 in soup.find_all('h2', class_='text-text-100'):
            title = h2.get_text(strip=True)
            ul= h2.find_next_sibling("ul")
            if ul:
                if isinstance(ul, Tag):
                    data[title] = [li.get_text(strip=True) for li in ul.find_all("li")]

        print(f"Data scraped successfully for {date} {month} {year}.")

        # return {"data": data, "message": "Data retrieved successfully.", "status_code": response.status_code}
        res = {"data": data, "message": "Data retrieved successfully.", "status_code": response.status_code}
    
    if save_result:
        save_to_file(res, date, month, year)
        