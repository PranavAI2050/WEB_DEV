# Project Wiki 📚

This repository hosts a powerful web application, serving as an encyclopedia where users can create, edit, and explore entries. The application is meticulously crafted using Python and Django.

https://github.com/PranavAI2050/WEB_DEV/assets/123180829/0b844e8f-3b1b-4477-8a79-cef4b8e2dc70
## Features 🚀

### Entry Page 📖

Visiting `/wiki/TITLE`, where `TITLE` is the entry title, renders a page displaying its contents. The content is fetched using the appropriate util function. If the entry doesn't exist, users see a user-friendly error page.

### Index Page 📑

The `index.html` page now allows users to click on any entry name, redirecting them directly to the corresponding entry page.

### Search 🔍

Users can type a query into the search box in the sidebar to find encyclopedia entries. If the query matches an entry name, users are redirected to that entry's page. Otherwise, a search results page is displayed, showing entries with the query as a substring. Clicking on any entry name on the search results page takes the user to that entry's page.

### New Page 🆕

Clicking "Create New Page" in the sidebar takes users to a page where they can craft a new encyclopedia entry. They can input a title and Markdown content, then click a button to save. If an entry already exists with the provided title, an error message is displayed. Otherwise, the entry is saved to disk, and the user is redirected to the new entry's page.

### Edit Page 🖊️

On each entry page, users can click a link to be taken to a page where they can edit the entry's Markdown content in a textarea. The textarea is pre-populated with the existing Markdown content. Clicking a button saves the changes, and the user is redirected back to the entry's page.

### Random Page 🎲

Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion 🔄

Any Markdown content in an entry file is converted to HTML before being displayed, using the `python-markdown2` package. Install it via `pip3 install markdown2`.

## Getting Started 🚀

1. **Clone this repository.**
   ```bash
   git clone https://github.com/PranavAI2050/WEB_DEV.git
   cd wiki
2. **Create and activate Virtual env:**
   ```bash
   python -m venv env_name
   .\env_name\Scripts\activate
3. **Install libraries:**
   ```bash
   pip install Django markdown2
4. **Run in terminal:**
   ```bash
   python manage.py
