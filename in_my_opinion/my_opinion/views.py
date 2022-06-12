from django.shortcuts import render
from .models import Appeal
from django.shortcuts import redirect
import math


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def end_edit(request):
    appeal_id = request.GET.get('appeal_id')
    title = request.GET.get('title')
    history = request.GET.get('history')
    appeal = Appeal.objects.get(appeal_id=appeal_id)
    if title != '':
        appeal.title = title
        appeal.save()
    if history != '':
        appeal.history = history
        appeal.save()
    response = redirect(f'http://127.0.0.1:8000/manage_appeal/?appeal_id_1={appeal_id}')
    return response


def edit(request):
    appeal_id = request.GET.get('appeal_edit')
    appeal = Appeal.objects.get(appeal_id=appeal_id)
    return render(request, 'my_opinion/tempalates/edit.html', {'appeal': appeal})


def publicate(request):
    object = request.GET.get('appeal_publicate')
    appeal = Appeal.objects.get(appeal_id=object)
    appeal.status = 'опубліковано'
    appeal.save()
    response = redirect('http://127.0.0.1:8000/')
    return response


def index(request):
    appeal_list = Appeal.objects.all()
    page = request.GET.get('page', 1)
    appeal_len = len(appeal_list)
    pages = math.ceil(appeal_len/5)
    paginator = Paginator(appeal_list, 5)

    try:
        appeals = paginator.page(page)
    except PageNotAnInteger:
        appeals = paginator.page(1)
    except EmptyPage:
        appeals = paginator.page(paginator.num_pages)

    return render(request, 'my_opinion/tempalates/index.html', {'appeal_list': appeals, 'pages': pages, 'appeals_len': appeal_len})


def null_appeal(request):
    object = request.GET.get('appeal_delete')
    object.delete()
    return render(request, 'my_opinion/tempalates/null_appeal.html', {})


def manage_appeal(request):
    id_query = request.GET.get('appeal_id_1')
    appeal_data = Appeal.objects.get(appeal_id=id_query)
    return render(request, 'my_opinion/tempalates/appeal.html', {'appeal': appeal_data})


def index1(request):
    status_query = request.GET.get('status')
    category_query = request.GET.get('category')
    data_range_from_query = request.GET.get('data_range_from')
    data_range_to_query = request.GET.get('data_range_to')
    sorting_by_query = request.GET.get('sorting_by')
    direct_query = request.GET.get('direct')
    btn_query = request.GET.get('btn')


"""temporary solution"""
    if direct_query == 'За зростанням':
        if sorting_by_query == 'Дата створення(за замовчуванням)':
            if status_query == 'Всі':
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.order_by('date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('date_of_creation')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query).order_by('date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('date_of_creation')
            else:
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(status=status_query).order_by('date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('date_of_creation')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by('date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('date_of_creation')

        if sorting_by_query == 'Категоріям':
            if status_query == 'Всі':
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.order_by('category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('category')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query).order_by('category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('category')
            else:
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(status=status_query).order_by('category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('category')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by('category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('category')

    if sorting_by_query == 'Статусу':
        if status_query == 'Всі':
            if category_query == None:
                if (data_range_from_query and data_range_to_query) == '':
                    appeal_list = Appeal.objects.order_by('status')
                elif data_range_from_query == '' and data_range_to_query != '':
                    appeal_list = Appeal.objects.filter( date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('status')
                elif data_range_from_query != '' and data_range_to_query == '':
                    appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('status')
                elif (data_range_from_query and data_range_to_query) != '':
                    appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('status')
            else:
                if (data_range_from_query and data_range_to_query) == '':
                    appeal_list = Appeal.objects.filter(category=category_query).order_by('status')
                elif data_range_from_query == '' and data_range_to_query != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('status')
                elif data_range_from_query != '' and data_range_to_query == '':
                    appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('status')
                elif (data_range_from_query and data_range_to_query) != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('status')
        else:
            if category_query == None:
                if (data_range_from_query and data_range_to_query) == '':
                    appeal_list = Appeal.objects.filter(status=status_query).order_by('status')
                elif data_range_from_query == '' and data_range_to_query != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('status')
                elif data_range_from_query != '' and data_range_to_query == '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('status')
                elif (data_range_from_query and data_range_to_query) != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('status')
            else:
                if (data_range_from_query and data_range_to_query) == '':
                    appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by('status')
                elif data_range_from_query == '' and data_range_to_query != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('status')
                elif data_range_from_query != '' and data_range_to_query == '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('status')
                elif (data_range_from_query and data_range_to_query) != '':
                    appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('status')



    else:
        if sorting_by_query == 'Дата створення(за замовчуванням)':
            if status_query == 'Всі':
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.order_by('-date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('-date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('-date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('-date_of_creation')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query).order_by('-date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('-date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('-date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('-date_of_creation')
            else:
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(status=status_query).order_by('-date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('-date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('-date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('-date_of_creation')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by('-date_of_creation')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('-date_of_creation')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('-date_of_creation')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('-date_of_creation')

        if sorting_by_query == 'Категоріям':
            if status_query == 'Всі':
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.order_by('-category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(
                            date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('-category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(
                            date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('-category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(
                            date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('-category')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query).order_by('-category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(
                            date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('-category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(
                            date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('-category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('-category')
            else:
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(status=status_query).order_by('-category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('-category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('-category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('-category')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by(
                            'category')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('-category')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('-category')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('-category')


        if sorting_by_query == 'Статусу':
            if status_query == 'Всі':
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.order_by('-status')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter(date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query]).order_by('-status')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"]).order_by('-status')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, data_range_to_query]).order_by('-status')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query).order_by('-status')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query).order_by('-status')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query).order_by('-status')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query).order_by('-status')
            else:
                if category_query == None:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(status=status_query).order_by('-status')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], status=status_query).order_by('-status')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], status=status_query).order_by('-status')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, data_range_to_query], status=status_query).order_by('-status')
                else:
                    if (data_range_from_query and data_range_to_query) == '':
                        appeal_list = Appeal.objects.filter(category=category_query, status=status_query).order_by('-status')
                    elif data_range_from_query == '' and data_range_to_query != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=["1000-10-10 10:10:10", data_range_to_query], category=category_query, status=status_query).order_by('-status')
                    elif data_range_from_query != '' and data_range_to_query == '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, "3000-10-10 10:10:10"], category=category_query, status=status_query).order_by('-status')
                    elif (data_range_from_query and data_range_to_query) != '':
                        appeal_list = Appeal.objects.filter( date_of_creation__range=[data_range_from_query, data_range_to_query], category=category_query, status=status_query).order_by('-status')

    appeal_len = len(appeal_list)
    pages = math.ceil(appeal_len / 5)
    page = request.GET.get('page', 1)

    paginator = Paginator(appeal_list, 5)
    try:
        appeals = paginator.page(page)
    except PageNotAnInteger:
        appeals = paginator.page(1)
    except EmptyPage:
        appeals = paginator.page(paginator.num_pages)

    return render(request, 'my_opinion/tempalates/index.html', {'appeal_list': appeals, 'pages': pages, 'appeals_len': appeal_len})
