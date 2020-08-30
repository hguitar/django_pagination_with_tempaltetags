from django.shortcuts import render
from django.http import HttpResponse
from .models import dummy
from django.core.paginator import Paginator

# Create your views here.
def main(requset):
	datas = dummy.objects.all()
	num_per_page = requset.GET.get('num_per_page',20)
	paged = Paginator(datas,num_per_page)
	page_num = requset.GET.get('page', 1)
	a_page = paged.get_page(page_num)
	return render(requset,template_name = 'main/main.html',context={'datas':a_page,})