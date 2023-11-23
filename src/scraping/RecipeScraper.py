import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import re

# This scraper is specifically designed to scrape recipes from allrecipes.com

class RecipeScraper():
  # Constructor initiates instatance by parsing the html of the recipe's page
  def __init__(self, url):
    self.url = url 
    self.soup = BeautifulSoup(requests.get(url).content, 'html.parser')

  # Every method from here will try to extract certain key info from parsed html, otherwise return NaN

  # Extract the recipe's title
  def get_recipe_title(self):
    try:
      return self.soup.find('h1', {'id': 'article-heading_1-0'}).text.strip()
    except:
      return np.nan

  # Extract list of ingredients
  def get_recipe_ingredients(self):
    try:
      ingredients = []
      # Loop through array of li elements to get entire ingredient content
      for li in self.soup.select('.mntl-structured-ingredients__list-item'):
        ingred = ' '.join(li.text.split())
        ingredients.append(ingred)
      return ingredients
    except:
      return np.nan

  # Extract the description
  def get_recipe_description(self):
    try:
      return self.soup.find('p', {'id': 'article-subheading_1-0'}).text.strip()
    except:
      return np.nan

  # Extract author name
  def get_recipe_author(self):
    try:
      return self.soup.select_one('.mntl-attribution__item-name').text.strip()
    except:
      return np.nan

  # Extract rating
  def get_recipe_rating(self):
    try:
      return self.soup.find('div', {'id': 'mntl-recipe-review-bar__rating_1-0'}).text.strip()
    except:
      return np.nan

  # Extract the date (publication or last updated)
  def get_recipe_date(self):
    try:
      recipe_date = self.soup.find('div', {'class': 'mntl-attribution__item-date'}).text.strip()

      # Allrecipes date format: "Published on [Month Day, Year]
      # Need to extract only the date portion
      months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
      
      # Loop through list of months and strip everything from month word onwards
      for month in months:
        if month in recipe_date:
          recipe_date = recipe_date[recipe_date.index(month):]
      return recipe_date
    except:
      return np.nan

  # Extract recipe instructions
  def get_recipe_instructions(self):
    try:
      steps = []
      # Loop through array of p elements to get every step involved in recipe
      for step in self.soup.find_all('p', {'class': 'comp mntl-sc-block mntl-sc-block-html'}):
          s = ' '.join(step.text.split())
          steps.append(s)
      return steps
    except:
      return np.nan

  # Extract basic nutrition facts (cals, carbs, fat, protein)
  def get_recipe_nutrition(self):
    try:
      # Nutrition facts displayed in a table
      # Every column is a nutrient (header on bottom)
      nutrition_summary = self.soup.find('table', {'class': 'mntl-nutrition-facts-summary__table'})
      summary_items = []

      # Loop through every table cell to get cell content
      # Loop traverses down each column from left to right
      # Resulting Array: ["###", "label1", "###", "label2", ...]
      for td in self.soup.select('.mntl-nutrition-facts-summary__table-cell'):
        summary_items.append(td.text.strip())
      
      calories = None
      fat = None
      carbs = None
      protein = None

      # Loop through every item in the summary array and extract only nutrient values 
      # (store to individual variables)
      i = 1
      for i in range(len(summary_items)):
        match summary_items[i]:
          case "Calories":
            calories = summary_items[i-1]
          case "Fat":
            fat = summary_items[i-1]
          case "Carbs":
            carbs = summary_items[i-1]
          case "Protein":
            protein = summary_items[i-1]
        i += 1
      return [calories, fat, carbs, protein]
    except:
      return np.nan

  # Extract summary information (cooking times and servings)
  def get_recipe_summary(self):
    try:
      # Summary info displayed in a table much like nutrients
      # Must follow a similar process to extract summary information
      recipe_details = self.soup.find('div', {'class': 'mntl-recipe-details__content'})
      detail_items = []
      for div in self.soup.find_all('div', {'class': ['mntl-recipe-details__label', 'mntl-recipe-details__value']}):
        detail_items.append(div.text.strip())
      prep_time = None
      cook_time = None
      total_time = None
      servings = None
      i = 0
      for i in range(len(detail_items)):
        match detail_items[i]:
          case "Prep Time:":
            prep_time = detail_items[i+1]
          case "Cook Time:":
            cook_time = detail_items[i+1]
          case "Total Time:":
            total_time = detail_items[i+1]
          case "Servings:":
            servings = detail_items[i+1]
        i += 1
      return [prep_time, cook_time, total_time, servings]
    except:
      return np.nan



  
