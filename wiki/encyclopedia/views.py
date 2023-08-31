from django.shortcuts import render 
from random import randint

from . import util
from markdown2 import markdown




def index(request):
    context = {
        "entries": util.list_entries(),
    }
    return render(request, "encyclopedia/index.html", context)


def wiki_Entry(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html")
    else:
        entry_content = markdown(entry)
        context = {
            "title": title,
            "entry_md": entry_content,
        }
        return render(request, "encyclopedia/entries.html", context)


def search(request):
    query = request.POST["q"]
    ls_entries = util.list_entries()
    feedback = []
    no_result = False
    for i in range(len(ls_entries)):
        if query.lower() == ls_entries[i].lower():
            return render(request, "encyclopedia/entries.html", {
                "title": ls_entries[i],
                "entry_md": markdown(util.get_entry(ls_entries[i]))
            })
        elif query.lower() in ls_entries[i].lower():
            feedback.append(ls_entries[i])
    if len(feedback) == 1:
        return render(request, "encyclopedia/entries.html", {
            "title": feedback[0],
                      "entry_md" : markdown(util.get_entry(feedback[0]))
            })
    elif len(feedback) == 0:
        no_result = True
    context = {
        "no_result": no_result,
        "query": query,
        "feedback": feedback,
    }
    return render(request ,"encyclopedia/search.html", context)

def randomPage(request):
    ls_entries = util.list_entries()
    rd_entry = ls_entries[randint(0, len(ls_entries)-1)]
    context = {
        "title": rd_entry,
        "entry_md":markdown(util.get_entry(rd_entry)),
    }
    return render(request, "encyclopedia/entries.html", context)
