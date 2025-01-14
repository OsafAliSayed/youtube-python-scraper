from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

def convert_subscriber_count(subscriber_count):
    subscriber_count = subscriber_count.replace(' subscribers', '')
    if 'K' in subscriber_count:
        return int(float(subscriber_count.replace('K', '')) * 1000)
    elif 'M' in subscriber_count:
        return int(float(subscriber_count.replace('M', '')) * 1000000)
    else:
        return int(subscriber_count.replace(',', ''))

search_keyword = input("Enter the search keyword: ")
try: 
    scroll_limit = int(input("Enter the number of times to scroll the page: "))
except ValueError:
    print("Please enter a valid number.")
    exit()
    
# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the YouTube search results URL
url = f"https://www.youtube.com/results?search_query={search_keyword}&sp=EgIQAg%253D%253D"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Scroll the page to load more results
scroll_count = 0
last_height = driver.execute_script("return document.documentElement.scrollHeight")


while scroll_count < scroll_limit:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    scroll_count += 1

# Locate the elements containing the channel name and subscriber count
channels = driver.find_elements(By.XPATH, '//yt-formatted-string[@id="text" and not(@has-link-only_) and not(@ellipsis-truncate)]')
subscribers = driver.find_elements(By.XPATH, '//span[@id="video-count"]')

# write channels, subscribers to a excel
df = pd.DataFrame(columns=['Channel Name', 'Subscribers'])
for channel, subscriber in zip(channels, subscribers):
    df = df._append({"Channel Name": channel.text, "Subscribers": convert_subscriber_count(subscriber.text)}, ignore_index=True)

df.to_excel(f'{search_keyword}_youtube_channels.xlsx', index=False)


# Close the WebDriver
driver.quit()