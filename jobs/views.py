from django.shortcuts import render


def encontrar_jobs(request):
    return render(request, 'jobs/encontrar_jobs.html')
