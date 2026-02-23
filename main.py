# https://www.bankersadda.com/

from packages import scrape_bankersadda

save_result= True

if __name__ == "__main__":
    
    # for current date

    # result = scrape_bankersadda(save_result=save_result)
    # result = scrape_bankersadda(date=None, month=None, year=None, save_result=save_result)

    # for user defined date
    
    user_date="16"
    user_month="february"
    user_year="2026"
    
    scrape_bankersadda(date=user_date, month=user_month, year=user_year, save_result=save_result)

    
    # print(result["data"])
    # for title in result["data"]:
    #     print(f"\n{title}")
    #     print(len(result["data"][title]))