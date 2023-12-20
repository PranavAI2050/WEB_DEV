from django.shortcuts import render
from markdown2 import Markdown
markdowner = Markdown()
# Create your views here.

from . import util
from django import forms

class Search_form(forms.Form):
    query = forms.CharField(label = 'Search Encyclopedia')

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })
def entry(request,entry):
    content = util.get_entry(entry)
    if content != None:
        return render(request, "encyclopedia/entry.html", {
        "entrie": markdowner.convert(content),
        'title':entry
    })
    else:
        return render(request, "encyclopedia/index.html", {
                "entries": None,
                 "message" :None
                
            })


def search(request):
    if request.method == "POST":
        query = request.POST.get("query").strip() if request.POST.get("query") else None

        if query:
            result, Flag = util.search(query)

            if Flag:
                content = util.get_entry(result)
                return render(request, "encyclopedia/entry.html", {
                    "entrie": markdowner.convert(content),
                    "title":query
                })
            elif not Flag:
                return render(request, "encyclopedia/index.html", {
                    "entries": result,
                    "message" :Flag,
                    "title":query

                })
            else:
                content = result
                return render(request, "encyclopedia/entry.html", {
                    "entrie": markdowner.convert(content),
                    "title":query
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                 "message" :Flag,
                 "title":query
                
            })

def create(request):
  
    if request.method == "POST":
        title = request.POST.get("title").strip() if request.POST.get("title") else ""
        content = request.POST.get("content").strip() if request.POST.get("content") else ""
        Flag = util.save_entry(title,content)
        if Flag == True:
            content = util.get_entry(title)
            return render(request, "encyclopedia/entry.html", {
                "entrie": markdowner.convert(content),
                "message":Flag,
                "title":title
                })
        else:
       
            return render(request, "encyclopedia/create.html", {
                "message": Flag
                })
    else:
    
        return render(request, "encyclopedia/create.html", {
            "edit":False,
            })
    
def edit(request,title):
    if request.method == "POST":
        content = request.POST.get("content").strip() if request.POST.get("content") else ""  
        util.Edit_entry(title,content)
        return render(request, "encyclopedia/entry.html", {
                "entrie": markdowner.convert(content),
                "message":True,
                "title":title
                })
        
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/create.html",{
            "edit" :True,
            "title":title,
            "content":content

        })
    
def random(request):
    title = util.give_random()
    content = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        "entrie": markdowner.convert(content),
        'title':title
    })
