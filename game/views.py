from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Game

def register_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        cp = request.POST.get('confirm_password')

        if p != cp:
            messages.error(request, "Passwords do not match!")
            return render(request, 'register.html')
        
        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already taken!")
            return render(request, 'register.html')

        user = User.objects.create_user(username=u, password=p)
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('game_dashboard')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('game_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from .models import Profile, Game, UserMission, Activity, Tournament

@login_required
def game_dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Get all active games
    game_list = Game.objects.filter(active=True)
    
    # Get user missions
    all_user_missions = UserMission.objects.filter(user=request.user)
    completed_missions = all_user_missions.filter(completed=True).count()
    missions = all_user_missions[:3]
    
    # Get recent activities
    activities = Activity.objects.filter(user=request.user)[:5]
    
    # Get active tournament
    tournament = Tournament.objects.filter(active=True).first()
    points_needed = 0
    progress_percentage = 0
    if tournament:
        points_needed = max(tournament.qualification_points - profile.points, 0)
        if tournament.qualification_points > 0:
            progress_percentage = min(int((profile.points / tournament.qualification_points) * 100), 100)
    
    # Get leaderboard - Top 5 players
    leaderboard = Profile.objects.order_by('-points')[:5]
    
    # Calculate user's numerical rank
    all_profiles = Profile.objects.order_by('-points')
    user_rank = 1
    for i, p in enumerate(all_profiles):
        if p.user == request.user:
            user_rank = i + 1
            break

    context = {
        'profile': profile,
        'games': game_list,
        'missions': missions,
        'completed_missions_count': completed_missions,
        'total_missions_count': all_user_missions.count(),
        'activities': activities,
        'leaderboard': leaderboard,
        'user_rank': user_rank,
        'tournament': tournament,
        'points_needed': points_needed,
        'progress_percentage': progress_percentage,
    }
    return render(request, "game.html", context)
