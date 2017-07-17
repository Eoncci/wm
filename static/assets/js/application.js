$(function() {

  // 验证手机号
  function checkPhone(phone){
      if(!(/^1[34578]\d{9}$/.test(phone))){
          return false;
      }
      return true;
  }

  /*-----------------------------------------------------------------------------------*/
  /*  Anchor Link
  /*-----------------------------------------------------------------------------------*/
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
      || location.hostname == this.hostname) {

      var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
    if (target.length) {
      $('html,body').animate({
        scrollTop: target.offset().top
      }, 1000);
        return false;
      }
    }
  });

  /*-----------------------------------------------------------------------------------*/
  /*  Tooltips
  /*-----------------------------------------------------------------------------------*/
  $('.tooltip-side-nav a').tooltip();
  
  // 预约申请
  $('#signform').submit(function (e) {
      e.preventDefault();
      if( !checkPhone($('#tel').val()) ){
          swal({
            html: true ,
            title: '提示',
            text: '电话号码格式不正确，请填写手机号码', 
            type: 'warning',
            confirmButtonText: '确定', 
          });
          $('#tel').focus();
          return false;
      }
      if( !$.trim($('#name').val()) ){
          swal({
            html: true ,
            title: '提示',
            text: '请填写姓名', 
            type: 'warning',
            confirmButtonText: '确定', 
          });
          $('#name').focus();
          return false;
      }
      if( !$.trim($('#address').val()) ){
          swal({
            html: true ,
            title: '提示',
            text: '请填写姓名', 
            type: 'warning',
            confirmButtonText: '确定', 
          });
          $('#address').focus();
          return false;
      }

      $.post('/washingmachine/wm_order', $('#signform').serialize() ,function (res) {
        console.log(res);
        if(res.match('success')){
          swal({ 
            html: true ,
            title: '预约成功',
            text: '可通过电话号码<a href="/washingmachine/status">查看申请状态</a>', 
            type: 'success',
            confirmButtonText: '确定', 
          });
        }else{
          swal({
            html: true ,
            title: '提示',
            text: JSON.parse(res).error, 
            type: 'warning',
            confirmButtonText: '确定', 
          });
        }
      });
  });


  // 获取预约状态
  $('#statusform').submit(function (e) {
      e.preventDefault();
      if( !checkPhone($('#tel').val()) ){
          swal({
            html: true ,
            title: '提示',
            text: '电话号码格式不正确，请填写手机号码', 
            type: 'warning',
            confirmButtonText: '确定', 
          });
          $('#tel').focus();
          return false;
      }
      $.post('/washingmachine/query', $('#statusform').serialize() ,function (res) {
        res = JSON.parse(res);
        var temp = $(
             '<div class="dn"><p>正在派送中，</p>\
              <p>联系人电话：'+ res.tel +'</p>\
              <p>租赁时间为：'+ res.start.substring(0, 10) + ' - ' + res.end.substring(0, 10) +'</p></div>'
            );
        $('#statusinfo').append(temp);
        temp.fadeIn();
      });
  });



});
