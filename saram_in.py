import requests
from bs4 import BeautifulSoup


def extract_jobs(url):
    jobs = []
    results = requests.get(url)  # page+1로 변경해주기
    soup = BeautifulSoup(results.text, "html.parser")
    posts = soup.find_all("div", {"class": "item_recruit"})
    for post in posts:
        job = extract_job(post)
        jobs.append(job)
    return jobs


def extract_job(html):
    title_info = html.find(
        "h2", {"class": "job_tit"})
    title = title_info.a["title"]
    apply_link = title_info.a["href"]
    company = html.find("div", {"class": "area_corp"}
                        ).find("strong", {"class": "corp_name"}).a["title"]

    return {"title": title, "company": company, "apply_link": f"https://www.saramin.co.kr{apply_link}"}


def saramIn_get_jobs():
    url = "https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=react"
    jobs = extract_jobs(url)
    return jobs
