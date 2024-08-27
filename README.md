## Project name
Sparta Market Implementation of Basic Web Features

## Introduction
The Sparta Market project allows users to post transaction photos of used goods. Users can engage with posts by expressing interest through **'likes'** and **'follows'.** The project is built using Django and provides essential social interaction features.

## Development Period
- Start Date: 2024.08.20
- End Date: 2024.08.28

## Team Roles and Responsibilities
|Team Member|Responsibilities|
|:--|:--|
|운율|- Documentation (Sofware Architecture)<br>- Basic Skeleton Implementation<br>- User Profile Features(username, join_date, view registered posts, see 'Like' post, view follow & following)<br>- CSS: Detailed page Template
|이규호|- Basic Skeleton Implementation<br>- Member Features(upload a profile picture, Default profile)<br>- Product Price Setting<br>- CSS: Main home, Navigation bar|
|김석환|- Basic Skeleton Implementation<br>- Posting Features(product list page, detailed page, CRUD features, 'Like' feature)<br>- CSS: Writing page Template|
|이광욱|- Basic Skeleton Implementation<br>- Posting Features('Like' count, vistor count, sort posts by most recent/popularity)<br>- CSS: Profile page Template|


## Full Technology Stack Overview
- Programming Language: python 3.10
- Web Framework: Django 4.2
- Database: SQLite
- IDE: PyCharm, Vs code
- Version Control: Git, Github
- Communication: Zep, Notion, Slack
- Technical stack
  - Backend: Python, Django
  - Frontend: HTML, CSS, Bootstrap
  - Database: Django ORM, SQLite

<br>

## Key Features
- User Profiles:
  - Users can create profiles with usernames and join dates.
  - Users can upload profile pictures (or use default ones).
  - View registered posts, liked posts, followers, and following lists.
- Posting System:
  - Users can post product images and details.
  - A CRUD (Create, Read, Update, Delete) system for product posts.
  - Posts can receive likes and visitors can be tracked.
  - Sort posts by most recent or most popular.
- Social Interactions:
  - Users can follow other users.
  - Liking posts functionality.


### Requirements
![image description](media\images\requirements.png)

## Folder Structure
```bash
SPARTAMARKET
│
├── accounts/           # App handling user authentication and permissions
├── media/              # Folder for storing user-uploaded files
├── products/           # App managing product-related features
├── spartamarket/       # Project configuration files (settings.py, etc.)
├── static/             # Static files (CSS)
├── templates/          # base.html, main.html HTML template files
│   ├── base.html       # Base template for shared layout
│   └── main.html       # Main page template extending base.html
├── users/              # App managing user profiles and information
├── db.sqlite3          # SQLite database file
├── .gitignore          # Files and directories to be ignored by Git
├── manage.py           # Django management command file
├── requirements.txt    # List of dependencies for the project
```