from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import sample


def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    # content = '<h3>今天推荐的水果是:</h3>'
    # content += '<hr>'
    # content += '<url>'
    # for fruit in selected_fruits:
    #     content += f'<li>{fruit}<li>'
    # content += '</url>'
    # return HttpResponse(content)

    return render(request, 'index.html', {'fruits': selected_fruits})
