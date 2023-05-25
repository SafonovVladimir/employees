from django.shortcuts import render

def index(request):
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits + 1,
    }

    return render(request, "employees/index.html", context=context)

