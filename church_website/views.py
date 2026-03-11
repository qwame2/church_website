import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
import fitz  # PyMuPDF
from django.templatetags.static import static
from django.http import HttpRequest

from .news_data import NEWS_POSTS, UPCOMING_EVENTS
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, "youth_church_landing.html", {
        "news_posts": NEWS_POSTS,
        "upcoming_events": UPCOMING_EVENTS
    })

def church_news_archive(request):
    return render(request, "church_news_archive.html", {"news_posts": NEWS_POSTS})

def gallery(request):
    return render(request, "gallery.html") 

def map(request):
    return render(request, "map.html") 

def book(request):
    return render(request, "book.html") 

def youth_church_landing(request):
    return render(request, "youth_church_landing.html", {
        "news_posts": NEWS_POSTS,
        "upcoming_events": UPCOMING_EVENTS
    })

def menfellow(request):
    return render(request, "menfellow.html")


def wemenfellow(request):
    return render(request, "wemenfellow.html")

def youth(request):
    return render(request, "youth.html")

def child(request):
    return render(request, "child.html")

def my_view(request):
    return render(request, "your_template.html", {"STATIC_URL": static('')})



def podcast(request):
    return render(request, "podcast.html")





def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    """
    text = ""
    try:
        # Open the PDF file
        with fitz.open(pdf_path) as doc:
            # Iterate through each page
            for page in doc:
                # Extract text from the page
                text += page.get_text("text") + "\n\n"
    except Exception as e:
        # Handle errors (e.g., invalid PDF file)
        text = f"Error reading PDF: {str(e)}"
    return text

def reading_page(request):
    pdf_filename = request.GET.get("pdf")  # Get the filename from the URL

    if not pdf_filename:
        return render(request, "reading_page.html", {"text_content": "No PDF selected."})

    # Resolve the static file path
    pdf_static_path = static(pdf_filename)

    # Construct the full path to the PDF file
    pdf_full_path = os.path.join(settings.BASE_DIR, pdf_static_path.lstrip('/'))

    # Debugging: Print the paths
    print("PDF Static Path:", pdf_static_path)
    print("PDF Full Path:", pdf_full_path)
    print("Does the file exist?", os.path.exists(pdf_full_path))

    if not os.path.exists(pdf_full_path):
        return render(request, "reading_page.html", {"text_content": "PDF not found."})

    # Extract text from PDF
    text_content = extract_text_from_pdf(pdf_full_path)

    return render(request, "reading_page.html", {"text_content": text_content})