from django.shortcuts import render, redirect

from . import util
from markdown2 import markdown


def index(request):
    content = {
        "entries": util.list_entries(),
    }
    return render(request, "encyclopedia/index.html", content)


def wiki_Entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html")
    else:
        entry_content = markdown(entry)
        content = {
            "title": title,
            "entry_md": entry_content,
        }
        return render(request, "encyclopedia/entries.html", content)


def search(request):
    query = request.POST["query"]
    ls_entries = util.list_entries()
    result = []
    for i in range(len(ls_entries)):
        if query.lower() == ls_entries[i].lower():
            return redirect("wiki_Entry", title=ls_entries[i])
        elif query.lower() in ls_entries[i].lower():
            result.append(ls_entries[i])
    content = {
        "title": "Search results",
        "query": query,
        "feedback": result,
    }
    return render(request, "encyclopedia/search.html", content)
