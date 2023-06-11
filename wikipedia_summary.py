from wikiutil.fetcher import Fetcher


class WikipediaSummary:

    def __init__(self) -> None:
        self.fet = Fetcher()

    def get_summary(self, query: str):
        return self.fet.fetch(query)
