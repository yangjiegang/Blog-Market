#coding:UTF-8
from django.utils.safestring import mark_safe
from web import common

def Pager(page,numPage):
#	page = common.intPage(page, 1)
	htmlPage = []

	FirstPage = "<a href='/web/blog/1/'>首页</a>"
	htmlPage.append(FirstPage)

	if page<=1:
		prevPage="<a href='#'>上一页</a>"
	else:
		prevPage="<a href='/web/blog/%d'>上一页</a>"%(page-1)
	htmlPage.append(prevPage)

	begin=page-2
	end=page+2

	if numPage<3:
		begin=0
		page=numPage
	else:
		if page<2:
			begin=0
			end=3
		else:
			if page+2>numPage:
				begin=page-2
				end=numPage
			else:
				begin=page-2
				end=page+2

	for i in range(begin, end):
		if page==i+1:
			aHtml = "<a style='color:red' href='/web/blog/%d/'>-%d-</a>" % (i + 1, i + 1)
		else:
			aHtml = "<a href='/web/blog/%d/'>-%d-</a>" % (i + 1, i + 1)
		htmlPage.append(aHtml)

	nextHtml="<a href='/web/blog/%d/'>下一页</a>"%(page+1)
	htmlPage.append(nextHtml)

	LastPage = "<a href='/web/blog/%d/'>尾页</a>" % (numPage)
	htmlPage.append(LastPage)

	page_string = mark_safe(''.join(htmlPage))
	return page_string


class PageInfo:
	def __init__(self,current_page,numPage,per_item=5):
		self.CurrentPage=current_page
		self.NumPage=numPage
		self.PerItem=per_item

#	@property
	def start(self):
		return (self.CurrentPage-1)*self.PerItem
#	@property
	def end(self):
		return self.CurrentPage*self.PerItem
#	@property
	def numPage(self):
		temp = divmod(self.NumPage,self.PerItem)
		if temp[1] == 0:
			num_page = temp[0]
		else:
			num_page = temp[0] + 1
		return num_page