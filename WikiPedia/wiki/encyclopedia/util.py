import re
import random
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def search(query):
    _, filenames = default_storage.listdir("entries")
    for filename in filenames:
        if filename.split(".")[0] == query:
            return query, True
    results = list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if (filename.endswith(".md") and filename.find(query)!=-1)))
    if len(results)!=0:
        return results,  False 
    else:
        return None,None
      
def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    if len(title) !=0:
        filename = f"entries/{title}.md"
        if default_storage.exists(filename):
            return False
        else:
            default_storage.save(filename, ContentFile(content))
            return True
    else:
        return False
     
      
def Edit_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def give_random():
    _, filenames = default_storage.listdir("entries")
    titles = list(sorted(re.sub(r"\.md$", "", filename)
                       for filename in filenames if (filename.endswith(".md"))))
    random_title = random.choice(titles)
    return random_title