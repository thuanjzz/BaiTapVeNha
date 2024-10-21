from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re

# Tạo dataframe rỗng và dictionary
all_links = []
musician_links = []
df = pd.DataFrame({"name of the band": [], "years active": []})

# Tạo tùy chọn để chạy chế độ ẩn
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--window-size=1920x1080")

# Khởi tạo webdriver với các tùy chọn
driver = webdriver.Chrome(options=chrome_options)

# Truy cập trang web
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#A'
driver.get(url)

# Dừng khoảng 3s để trang tải xong
time.sleep(3)

try:
    # Lấy tất cả các thẻ ul trong web danh mục
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_tags))

    # Chọn ul thứ 22
    ul_musician = ul_tags[21]

    # Lấy tất cả link chứa thông tin nhạc sĩ bắt đầu bằng chữ A thuộc ul_musician
    li_tags = ul_musician.find_elements(By.TAG_NAME, "li")
    print(len(li_tags))

    # Tạo danh sách các URL
    links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
    all_links.extend(links)

except Exception as e:
    print("Error: ", e)

# Tắt trình duyệt
driver.quit()

# Kiểm tra all_links có dữ liệu chưa
print(all_links)

# Truy cập vào đường link đầu tiên của all_links
artists_driver = webdriver.Chrome(options=chrome_options)
artists_driver.get(all_links[0])

# Dừng khoảng 2s để trang tải xong
time.sleep(2)

try:
    # Lấy tất cả các thẻ ul của danh sách nghệ sĩ acid rock
    ul_artists_tags = artists_driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_artists_tags))

    # Chọn ul thứ 25
    ul_artist = ul_artists_tags[24]

    # Lấy tất cả link chứa thông tin thuộc artists
    li_artist = ul_artist.find_elements(By.TAG_NAME, "li")
    print(len(li_artist))

    # Tạo danh sách các URL của artist
    links_artist = [artist_tag.find_element(By.TAG_NAME, "a").get_attribute("href") for artist_tag in li_artist]
    musician_links.extend(links_artist)

except Exception as e:
    print("Error: ", e)

# Tắt trình duyệt
artists_driver.quit()

# Kiểm tra musician_links có dữ liệu chưa
print(musician_links)

# Lấy thông tin của các nhạc sĩ, ca sĩ
count = 0
for link in musician_links:
    if count >= 100:  # Dừng lại sau khi đã lấy thông tin cho 100 nhạc sĩ
        break
    count += 1
    print(link)

    try:
        # Khởi tạo webdriver
        driver = webdriver.Chrome(options=chrome_options)

        # Mở trang web
        driver.get(link)

        # Đợi khoảng 3s
        time.sleep(3)

        # Lấy tên ban nhạc
        try:
            name_band = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name_band = ""

        # Lấy năm hoạt động
        try:
            year_active_element = driver.find_element(By.XPATH,
                                                      '//span[contains(text(),"Years active")]/parent::*/following-sibling::td')
            year_active = year_active_element.text
        except:
            year_active = ""

        # Tạo dictionary để thêm thông tin nhạc sĩ
        musician = {'name of the band': name_band, 'years active': year_active}

        # Chuyển đổi dictionary thành dataframe
        musician_df = pd.DataFrame([musician])

        # Thêm thông tin vào df chính
        df = pd.concat([df, musician_df], ignore_index=True)

        # Đóng web
        driver.quit()

    except Exception as e:
        print("Error: ", e)

# In thông tin ra file Excel
print(df)

# Đặt tên file Excel
file_name = "musician.xlsx"

# Lưu thông tin vào file Excel
df.to_excel(file_name, index=False)
print('Chạy thành công, mời bạn mở file Excel lên!')
