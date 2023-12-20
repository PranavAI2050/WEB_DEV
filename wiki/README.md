# Project Wiki

This repository contains a web application that serves as an encyclopedia, allowing users to create, edit, and explore entries. The application is built using Python and Django.

https://github.com/PranavAI2050/WEB_DEV/assets/123180829/0b844e8f-3b1b-4477-8a79-cef4b8e2dc70

## Features

### Entry Page

Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, will render a page displaying the contents of that entry. The content is fetched using the appropriate util function. If the requested entry does not exist, the user will be presented with an error page.

### Index Page

The `index.html` page has been updated to allow users to click on any entry name, redirecting them directly to the corresponding entry page.

### Search

Users can type a query into the search box in the sidebar to search for an encyclopedia entry. If the query matches the name of an entry, the user is redirected to that entry's page. If not, a search results page is displayed, showing entries that have the query as a substring. Clicking on any entry name on the search results page takes the user to that entry's page.

### New Page

Clicking "Create New Page" in the sidebar takes the user to a page where they can create a new encyclopedia entry. Users can enter a title and Markdown content for the page, then click a button to save. If an entry already exists with the provided title, an error message is displayed. Otherwise, the entry is saved to disk, and the user is redirected to the new entry's page.

### Edit Page

On each entry page, users can click a link to be taken to a page where they can edit the entry's Markdown content in a textarea. The textarea is pre-populated with the existing Markdown content. Clicking a button saves the changes, and the user is redirected back to the entry's page.

### Random Page

Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

### Markdown to HTML Conversion

Any Markdown content in an entry file is converted to HTML before being displayed, using the `python-markdown2` package. Install it via `pip3 install markdown2`.

## Getting Started

1. Clone this repository.
   ```bash
   git clone https://github.com/PranavAI2050/WEB_DEV.git
   cd your-repo
  ### Setting up a Wiki  

1. Open your terminal or command prompt.

2. Navigate to your project directory.
   ```bash
     cd path/to/your/wiki
3.Create and activate Virtual env
```bash
     python -m venv venv
     .\venv\Scripts\activate
```
4.Install requirements Run in terminal.
````bash
    python manage.py runserver
