import typer
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random
from datetime import datetime, timedelta,date
import string
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os.path
import time
from typing_extensions import Annotated
from rich.progress import track
from rich.progress import Progress
app = typer.Typer()

def read_words(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def generate_password(words):
    word1 = random.choice(words)
    word2 = random.choice(words)
    return f"{word1}.{word2}"

def generate_email(words, first_name, last_name):
    domain = random.choice(words)
    return f"{first_name}.{last_name}@{domain}.com"


def genDate():
    month = datetime.now().month + 1
    year = random.randint(datetime.now().year - 30, datetime.now().year - 18) 
    start_date = date(year, month, 1)  
    end_date = start_date.replace(day=28) + timedelta(days=4)  
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date
def genPhone():
    
    return '780'+ "".join(random.choices(string.digits, k=7))


words = read_words("opagen/words.txt")
@app.command()
def main(accounts: Annotated[int, typer.Argument()] = "1"):
        for x in track(range(accounts),description="Processing..."):
            firstnameGen = random.choice(words)
            lastnameGen = random.choice(words)
            emailGen = generate_email(words, firstnameGen, lastnameGen)
            passwordGen = generate_password(words)
            birthdayGen = genDate()
            phoneGen =  genPhone()


            driver = uc.Chrome(headless=True,use_subprocess=False)
            driver.get('https://opa.orderexperience.net/register')
            title = driver.title

            driver.implicitly_wait(1)
            opt_in = driver.find_element(by=By.CLASS_NAME, value="custom-control-label")
            first_name = driver.find_element(by=By.ID, value="__BVID__109")
            last_name = driver.find_element(by=By.ID, value="__BVID__111")
            phone = driver.find_element(by=By.ID, value="__BVID__113")
            birthday = driver.find_element(by=By.ID, value="__BVID__115")
            email = driver.find_element(by=By.ID, value="__BVID__117")
            password = driver.find_element(by=By.ID, value="__BVID__120")
            location = driver.find_element(by=By.ID, value="__BVID__122")
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")

            opt_in.click()
            first_name.send_keys(firstnameGen)
    
            last_name.send_keys(lastnameGen)
            
            phone.send_keys(phoneGen)
            
            birthday.send_keys(birthdayGen.strftime('%m%d%Y'))

            email.send_keys(emailGen)
            
            password.send_keys(passwordGen)
            location.send_keys('a')

            
            
            driver.implicitly_wait(10)
            submit_button.send_keys(Keys.ENTER)
            driver.implicitly_wait(10)


            if os.path.isfile('opaaccs.csv') == False : 
                with open('opaaccs.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    field = ["username", "password","birth month"]
                    writer.writerow(field)
                    writer.writerow([emailGen, passwordGen,birthdayGen.strftime('%B')])
            else:
                with open('opaaccs.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([emailGen, passwordGen,birthdayGen.strftime('%B')])
            time.sleep(5)
            
        
if __name__ == "__main__":
    app()
    
