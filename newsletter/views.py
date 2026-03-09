from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber, WebsiteContent
import os
import json
from django.views.decorators.csrf import csrf_protect

# Handle subscription
@csrf_protect  # Use proper CSRF protection
def subscribe(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email", "")

            # Validate the email address
            if not email or "@" not in email:
                return JsonResponse({"error": "Invalid email address"}, status=400)

            # Save the email to the Subscriber model
            subscriber, created = Subscriber.objects.get_or_create(email=email)

            if not created:
                return JsonResponse({"message": "You are already subscribed!"})

            return JsonResponse({"message": "Subscription successful!"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=405)


# Admin login function
DEFAULT_PASSWORD = os.getenv("ADMIN_PASSWORD", "fallback-password-dev-only")

def admin_login(request):
    if request.method == "POST":
        password = request.POST.get("password")
        
        if password == DEFAULT_PASSWORD:
            # If the password matches, you can store the password check status in the session
            request.session["is_authenticated"] = True
            return redirect("dashboard")  # Redirect to the admin dashboard after successful login
        
        else:
            # Show an error message if the password is wrong
            return render(request, "newsletter/admin_login.html", {"error": "Invalid password!"})

    return render(request, "newsletter/admin_login.html")


from church_website.news_data import NEWS_POSTS

# Admin dashboard to view all subscribers and website content
def dashboard(request):
    # Check if the user is authenticated
    if not request.session.get("is_authenticated"):
        return redirect("admin_login")  # Redirect to login page if not authenticated

    subscribers = Subscriber.objects.all()
    content = WebsiteContent.objects.all()
    return render(request, "newsletter/Admin_Dashboard.html", {
        'subscribers': subscribers, 
        'content': content,
        'news_posts': NEWS_POSTS,
        'upcoming_events': UPCOMING_EVENTS
    })


# Update website content for a specific page
def update_content(request, page_name):
    content = get_object_or_404(WebsiteContent, page_name=page_name)

    if request.method == 'POST':
        content.content = request.POST.get('content')
        content.save()
        return redirect('dashboard')  # Redirect after updating content
    
    return render(request, "newsletter/update_content.html", {'content': content})


# View to clear all subscriptions
def clear_subscriptions(request):
    if request.method == "POST":
        Subscriber.objects.all().delete()  # Deletes all subscribers
        return redirect('dashboard')  # Redirect back to the dashboard after clearing
    
    return redirect('dashboard')  # If not a POST request, redirect to the dashboard
