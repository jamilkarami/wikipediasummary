class WikipediaPage:

    def __init__(
        self, title: str, url: str, summary: str, description: str,
        thumbnail_url: str, image_url: str,
    ) -> None:
        """
        Class to represent a wikipedia page details summary.

        ...

        Attributes
        ----------
        title : str
            full title of the wikipedia page
        url : str
            url of the page
        summary : str
            short summary of the page (e.g. "Singer from the Netherlands")
        description: str
            fleshed-out summary with more details
        thumbnail_url: str
            url that points to the thumbnail image of the page
        image_url: str
            url that points to the full size image of the page
        """
        self.title = title
        self.url = url
        self.summary = summary
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.image_url = image_url
