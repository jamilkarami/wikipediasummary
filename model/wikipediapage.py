
class WikipediaPage():
    thumbnail_url : str
    summary: str
    url: str

    def __init__(self, url : str, summary : str, thumbnail_url : str) -> None:
        self.url = url
        self.summary = summary
        self.thumbnail_url = thumbnail_url