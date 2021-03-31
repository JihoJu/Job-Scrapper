import requests
from bs4 import BeautifulSoup


def extract_last_page(url):
    results = requests.get(url)
    soup = BeautifulSoup(results.text, "html.parser")
    last_page = soup.find(
        "span", {"class": "pgTotal"}).get_text()

    return int(last_page)


def extract_jobs(url, last_page):
    jobs = []
    # for page in range(last_page): => 결과값 빨리 보기 위함
    results = requests.get(f"{url}&Page_No={1}")  # page+1로 변경해주기
    soup = BeautifulSoup(results.text, "html.parser")
    posts = soup.find("div", {"class": "lists-cnt"}
                      ).find_all("li", {"class": "list-post"})
    for post in posts:
        job = extract_job(post)
        jobs.append(job)
    return jobs


def extract_job(html):
    company_info = html.find(
        "div", {"class": "post-list-corp"})
    company = company_info.a["title"]
    apply_link = company_info.a["href"]
    title = html.find("div", {"class": "post-list-info"}
                      ).a.get_text(strip=True)
    return {"title": title, "company": company, "apply_link": f"https://www.jobkorea.co.kr/{apply_link}"}


def jobKorea_get_jobs():
    url = "https://www.jobkorea.co.kr/Search/?stext=react"
    last_page = extract_last_page(url)
    jobs = extract_jobs(url, last_page)
    return jobs
