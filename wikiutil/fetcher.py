import requests
import json
from model.wikipediapage import WikipediaPage

GET = "GET"
SUMMARY_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"
SEARCH_API_URL = "https://en.wikipedia.org/w/api.php?origin=*&action=opensearch&search="

class Fetcher():
    def fetch(self, query: str) -> WikipediaPage:
        most_relevant_result = self.get_most_relevant_result(query)
        if most_relevant_result:
            page_details = self.get_page_details(self.process_query(most_relevant_result))
            page_dict : dict = json.loads(page_details)

            title = page_dict.get('title')
            url = page_dict.get('content_urls').get('desktop').get('page')
            summary = page_dict.get('extract')
            description = page_dict.get('description')
            thumbnail_url = page_dict.get('thumbnail').get('source') if 'thumbnail' in page_dict else None
            image_url = page_dict.get('originalimage').get('source') if 'originalimage' in page_dict else None

            return WikipediaPage(title, url, summary, description, thumbnail_url, image_url)
        return None

    def get_page_details(self, query: str):
        fetch_url = f"{SUMMARY_API_URL}{self.process_query(query)}"

        try:
            page_content = requests.request(GET, fetch_url).content
            return page_content
        except Exception as e:
            print(e)

    def get_most_relevant_result(self, query: str):
        s_url = f"{SEARCH_API_URL}{self.process_query(query)}"
        res = requests.request(GET, s_url).content
        par_res = json.loads(res)
        if par_res[1]:
            return par_res[1][0]
        return None

    def process_query(self, query: str):
        return query.replace(" ", "_")
