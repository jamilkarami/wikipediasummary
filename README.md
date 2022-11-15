# Wikipedia Summary

A small utility package I wrote for a side-project for fetching summaries of Wikipedia pages.

## Usage

```
from wikipedia_summary import WikipediaSummary
wiki = WikipediaSummary()
wiki.get_summary("Eindhoven")

>>> wiki.url
https://en.wikipedia.org/wiki/Eindhoven
>>> wiki.thumbnail_url
https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Lichttoren_Eindhoven_1_-_Cropped.jpg/320px-Lichttoren_Eindhoven_1_-_Cropped.jpg
>>> wiki.summary
Eindhoven is a city and municipality in the Netherlands, located in the southern province of North Brabant of which it is its largest. With a population of 238,326 on 1 January 2022, it is the fifth-largest city of the Netherlands and the largest outside the Randstad conurbation.
```