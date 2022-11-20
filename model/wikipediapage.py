
class WikipediaPage():
    title : str
    url: str
    summary: str
    description : str
    thumbnail_url : str
    image_url : str

    # title, url, summary, description, thumbnail_url, image_url
    def __init__(self, title: str, url : str, summary : str, description: str, thumbnail_url : str, image_url: str) -> None:
        self.title = title
        self.url = url
        self.summary = summary
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.image_url = image_url