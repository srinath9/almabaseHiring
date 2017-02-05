from django.shortcuts import render

from models import Games
# Create your views here.
import pdb,json , math

def all(request):
    response = "You're looking at the results of question %s."

    # pdb.set_trace()
    count = Games.objects.all().count()
    list_val = Games.objects.all()[:6]
    # inc_api_count(request)
    # solr_list = SearchQuerySet().autocomplete(content_auto = 'Treebo')
    Games.es.create_index()

    try:
        if request.method == 'GET' :
            # pdb.set_trace()
            if request.GET !=  {}:
                stringquery = request.GET['name']
                list_val = Games.objects.filter(title__contains=stringquery)
                # pdb.set_trace()
                count = list_val.count()
            
    except Exception as e:
        pass
    context = {
        'list_val': list_val,
        'count': int(math.ceil(count / 6.0)),
        'current': 1,
        'range_list': range(1,int(math.ceil(count / 6.0)) +1 )
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
    # return render(request, 'list_products.html', context)
    # return HttpResponse(list_val)

def pagination(request, page_id):
    page_id = int(page_id)-1
    count = Games.objects.all().count()
    list_val = Games.objects.all()[page_id*6:page_id*6 + 6]
    # inc_api_count(request)
    context = {
        'list_val': list_val,
        'count' : int(math.ceil(count/6.0)),
        'current' : page_id,
        'range_list' : range(int(math.ceil(count/6.0)))
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)