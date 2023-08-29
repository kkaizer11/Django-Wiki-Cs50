from django.shortcuts import render

from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


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
