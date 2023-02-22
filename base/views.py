from django.db.models import Q, Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import School, Review, FakeShool
from .forms import ReviewForm



def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=q)
    )
    context = {'schools': schools}


    return render(request, 'base/home.html', context)

def search(request):
    school = request.GET.get('school')
    payload = []
    if school:
        schools = School.objects.filter(name__icontains=school).values('name', 'id')
        for fake_school_obj in schools:
            payload.append(fake_school_obj)
    return JsonResponse({'data': payload})


def school(request, pk):
    schools = School.objects.get(id=pk)

    reviewz = schools.review_set.all()
    sum_nums = []



    for review in reviewz:
        sum_nums.append(round((review.location +
                          review.opportunities + review.facilities + review.food
                          + review.clubs + review.social) / 6))
        review.overall = round((review.location +
                                review.opportunities + review.facilities + review.food
                                + review.clubs + review.social) / 6)
        review.save()

    schools.rating = (sum(sum_nums) / len(sum_nums))
    schools.rating = round(schools.rating, 1)
    schools.rating_location = round(reviewz.aggregate(Avg('location'))['location__avg'], 1)
    schools.rating_opportunities = round(reviewz.aggregate(Avg('opportunities'))['opportunities__avg'], 1)
    schools.rating_facilities = round(reviewz.aggregate(Avg('facilities'))['facilities__avg'], 1)
    schools.rating_food = round(reviewz.aggregate(Avg('food'))['food__avg'], 1)
    schools.rating_clubs = round(reviewz.aggregate(Avg('clubs'))['clubs__avg'], 1)
    schools.rating_social = round(reviewz.aggregate(Avg('social'))['social__avg'], 1)
    schools.save()



    reviews = schools.review_set.all().order_by('-created')


    context = {'schools': schools, 'reviews': reviews}
    return render(request, 'base/school.html', context)


def review(request, pk):
    school = School.objects.get(id=pk)
    form = ReviewForm

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                object = form.save(commit=False)
                object.user = request.user
                object.school = school
                form.save()
                return redirect('home')

        context = {'form': form, 'schools': school}
        return render(request, 'base/review.html', context)

    else:
        return redirect('register_user')


