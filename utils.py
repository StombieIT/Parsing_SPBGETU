from requests import get
from random import choice

with open('USER_AGENTS.txt') as f:
    USER_AGENTS = [user_agent[:-1] for user_agent in f.readlines()]

def url_open(url):
    return get(url, headers={'user-agent': choice(USER_AGENTS)}).text
