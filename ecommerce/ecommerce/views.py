from django.shortcuts import render


# def home(request):
#     # process the request/fetch data
#     return render(request,"home.html")


def about(request):
    # process the request/fetch data
    return render(request,"about.html")


def home(request):
    context = {
        "page_title": "Home Page",
        "user_name": "Kelvin",
        "user_email": "kelvin@example.com"
    }
    return render(request, "home.html", context)


def dashboard(request):
    context = {
        "username": "Alice",
        "is_admin": False
    }
    return render(request, "dashboard.html", context)

def shopping(request):
    context = {
        "shopping_list": ["Milk", "Bread", "Eggs", "Butter"]
    }
    return render(request, "shopping.html", context)

def students(request):
    students_data = [
        {"name": "John", "grade": 72},
        {"name": "Mary", "grade": 45},
        {"name": "Peter", "grade": 88},
    ]
    return render(request, "students.html", {"students": students_data})

