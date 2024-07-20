from django.shortcuts import get_object_or_404, redirect, render
from .models import Professor ,  Rating
from .forms import RatingForm
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    ProfessorDetails = Professor.objects.all()
    return render(request , 'home.html' , {'ProfessorDetails': ProfessorDetails})

@login_required
def rate_professor(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    user = request.user
    
    # Check if the user has already rated this professor
    if request.session.get(f'has_rated_{professor.pk}_{user.pk}', False):
        messages.error(request, f"You have already rated {professor.name}.")
        return redirect('home')

    
    if request.method == 'POST':
        form = RatingForm(request.POST) 
        if form.is_valid():
            rating = form.save(commit=False)
            rating.professor = professor  # Assign the professor to the rating
            rating.author = user
            rating.save()
            messages.success(request, f"Successfully rated {professor.name}")
            request.session[f'has_rated_{professor.pk}_{user.pk}'] = True
            return redirect('home')
        else:
            messages.error(request, "There was an error with your rating.")
    else:
        form = RatingForm(initial={'professor': professor})

    return render(request, 'rate.html', {'form': form, 'professor': professor})

def check_rating(request):
    ratings = Rating.objects.all().order_by('-datecreated')
    return render(request, 'check_rating.html', {'ratings': ratings})

def overall_rating(request,pk):
    professor = get_object_or_404(Professor , pk = pk)
    ratings = Rating.objects.filter(professor = professor)
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    context = {
        'average_rating': average_rating,
        'professor': professor
    }
    
    return render(request, 'overall_rating.html', context=context)
    