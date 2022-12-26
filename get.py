import requests
import os

API_KEY = os.environ["API_KEY"]

headers = {
    'Authorization': f"bearer {API_KEY}",
}
query = """
query {
    user(login: "aadittambe") {
    name
    contributionsCollection {
        contributionCalendar {
        colors
        totalContributions
        weeks {
            contributionDays {
            color
            contributionCount
            date
            weekday
            }
            firstDay
        }
        }
    }
    }
    }
"""

req = requests.post(
    'https://api.github.com/graphql',
    json={
        'query': query
    },
    headers=headers
)


with open('contribs.json', 'w') as f:
    f.write(req.text)
