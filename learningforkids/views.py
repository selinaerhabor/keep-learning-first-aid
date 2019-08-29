from django.shortcuts import render


# Learning for kids navigation link.
def learningforkids(request):
    return render(request, 'learningforkids.html')


"""
Redirects users to an interactive quiz aimed at kids, which has 
10 multiple choice questions and gives players feedback after
completion of quiz
"""
def learningforkidsquiz(request):
    return render(request, "learningforkidsquiz.html")