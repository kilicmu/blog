#coding=utf-8
#此文件为视图处理文件
from .models import Article, Tags, Filter, User, Headpic,Comments
from django.core.paginator import  Paginator
from django.db.models import Max
from lxml import etree
import random


def get_header_pic():
    pics = Headpic.objects.all()
    choose_num = random.randint(0, len(pics))
    if choose_num == len(pics):
        choose_num-=1
    pic = pics[choose_num]
    
    temp={}
    temp["title"] = pic.h_title.upper()
    temp["pwd"] = pic.h_pic
    temp["content"] = pic.h_content
    return temp
    
def get_filter_header_pic(filter_id):
    filter = Filter.objects.get(pk=filter_id)
    
    temp={}
    temp["title"] = filter.Fname.upper()
    temp["pwd"] = filter.header_pic
    temp["content"] = "Classification and specific content"
    return temp

def get_time_header_pic():
    pics = Headpic.objects.all()
    choose_num = random.randint(0, len(pics))
    if choose_num == len(pics):
        choose_num-=1
    pic = pics[choose_num] 
    temp={}
    temp["title"] = "Recently".upper()
    temp["pwd"] = pic.h_pic
    temp["content"] = "The ten most recent selections"
    return temp

def get_root():
    user_temp = User.objects.filter(pk=1)[0]
    
    root = {}
    root['title']=user_temp.Uname
    root['content']=user_temp.Ucontent
    root['pic']=user_temp.Uimg
    return root


def get_all_articles(PIndex):
    articles = Article.objects.filter(a_isdelete = 0)
    count = articles.count()
    contents = []
    for article in articles:
        temp = {}
        temp['article_id'] = article.id
        tags = Tags.objects.filter(Tags_Article_id = temp['article_id'])
        tag_temp = []
        for tag in tags:
            t={}
            fil = tag.Filter_Tags_id
            t["id"] = fil.id
            t["name"] = fil.Fname
            tag_temp.append(t)
            
        temp['tags'] = tag_temp
        temp['title'] = article.a_title
        context_temp = article.a_content
        context_html = etree.HTML(context_temp)
        temp['pic'] = article.a_pic
        temp['year'] = article.a_uploadTime.year
        temp['month'] = article.a_uploadTime.month
        temp['day'] = article.a_uploadTime.day
        temp['count'] = 0
        contents.append(temp)
    p = Paginator(contents, 2)
    if PIndex == '':
        PIndex = '1'
    PIndex = int(PIndex)
    contents2 = p.page(PIndex)
    has_next = contents2.has_next()
    has_prev = contents2.has_previous()
    Pnum = p.num_pages
    return contents2, PIndex, Pnum, has_next, has_prev


def get_article_by_id(id):
    temp = {}
    article = Article.objects.get(pk = id)
    tags = Tags.objects.filter(Tags_Article_id = id)
    tags_temp = []
    for tag in tags:
        t = {}
        filter = Filter.objects.get(id = tag.Filter_Tags_id_id)
        t["title"] = filter.Fname
        t["id"] = filter.id
        tags_temp.append(t)
    comments = Comments.objects.filter(Comments_Article_id_id=id, Cisdelete=0)
    comment_datas = []
    for comment in comments:
        c_temp = {}
        c_temp["user"] = comment.Cuser
        c_temp["content"] = comment.Ccontent
        c_temp["date"] = comment.Cdate
        comment_datas.append(c_temp)
    temp['comment'] = comment_datas
    
    temp['title'] = article.a_title
    temp['context'] = article.a_content
    temp['tags'] = tags_temp
    temp['pic'] = article.a_pic
    temp['date'] = article.a_uploadTime
    temp['year'] = article.a_uploadTime.year
    temp['month'] = article.a_uploadTime.month
    temp['day'] = article.a_uploadTime.day
    temp['readnum'] = article.a_readnum
    temp['likenum'] = article.a_likenum
    return temp


def get_all_filter():
    filters_temp = Filter.objects.all()
    filters = []
    for i in filters_temp:
        temp = {}
        temp['id'] = i.pk
        temp['title'] = i.Fname
        filters.append(temp)
    return filters

def get_article_by_filter(filter_id, PIndex):
    contents = []
    tags = Tags.objects.filter(Filter_Tags_id_id=filter_id)
    articles = []
    for tag in tags:
        article = Article.objects.filter(pk=tag.Tags_Article_id_id)
        articles.append(article[0])
    
    for article in articles:
        temp = {}
        temp['article_id'] = article.id
        tags = Tags.objects.filter(Tags_Article_id = temp['article_id'])
        tag_temp = []
        for tag in tags:
            t={}
            fil = tag.Filter_Tags_id
            t["id"] = fil.id
            t["name"] = fil.Fname
            tag_temp.append(t)
        temp['tags'] = tag_temp
        temp['title'] = article.a_title
        context_temp = article.a_content
        context_html = etree.HTML(context_temp)
        temp['pic'] = article.a_pic
        temp['year'] = article.a_uploadTime.year
        temp['month'] = article.a_uploadTime.month
        temp['day'] = article.a_uploadTime.day
        temp['count'] = 0
        contents.append(temp)
    p = Paginator(contents, 2)
    if PIndex == '':
        PIndex = '1'
    PIndex = int(PIndex)
    contents2 = p.page(PIndex)
    has_next = contents2.has_next()
    has_prev = contents2.has_previous()
    Pnum = p.num_pages
    return contents2, PIndex, Pnum, has_next, has_prev
        
    

def get_article_by_time(PIndex):
    contents=[]
    articles = Article.objects.all()
    count = articles.count()
    if count < 10:
        articles = articles[:count]
    else:
        articles = articles[count-10:count]
    
    for article in articles[::-1]:
        temp = {}
        temp['article_id'] = article.id
        tags = Tags.objects.filter(Tags_Article_id = temp['article_id'])
        tag_temp = []
        for tag in tags:
            t={}
            fil = tag.Filter_Tags_id
            t["id"] = fil.id
            t["name"] = fil.Fname
            tag_temp.append(t)
            
        temp['tags'] = tag_temp
        temp['title'] = article.a_title
        context_temp = article.a_content
        context_html = etree.HTML(context_temp)
        temp['pic'] = article.a_pic
        temp['year'] = article.a_uploadTime.year
        temp['month'] = article.a_uploadTime.month
        temp['day'] = article.a_uploadTime.day
        temp['count'] = 0
        contents.append(temp)
    p = Paginator(contents, 2)
    if PIndex == '':
        PIndex = '1'
    PIndex = int(PIndex)
    contents2 = p.page(PIndex)
    has_next = contents2.has_next()
    has_prev = contents2.has_previous()
    Pnum = p.num_pages
    return contents2, PIndex, Pnum, has_next, has_prev