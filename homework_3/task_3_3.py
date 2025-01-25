import requests
from bs4 import BeautifulSoup

url_example = "https://github.com/vladze33/PythonEdutoriaHW"
session = requests.Session()
response = session.get(url_example)

try:
    soup = BeautifulSoup(response.text, features="html.parser")
    if response:
        hw3_element = soup.select("#folder-row-2.react-directory-row .react-directory-filename-cell a")[0]
        hw3_row_title = hw3_element.text
        hw3_relative_ref = hw3_element.attrs["href"]

        print("Repository title: ", soup.title.text)
        print("Homework:", f"{hw3_row_title} (href={hw3_relative_ref})")
    else:
        print("Error:", f"{response.status_code} (title={soup.title.text})")
    print("Elapsed:", response.elapsed)
except Exception as e:
    print("Caught error:", e)
