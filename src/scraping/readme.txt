Files here deal with the one-time process of scraping allrecipes.com for recipes and storing them in a CSV database.

RecipeScraper.py is used to scrape an individual recipe. It contains all the functions needed to scrape various pieces of info, such as the recipe title, author, etc. The file itself is never run individually, instead other pieces of code import it as a scraper object to do the scraping.

The Recipe_Links_Collector.ipybn is a Python notebook that's used to collect links to scrape recipes from. It self scrapes allrecipes, but only for recipe links, not info related to recipes. In short, it visits the Recipes A-Z page, collects the link for each category's page, visits each category's page, and scrapes 21 links from each. These links are further filtered so that only recipe links (containing '/recipe/' in its URL) are kept, as well as filtering out duplicate links.

Finally, the Full_Scraper.ipybn notebook takes the links generated from the previous notebook as a CSV file and visits each link, using RecipeScraper.py to create a scraper object, scrape the recipes info, and create a row for the recipe in a dataframe. The entire dataframe later gets converted to a CSV.

To run Full_Scraper.ipybn, it's important to have both RecipeScraper.py and the CSV of URLs in the session storage. One thing to note is that while this notebook can scrape all the recipe links in the CSV in theory, in practice, we've reduced it to 300 both to reduce scraping time.
