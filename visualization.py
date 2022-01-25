#Name: Joseph Bobowski
#Date: 1/24/2022

#(in venv) pip install requests
import requests

#(in venv) pip install plotly
from plotly.graph_objs import bar
from plotly import offline

apiURL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
requesting = requests.get(apiURL, headers=headers)
print(f"Status code: {requesting.status_code}")

apiResponse = requesting.json()
repoResponse = apiResponse['items']
repositories, ratings = [], []

for repos in repoResponse:
    repositories.append(repos['name'])
    ratings.append(repos['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repositories,
    'y': ratings,
}]
plotLayout = {
    'title': 'Python Projects with the highest star counts on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Rating'},
}

fig = {'data': data, 'layout': plotLayout}
offline.plot(fig, filename='pythongGitRepos.html')



#BELOW WAS CODE USED TO GATHER DATA ABOUT THE REPOSITORIES AND HOW THEIR DATA WAS LAID OUT
#BELOW IS NO LONGER NEEDED TO VISUALIZE THE DATA

#print(f"Total respositories: {apiResponse['total_count']}")
#print(f"Repositories returned: {len(repoResponse)}")
#print("\nInformation about each repository:")
    #print(f"\nName: {repos['name']}")
    #print(f"Owner: {repos['owner']['login']}")
    #print(f"Stars: {repos['stargazers_count']}")
    #print(f"Repository: {repos['html_url']}")
    #print(f"Description: {repos['description']}")