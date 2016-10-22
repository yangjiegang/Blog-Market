$(function(){
	var per_item = $.cookie("page_num");
	$("#slt").val(per_item);

	var oUnm = $("ul.navbar-right").find("li").eq(2);
	var oLogin = $("ul.navbar-right").find("li").eq(1);
	var oLogout = $("ul.navbar-right").find("li").eq(0);
	$.ajax({
		url:'/web/account/',
		type:'post',
		success:function(callback){
			var obj = jQuery.parseJSON(callback);
			window.unm = obj.unm;
			len = oUnm.find("a");
			len.text("欢迎："+obj.unm);
			if (len.text().length > 5) {
				oLogin.hide();
			} else {
				oUnm.hide();
				oLogout.hide();
				$(".GoodsList").each(function(k,v){
					var iUnmDom = $(this).find("span").find("p").eq(1).find("a");
					var iUnm = iUnmDom.text().slice(4,-1);
					iUnmDom.parent().text("登录后再联系卖家");
				});
			}
			$(".GoodsList").each(function(k,v){
				var iUnmDom = $(this).find("span").find("p").eq(1).find("a");
				var iUnm = iUnmDom.text().slice(4,-1);
				if (iUnm){
					if(window.unm == iUnm){
						iUnmDom.parent().text("卖家： 自己");
					}
				}
			});
			if($("#talk").text().slice(4,-1) == window.unm){
				$("#talk").parent().text("卖家： 自己");
			}
		}
	});
});
function favor(doc,id){
	$.ajax({
		url:'/web/addLike/',
		data:{nid:id},
		type:'post',
		success:function(callback){
			var obj = jQuery.parseJSON(callback);
			if(obj.status == 1){
				var temp = '赞:'+ obj.data;
				$(doc).text(temp);
			}else{
				alert(obj.message);
			}
		}
	});
};
function reply(doc,id){
	var txt = $(doc).parent().next();
	$.ajax({
		url:'/web/getReply/',
		data:{nid:id},
		type:'post',
		success:function(callback){
			var obj = jQuery.parseJSON(callback);
			txt.find('.history').empty();
			$.each(obj,function(k,v){
				temp = "<p> 在 "+  v.create_date + "-> 用户" +  v.users__username + " 说: " + v.content + "</p>";
				txt.find('.history').append(temp);
			});
		}
	});
	txt.toggleClass('hide');
};
function submit(doc,id){
	$('#shade').removeClass('hide');
	var value = $(doc).prev().val();
	$(doc).prev().val('');
	$.ajax({
		url:'/web/submitReply/',
		data:{nid:id,data:value},
		type:'post',
		success:function(callback){
			back = jQuery.parseJSON(callback);
			if(back.status==1){
				temp = "<p> 在: " + back.data.create_date + " 用户:" +  back.data.users__username + " 说: " + back.data.content + "</p>";
				$(doc).parent().parent().find(".history").append(temp);
				reply_count = '评论数:' + back.data.reply_count;
				$('.reply_count').text(reply_count);
			}else{
				alert('无效的评论！')
			}
			$('#shade').addClass('hide');
		}
	});
};
function sendmsg(){
	var value = $('#msgtxt').val();
	$('#msgtxt').val('');
	$.ajax({
		url:'/web/SendMsg/',
		data:{data:value},
		type:'post',
		success:function(callback){
			back = jQuery.parseJSON(callback);
			if(back.status==1){
				var create_date = back.data.create_date;
				var username = back.data.username;
				var msg = "<div><p>用户："+username+" 在 "+create_date+" 说道: "+value+"</p></div>";
			}else{
				alert('请先登录！')
			}
		}
	});
};
window.is_first = 1;
function getmsg(){
	if(window.is_first == 1){
		$.ajax({
			url:'/web/getChat/',
			type:'post',
			success:function(callback){
				back = jQuery.parseJSON(callback);
				window.last_id = back[0].id;
				back = back.reverse();
				$.each(back,function(k,v){
					temp  = "<div><p>"+ v.create_date + "</p><p>" + v.user__username+" 说道: "+ v.content +"</p></div>";
					$('.pool').append(temp);
				});
				window.is_first = 0;
				var ht = document.getElementById("pool").scrollHeight;
				document.getElementById("pool").scrollTop = ht;
			}
		});
	}else{
		$.ajax({
			url:'/web/getChat2/',
			data:{last_id:window.last_id},
			type:'post',
			success:function(callback){
				back = jQuery.parseJSON(callback);
				if(back.length > 0){
					window.last_id = back[back.length-1].id;
					$.each(back,function(k,v){
						temp  = "<div><p>"+ v.create_date + "</p><p>" + v.user__username+" 说道: "+ v.content +"</p></div>";
						$('.pool').append(temp);
					});
					var ht = document.getElementById("pool").scrollHeight;
					document.getElementById("pool").scrollTop = ht;
				}
			}
		});
	}
};
function changepageitem(arg){
	var value = $(arg).val();
	$.cookie("page_num",value,{path:"/"});
}
function Contact(dom,nid){
	window.salesId = nid;
	$.ajax({
		url:"/web/sales/",
		data:{uid:window.salesId},
		type:"post",
		success:function(callback){
			callback = jQuery.parseJSON(callback);
			console.log(callback);
		}
	}); 
	window.open("/web/sales/");
}
window.flagBuyerId = 1;
function Pull(){
	$.ajax({
		url:"/web/sales/",
		type:"post",
		success:function(callback){
			callback = jQuery.parseJSON(callback);
			window.last_id = callback[0].id;
			callback = callback.reverse();
			var divSales = $("#sales");
			$.each(callback,function(k,v){
				var temp = "<p> 在 "+  v.create_date + "-> 用户" +  v.user__username + " 说: " + v.content + "</p>";
				divSales.append(temp);
			});
		}
	});
	$.ajax({
		url:"/web/buyer/",
		type:"post",
		success:function(callback){
			callback = jQuery.parseJSON(callback);
			var divBuyer = $("#buyer");
			$.each(callback,function(k,v){
				if(window.flagBuyerId == 1){
					window.BuyerId = v.user__id;
					window.flagBuyerId = 0;
				}; 
				var temp = "<p> 在 "+  v.create_date + "-> 用户" +  v.user__username + " 说: " + v.content + "</p>";
				divBuyer.append(temp);
			});
		}
	});
	var ht = document.getElementById("record").scrollHeight;
	document.getElementById("record").scrollTop = ht;
}
function SendDialog(){
	var value = $('#msgtxt').val();
	$('#msgtxt').val('');
	$.ajax({
		url:'/web/SendMsg/',
		data:{data:value},
		type:'post',
		success:function(callback){
			back = jQuery.parseJSON(callback);
			if(back.status==1){
			}else{
				alert('请先登录！')
			}
		}
	});
};
window.is_one = 1;
function GetDialog(){
	if(window.is_one == 1){
		Pull();
		window.is_one = 0;
	}else{
		$.ajax({
			url:'/web/sales/',
			data:{last_id:window.last_id,},
			type:'post',
			success:function(callback){
				back = jQuery.parseJSON(callback);
				if(back.length > 0){
					window.last_id = back[back.length-1].id;
					$.each(back,function(k,v){
						if (v.user__id != window.BuyerId){
							var temp = "<p>"+  v.create_date + "-> 卖家" +  v.user__username + " 说: " + v.content + "</p>";
							$("#sales").append(temp);
						}else{
							var temp = "<p>"+  v.create_date + "-> 买家" +  v.user__username + " 说: " + v.content + "</p>";
							$("#buyer").append(temp);
						}
					});
					var ht = document.getElementById("record").scrollHeight;
					document.getElementById("record").scrollTop = ht;
				}
			}
		});
	}
};
function Market(){
	var DivLeft = $(".left");
	var DivRight = $(".right");
	DivLeft.click(function(){
		window.location.href="/web/upload/";
	});
	DivRight.click(function(){
		window.location.href="/web/goodslist/";
	});
}