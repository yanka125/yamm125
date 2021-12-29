import json

from django.shortcuts import render, redirect

from .forms import InputForm
from .models import InputModel


def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['name']
            data = json.dumps(name_input, ensure_ascii=False)
            InputModel.objects.create(data=data, field='name')

            for count in range(1, len(request.POST) - 1):
                query = 'name' + str(count)
                input_value = request.POST[query]
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data, field=field)
                count += 1
        return redirect('/submitted_forms/')
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})


def complete(request):
    query = InputModel.objects.all().values('id', 'field', 'data')
    json_list = list(query)
    return render(request, 'submitted_forms.html', {'json_list': json_list})
