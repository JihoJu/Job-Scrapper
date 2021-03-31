from job_korea import jobKorea_get_jobs
from saram_in import saramIn_get_jobs


def get_jobs(word):
    jobKorea_jobs = jobKorea_get_jobs(word)
    saramIn_jobs = saramIn_get_jobs(word)

    jobs = jobKorea_jobs + saramIn_jobs

    return jobs
