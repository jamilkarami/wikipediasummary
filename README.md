# Wikipedia Summary

A small utility package I wrote for a side-project for fetching summaries of Wikipedia pages.

## Installation

You can install the package with:
```
pip install wikipediasummary
```

## Usage
```
from wikipedia_summary import WikipediaSummary
wiki = WikipediaSummary()
eindje = wiki.get_summary("Eindhoven")

>>> eindje.url
https://en.wikipedia.org/wiki/Eindhoven
>>> eindje.thumbnail_url
https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Lichttoren_Eindhoven_1_-_Cropped.jpg/320px-Lichttoren_Eindhoven_1_-_Cropped.jpg
>>> eindje.summary
Eindhoven is a city and municipality in the Netherlands, located in the southern province of North Brabant of which it is its largest. With a population of 238,326 on 1 January 2022, it is the fifth-largest city of the Netherlands and the largest outside the Randstad conurbation.
```
