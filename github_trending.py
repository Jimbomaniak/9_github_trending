import requests
import datetime


TOP_SIZE = 20
DAYS_CREATED_BEFORE = 7


def get_trending_repositories(top_size, date_created):
	url = 'https://api.github.com/search/repositories'
	payload = {
				'q': 'created:{0}'.format(date_created),
				'sort': 'stars',
				'order': 'desc'
				}
	response = requests.get(url, params=payload).json()
	return response['items'][:top_size] #"stargazers_count"


def get_start_date(days_before):
    today = datetime.date.today()
    starting_date = today - datetime.timedelta(days=DAYS_CREATED_BEFORE)
    return starting_date


def pprint_github_top(json_from_github_api):
	for num, repository in enumerate(json_from_github_api):
		print('{0}.'
			  'Stars-{stargazers_count}, '
		 	  'Open issues-{open_issues}, '
		 	  'Link-{html_url}'.format(num+1, **repository)
		 	  )


if __name__ == '__main__':
	date_created = get_start_date(DAYS_CREATED_BEFORE)
	repos = get_trending_repositories(TOP_SIZE, date_created)
	pprint_github_top(repos)
