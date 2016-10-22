#coding:UTF-8
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from web import models, common, htmlTool
import json, time, os, datetime
from django.core import serializers
from django import forms
# Create your views here.
def index(request):
	try:
		lastNews = models.News.objects.all().order_by("-id")[0:2].values("title","summary")
		hotNews = models.News.objects.all().order_by("-favor_count")[0:2].values("title","summary")
		ret = {"lastNews":lastNews,'hotNews':hotNews}
	except:
		ret = {"lastNews":"Error!",'hotNews':"Null!"}
	return render_to_response("web/index.html",ret)
def addLike(request):
	ret = {'status': 0, 'data': '', 'message': ''}
	try:
		id = request.POST.get('nid')
		newsObj = models.News.objects.get(id=id)
		temp = newsObj.favor_count + 1
		newsObj.favor_count = temp
		newsObj.save()
		ret['status'] = 1
		ret['data'] = temp
	except:
		ret['message'] = "Error..."
	return HttpResponse(json.dumps(ret))
class CJsonEncoder(json.JSONEncoder):
	def default(self,obj):
		if isinstance(obj,datetime.datetime):
			return obj.strftime("%Y-%m-%d %H:%M:%S")
		elif isinstance(obj,date):
			return obj.strftime("%Y-%m-%d")
		else:
			return json.JSONEncoder.default(self,obj)
def getReply(request):
	id = request.POST.get('nid')
	reply_list = models.Reply.objects.filter(new__id=id).values('content','users__username','create_date')
	reply_list = list(reply_list)
	reply_list = json.dumps(reply_list,cls = CJsonEncoder)
	return HttpResponse(reply_list)
def submitReply(request):
	ret = {'status': 0, 'data': '', 'message': ''}
	try:
		nid = request.POST.get('nid')
		data = request.POST.get('data')
		newsObj = models.News.objects.get(id=nid)
		obj = models.Reply.objects.create(content=data, new=models.News.objects.get(id=nid),
										  users=models.Admin.objects.get(id=request.session['current_uid']))
		temp = newsObj.reply_count + 1
		newsObj.reply_count = temp
		newsObj.save()
		ret['data'] = {'reply_count': temp, 'content': obj.content, 'users__username': obj.users.username,
					   'create_date': obj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
		ret['status'] = 1
	except:
		ret['message'] = "Wrong!"
	return HttpResponse(json.dumps(ret))
def SendMsg(request):
	ret = {'status': 0, 'data': '', 'message': ''}
	try:
		value = request.POST.get('data')
		userObj = models.Admin.objects.get(id=request.session['current_uid'])
		chatObj = models.Chat.objects.create(content=value, user=userObj)
		ret['status'] = 1
		ret['data'] = {'username': userObj.username, 'content': chatObj.content,
					   'create_date': chatObj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
	except:
		ret['message'] = "Have not login!"
	return HttpResponse(json.dumps(ret))
def getChat(request):
	chatObj = models.Chat.objects.all().order_by('-id')[0:20].values('id', 'content', 'user__username','create_date')
	chatObj = list(chatObj)
	chatObj = json.dumps(chatObj,cls = CJsonEncoder)
	return HttpResponse(chatObj)
def getChat2(request):
	last_id = request.POST.get('last_id')
	chatObj = models.Chat.objects.filter(id__gt=last_id).values('id', 'content', 'user__username','create_date')
	chatObj = list(chatObj)
	chatObj = json.dumps(chatObj,cls = CJsonEncoder)
	return HttpResponse(chatObj)
def blog(request, page=1):
	temp = request.COOKIES.get("page_num",3)
	per_item = common.intPage(temp,3)
	page = common.intPage(page, 1)
	count = models.News.objects.all().count()
	pageObj = htmlTool.PageInfo(page,count,per_item)
	result = models.News.objects.all()[pageObj.start():pageObj.end()]
	page_string = htmlTool.Pager(page,pageObj.numPage())
	unm = request.session.get('current_unm',False)
	if(unm):
		ret = {'data': result, 'count': count, 'page': page_string,'unm':unm}
	else:
		ret = {'data': result, 'count': count, 'page': page_string}
	response =  render_to_response('web/blog.html', ret)
	response.set_cookie("page_num",per_item)
	return response
def Account(request):
	ret = {"unm":"", "uid":"","msg":""}
	unm = request.session.get('current_unm',False)
	uid = request.session.get('current_uid',False)
	if unm:
		ret["unm"]=unm
		ret["uid"]=uid
		return HttpResponse(json.dumps(ret))
	else:
		ret["msg"]="Null"
		return HttpResponse(json.dumps(ret))
def SignIn(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			currentObj = models.Admin.objects.get(username=username, password=password)
		except:
			ret={'msg':'无效的用户名或者密码!',}
			return render_to_response('web/signin.html',ret)
		if currentObj:
			request.session['current_unm'] = currentObj.username
			request.session['current_uid'] = currentObj.id
			return redirect('/web/')
		else:
			return render_to_response('web/signin.html')
	return render_to_response('web/signin.html')
def SignOut(request):
	try:
		del request.session['current_unm']
		del request.session['current_uid']
	except KeyError:
		print('KeyError!')
	return redirect('/web/SignIn/')
def NewsDetalis(request,pk):
	pk=int(pk)
	value = models.News.objects.get(id=pk)
	ul = models.News.objects.filter(id__range=(pk-3,pk+3)).values('id','title','url')
	ret = {'data': value,'ul':ul}
	return render_to_response('web/newsdetails.html', ret)
def GetContent(request):
	ret = {'status': 0, 'data': '', 'message': ''}
	if request.method == 'POST':
		nid = int(request.POST.get('nid'))
		_title = request.POST.get('_title')
	try:
		NewsObj = models.News.objects.get(id=nid,title=_title)
		ret['status']=1
		ret['data'] = {"content":NewsObj.content,"title":NewsObj.title}
	except:
		ret['message']='None!'
	return HttpResponse(json.dumps(ret))
def about(request):
	return render_to_response('web/about.html')
def SearchNews(request):
	question = request.POST.get("question")
	answer = models.News.objects.filter(title__icontains=question).values("title","summary","url",)
	count = answer.count()
	ret = {"answer":answer,"count":count,"question":question}
	return render_to_response("web/searchresult.html",ret)
def Market(request):
	return render_to_response("web/market.html")
class GoodsForm(forms.Form):
	name = forms.CharField(label="商品名称 ", max_length=20)
	value = forms.FloatField(label="挂售价格 ")
	descript = forms.CharField(label="简要描述 ", max_length=254)
	details = forms.CharField(label="详细描述 ",max_length=9999)
	goodsImg = forms.FileField()
def upload(request):
	if request.method == 'POST':
		gf = GoodsForm(request.POST, request.FILES)
		if gf.is_valid():
			handle_uploaded_file(request.FILES['goodsImg'])
			name = gf.cleaned_data['name']
			value = gf.cleaned_data['value']
			descript = gf.cleaned_data['descript']
			goodsImg = gf.cleaned_data['goodsImg']
			details = gf.cleaned_data['details']
			uid = request.session.get("current_uid")
			mg = models.Goods()
			mg.name=name
			mg.value=value
			mg.descript=descript
			mg.details=details
			mg.user_id=uid
			global file_name
			mg.goodsImg= "/%s"%(file_name)
			mg.save()
			return redirect("/web/management/")
	else:
		gf = GoodsForm()
		return render_to_response('web/upload.html',{'gf':gf})
def handle_uploaded_file(f):
	global file_name
	file_name = ""
	try:
		path = "static/upload" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
		if not os.path.exists(path):
			os.makedirs(path)
			file_name = path + f.name
			destination = open(file_name, 'wb+')
			for chunk in f.chunks():
				destination.write(chunk)
			destination.close()
	except:
		print("Upload_error!")
	return file_name
def SearchGoods(request):
	value = request.POST.get("SearchGoods")
	gdObj1 = models.Goods.objects.filter(name__icontains=value).values("id","name","value","goodsImg","descript", "user__id",'user__username')
	gdObj2 = models.Goods.objects.filter(descript__icontains=value).values("id","name","value","goodsImg","descript", "user__id",'user__username')
	count1 = gdObj1.count()
	count2 = gdObj2.count()
	ret = {"gdObj":"","count":"","value":value}
	if count1 != 0 and count2 != 0:
		gdObj1=list(gdObj1)
		gdObj2=list(gdObj2)
		for gd in gdObj1:
			if gd not in gdObj2:
				gdObj2.append(gd)
		count4 = len(gdObj2)
		ret["count"] = count4
		ret["gdObj"] = gdObj2
		return render_to_response("web/goodslist.html",ret)
	elif count1 != 0 and count2 == 0:
		ret["count"]=count1
		ret["gdObj"]=gdObj1
		return render_to_response("web/goodslist.html",ret)
	elif count1 == 0 and count2 != 0:
		ret["count"]=count2
		ret["gdObj"]=gdObj2
		return render_to_response("web/goodslist.html",ret)
	else:
		return render_to_response("web/goodslist.html",ret)
def GoodsList(request):
	gdObj = models.Goods.objects.all().values('id','name','value','descript', 'goodsImg', 'user__id',"user__username")
	count = gdObj.count()
	ret = {"gdObj":gdObj,"count":count}
	return render_to_response("web/goodslist.html",ret)
def GoodsDetails(request):
	goods_id = request.POST.get("gid")
	goods_id = int(goods_id)
	gdObj  = models.Goods.objects.filter(id = goods_id).values("id",'name','value','descript','details', 'goodsImg', 'user__id','user__username')
	ret = {"gdObj":gdObj,}
	return render_to_response("web/goodsdetails.html",ret)
#global gid
gid=0
def payment(request,way):
	global gid
	if way=="make":
		#global gid
		gid = request.POST.get("gid")
		gdObj = models.Goods.objects.get(id=gid)
		return render_to_response("web/payment.html",{"gdObj":gdObj})
	elif way=="done":
		reciever = request.POST.get("reciever")
		address = request.POST.get("address")
		phone = request.POST.get("phone")
		buyerName = request.session.get("current_unm")
		buyer=models.Admin.objects.get(username=buyerName)
		#global gid
		gdObj = models.Goods.objects.get(id=gid)#借用上次的gid
		goods = gdObj
#		pay = gdObj.value
#		sales = gdObj.user
		models.Orders.objects.get_or_create(reciever=reciever,address=address,phone=phone,buyer=buyer,goods=goods)
		return redirect("/web/management/")
def Management(request):
	uid = request.session.get("current_uid")
	gdSales = models.Goods.objects.filter(user__id=uid).values("name","value")
	orders = models.Orders.objects.filter(buyer__id=uid).values("goods__name","goods__value","goods__user__username")
	ret={"gdSales":gdSales,"orders":orders}
#	print(ret)
	return render_to_response("web/management.html",ret)

#global salesId,buyerId
salesId=0
buyerId=0
def Sales(request):
	global salesId
	global buyerId
	if request.method == 'POST':
		try:
			sales_id = request.POST.get("uid")
			last_id = request.POST.get("last_id")
			if (last_id == None) and (sales_id != None):
				#global salesId
				salesId = sales_id
				return HttpResponse(json.dumps("Go next page."))
			elif (last_id == None) and (sales_id == None):
				#global salesId
				sales = models.Chat.objects.filter(user__id=salesId).order_by('-id')[0:2].values('id', 'content', 'user__username','create_date')
				obj = list(sales)
				obj = json.dumps(obj,cls = CJsonEncoder)
				return HttpResponse(obj)
			else:
				#global salesId
				buyer_id = request.session.get('current_uid',default=None)
				if buyer_id != salesId and buyerId == 0:
					#global buyerId
					buyerId = buyer_id
				elif buyer_id == salesId:
					buyer_id = buyerId
				list_tmp = [buyerId, salesId]
				obj = models.Chat.objects.filter(user__id__in=list_tmp,id__gt=last_id).values('id', 'content', 'user__username','create_date','user__id')
				obj = list(obj)
				obj = json.dumps(obj,cls = CJsonEncoder)
				return HttpResponse(obj)
		except:
			pass
	else:
		return render_to_response("web/contact.html")
def Buyer(request):
	global salesId
	global buyerId
	if request.method == 'POST':
		buyer_id = request.session.get('current_uid',default=None)
#		global salesId,buyerId
		buyer_id = int(buyer_id)
		salesId = int(salesId)
		buyerId = int(buyerId)
		if buyer_id == salesId:
			buyer_id = buyerId
		buyer = models.Chat.objects.filter(user__id=buyer_id).order_by('-id')[0:2].values('id', 'content', 'user__username','create_date','user__id')
		buyer = list(buyer)
		buyer = json.dumps(buyer,cls = CJsonEncoder)
		return HttpResponse(buyer)