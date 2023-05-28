
# Wikipedia API & Python Library

import wikipedia


def main():
    """Wikipedia API program that prints title, summary and URL of a page in Wikipedia"""
    search_term = None
    while search_term != "":
        search_term = input("please input a page title or search phrase:")
        if search_term != "":
            try:
                page_results = wikipedia.page(search_term, auto_suggest=False)
                print(page_results.title)
                print(page_results.summary)
                print(page_results.url)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)


main()
