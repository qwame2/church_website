from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Profile, Game, UserMission, Activity, Tournament

@never_cache
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

@never_cache
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

@never_cache
def logout_view(request):
    logout(request)
    return redirect('login')

@never_cache
@login_required(login_url='login')
def game_dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Get all active games
    game_list = Game.objects.filter(active=True)
    
    # Get user missions
    all_user_missions_qs = UserMission.objects.filter(user=request.user)
    completed_missions = all_user_missions_qs.filter(completed=True).count()
    missions = all_user_missions_qs[:3]
    
    # Get recent activities
    activities_qs = Activity.objects.filter(user=request.user)
    activities = activities_qs[:5]
    
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
        'total_missions_count': all_user_missions_qs.count(),
        'activities': activities,
        'leaderboard': leaderboard,
        'user_rank': user_rank,
        'tournament': tournament,
        'points_needed': points_needed,
        'progress_percentage': progress_percentage,
    }
    return render(request, "game.html", context)

@never_cache
@login_required(login_url='login')
def tournaments_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    tournament = Tournament.objects.filter(active=True).first()
    leaderboard = Profile.objects.order_by('-points')[:5]
    
    context = {
        'profile': profile,
        'tournament': tournament,
        'leaderboard': leaderboard,
    }
    return render(request, "tournaments.html", context)
