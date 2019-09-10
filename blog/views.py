#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article, Tags, Filter, User, Comments
import re
from . import handlelib
import time
import json

# Create your views here.


def index(request):
    try:
        PIndex = request.GET['p']
    except:
        PIndex = ''
    articles, PIndex, Pnum, has_next, has_prev = handlelib.get_all_articles(PIndex)
    content = {}
    content["articles"] = articles
    content["pic"] = handlelib.get_header_pic()
    content["filters"] = handlelib.get_all_filter()
    content["root"] = handlelib.get_root()
    content["PIndex"] = PIndex
    content["Pnum"] = Pnum
    content["has_next"] = has_next
    content["has_prev"] = has_prev
    content["filter_flag"] = 0
    
    
    return render(request,  "blog/index.html", content)


def detail(request):
    try:
        id = request.GET['id']
    except:
        id = 1
    content = {}
    content['article'] = handlelib.get_article_by_id(id)
    content['id'] = id
    content['filters'] = handlelib.get_all_filter()
    content["root"] = handlelib.get_root()
    return render(request, "blog/detail.html", content)

def filte(request, id):
    try:
        PIndex = request.GET['p']
    except:
        PIndex=''
    articles, PIndex, Pnum, has_next, has_prev = handlelib.get_article_by_filter(id, PIndex)
    content = {}
    content["articles"] = articles
    content["pic"] = handlelib.get_filter_header_pic(id)
    content["filters"] = handlelib.get_all_filter()
    content["root"] = handlelib.get_root()
    content["PIndex"] = PIndex
    content["Pnum"] = Pnum
    content["has_next"] = has_next
    content["has_prev"] = has_prev
    content["filter_flag"] = 0
    return render(request,  "blog/index.html", content)


def filte_by_time(request):
    
    try:# Create your views here.
        PIndex = request.GET['p']
    except:
        PIndex=''
    
    articles, PIndex, Pnum, has_next, has_prev = handlelib.get_article_by_time(PIndex)
    content = {}
    content["articles"] = articles
    content["pic"] = handlelib.get_time_header_pic()
    content["filters"] = handlelib.get_all_filter()
    content["root"] = handlelib.get_root()
    content["PIndex"] = PIndex
    content["Pnum"] = Pnum
    content["has_next"] = has_next
    content["has_prev"] = has_prev
    content["filter_flag"] = 0
    return render(request, 'blog/index.html', context=content)

def comment(request):
    
    a_id = request.POST.get("a_id")
    u_id = request.POST.get("u_id")
    u_conmment = request.POST.get("comment")
    comment = Comments.create(a_id, u_id, u_conmment)
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    try:
        comment.save()
    except Exception:
        print(Exception)

        return JsonResponse({"status": 0})
        
    return JsonResponse({"status": 1, "a_id": a_id, "u_id": u_id, "u_comment":u_conmment, "year":year, "month": month, "day":day})
        