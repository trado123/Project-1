from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def show_entry(request):
    return render(request, "encyclopedia/entry.html", {
        "entry_text": util.get_entry("CSS")
    })

