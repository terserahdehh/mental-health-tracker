from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306173435',
        'name': 'Serafina Nala Putri Setiawan',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)