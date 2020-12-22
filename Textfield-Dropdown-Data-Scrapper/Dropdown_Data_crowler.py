'''
    This Module scrappes all the data from make form from the
    premium page of the webpage https://www.boattrader.com/sell/
'''
import csv
from selenium import webdriver

def goto_premium():
    '''
        This fumction clicks over select button of premium section,
        to nevigate over the premium page.
    '''
    driver.find_element_by_id("sm-package.premium").click()

def get_combination():
    '''
        This function creates all the possible combination from a to z
        for single and double charecter word.
    '''
    combination = []
    for i in range(97,123):
        combination.append(chr(i))
    for i in range(97,123):
        for j in range(97,123):
            combination.append(chr(i)+chr(j))
    return list(set(combination))

def make_scrapper():
    '''
        This function all dropdowd data from make form.
    '''
    main_data = []
    counter = 0
    for i in combinations:
        driver.find_element_by_id("make").send_keys(i)
        datas = driver.find_elements_by_xpath("//*[@class='typeahead dropdown-menu']\
            /descendant::li")
        for data in datas:
            main_data.append(data.get_attribute("data-value"))
        counter += 1
        print("Number of keys searched %d out of %d"%(counter,len(combinations)))
        driver.find_element_by_id("make").clear()
    return list(set(main_data))

def push_into_csv():
    '''
        This function pushes all the scrapped data into data.csv
    '''
    for row in scrapped_datas:
        temp = [row]
        with open("data.csv", 'a', newline='') as file:
            writedata = csv.writer(file)
            writedata.writerow(temp)
        temp = []

# Driver code
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.boattrader.com/sell/")
    goto_premium()
    combinations = get_combination()
    print("Total number of keyes : ",len(combinations))
    scrapped_datas = make_scrapper()
    push_into_csv()
    driver.quit()
