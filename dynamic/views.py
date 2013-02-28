from django.shortcuts import render
from random import choice


from django.http import HttpResponse

def index(request):
    """This is the default/home page"""
    
    return HttpResponse("Hello, world. This is a dynamic view.")

def question(request):
    """Show the question form for the magic eightball"""
   
    return render(request, 'question.html')



def magic(request,question=""):
    """Ask the question and show the mystical response"""
    
    #read the POST parameter, "question" from our form
    question = request.REQUEST["question"]

    #choose a random response
    answer = random_response()

    #create a dictionary with that data our template needs
    context = {"question": question, "answer": answer }

    #"render the template, "magic.html", with our context
    return render(request, 'magic.html', context)


def random_response():
    """A helper method for magic() which chooses one of the random responses"""
    
    responses = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes – definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"]
    
    return choice(responses)
