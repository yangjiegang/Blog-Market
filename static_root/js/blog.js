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
				temp = "<p>"+  v.fields.users + ":" + v.fields.content + "->" + v.fields.create_date + "</p>";
				txt.find('.history').append(temp);
			});
		}
	});
	txt.toggleClass('hide');
};
function submit(doc,id){
	$('#shade').removeClass('hide');
	var value = $(doc).prev().val();
	//console.log(value);
	$(doc).prev().val('');
	$.ajax({
		url:'/web/submitReply/',
		data:{nid:id,data:value},
		type:'post',
		success:function(callback){
			//console.log(callback)
			back = jQuery.parseJSON(callback);
			//console.log(back.message)
			if(back.status==1){
				//console.log(back);
				temp = "<p>"+ " user:" +  back.data.users__username + " say: " + back.data.content + " at: " + back.data.create_date + "</p>";
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
			//console.log(back);
			if(back.status==1){
				var create_date = back.data.create_date;
				var username = back.data.username;
				var msg = "<div><p>用户："+username+" 在 "+create_date+" 说道: "+value+"</p></div>";
				$('.pool').append(msg);
				//console.log(back);
			}else{
				alert('请先登录！')
			}
		}
	});
};

setTimeout(getmsg,1000);
//setinterval(getmsg,2000);
window.is_first = 1;
function getmsg(){
	if(window.is_first = 1){
		$.ajax({
			url:'/web/getChat/',
			type:'post',
			success:function(callback){
				back = jQuery.parseJSON(callback);
				back = back.reverse();
				window.last_id = back[0].id;
				//console.log(window.last_id);
				$.each(back,function(k,v){
					temp  = "<div><p>"+ v.user__username+" 说道: "+ v.content +"</p></div>";
					$('.pool').append(temp);
					//console.log(v.fields);
				});
				window.is_first = 0;
				//console.log(window.is_first);
			}
		});
	}else{
		$.ajax({
			url:'/web/getChat2/',
			data:{last_id:window.last_id},
			type:'post',
			success:function(){
				//console.log('ok');
			}
		});
	}
};
function login(){
	$.ajax({
		url:'/web/loginBlog/',
		type:'post',
		success:function(callback){
		}
	});
}
function logout(){
	$.ajax({
		url:'/web/logoutBlog/',
		type:'post',
		success:function(callback){
		}
	});
}
function logShow()
{
	var oUnm = $("ul.navbar-right").find("li").eq(2);
	var oLogin = $("ul.navbar-right").find("li").eq(1);
	var oLogout = $("ul.navbar-right").find("li").eq(0);
	if (oUnm.text().length > 6) {
		oLogin.hide();
	} else {
		oUnm.hide();
		oLogout.hide();
	}
}
function changepageitem(arg){
	var value = $(arg).val();
	$.cookie("page_num",value,{path:"/"});
}
$(function(){
	var per_item = $.cookie("page_num");
	$("#slt").val(per_item);
	logShow();
});
