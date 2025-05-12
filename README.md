# 7 Spices - Django Food Ordering Web App

**7 Spices** is a colorful, beginner-friendly Django project that simulates a food ordering website. It includes a login system and pages for hotel info, menu display (veg & non-veg), and detailed nutritional information for each dish.

## Features

- User login page (username & password)
- Home page with hotel name, image, and address
- Menu page with food categorized as Veg and Non-Veg
- Nutritional page ("Healthy Kitchen") for each dish
- Colorful UI using basic CSS and JavaScript
- Navigation between all pages
- Fully functional Django routing

## Pages Overview

- `/login/` – Login page (first page)
- `/index/` – Welcome page after login (7 Spices with Home & Menu buttons)
- `/home/` – Hotel image and address
- `/menu/` – Food items displayed with image, name, and price
- `/healthy_kitchen/<dish_name>/` – Ingredients & nutritional values for the selected dish

## Tech Stack

- Python 3
- Django 4.x
- HTML5, CSS3, JavaScript
- SQLite (default Django DB)

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/7-spices-django.git
   cd 7-spices-django
