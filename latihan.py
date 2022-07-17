import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print("-----------------------------------------------------------")
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

designer =  results.find_all(
    "h2", string=lambda text: "designer" in text.lower()
)
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    print(title_element.text.strip())
    print( )

print("designer total job = ", end=" ")
print(len(designer)) 


