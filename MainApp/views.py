from django.shortcuts import render,redirect
from .models import Pizza, Topping
from .forms import PizzaForm

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas =Pizza.objects.all()

    context ={'pizzas': pizzas} #key for html value for views

    return render(request,'MainApp/pizzas.html',context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings =pizza.topping_set.order_by('-topping_name')

    context= {'pizza':pizza,'toppings':toppings}
    return render(request,'MainApp/pizza.html',context)

def new_comment(request, pizza_id):

    pizza = Topping.objects.get(id=pizza_id)

    if request.method !='POST':
        form = PizzaForm()
    else:
        form =PizzaForm(data=request.POST)

        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.pizza= pizza
            new_comment.save()
            return redirect('MainApp:pizza',pizza_id=pizza_id)

    context= {'form':form,'pizza':pizza}
    return render(request,'MainApp/new_comment.html',context)