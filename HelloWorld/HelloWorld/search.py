from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators import csrf
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
import imghdr
from django import forms
from django.core.files.base import ContentFile 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)



 
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
# @csrf_protect
def process(request):
    # data = {
    #     'name': 'Vitor',
    #     'location': 'Finland',
    #     'is_active': True,
    #     'count': 28
    # }
    receive_data = json.loads(request.body.decode())
    result={}
    result['cx']=float(receive_data['sl'])+float(receive_data['yaw'])
    return JsonResponse(result)

def ProcessImg(request):
    if request.method == 'POST':
        
        #判断是否为有效的
        print(request.FILES)
        if request.FILES:
        # if request.FILES.get('png'): #img为upload.html中的input标签名称
            # print("w")
            # new_img = models.Profile(
            # avatar_thumbnail = request.FILES.get('img'),
            # name = request.FILES.get('img').name)
            # # new_img = models.Upload_img(
            # # img = request.FILES.get('img'),
            # # name = request.FILES.get('img').name
            # # )
            # type_list = ['.jpg','.png','.gif','.webp']
            # #判断上传图片格式
            # if os.path.splitext(new_img.name)[1].lower() in type_list:
            #     new_img.save()
        # return render(request,'blog1/processupload.html')
            return HttpResponse("fimg")
        return HttpResponse("dsds")

       

def getImg(request):
    file_content = ContentFile(request.FILES['img'].read())  
    img = ImageStore(name = request.FILES['img'].name, img = request.FILES['img'])  
    img.save()
    return HttpResponse("dsds")