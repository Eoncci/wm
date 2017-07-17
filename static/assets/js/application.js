$(function() {

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
  
  // 获取预约状态
  $('#statusform').submit(function (e) {
      e.preventDefault();
      $.post('/washingmachine/query',function (res) {
        console.log(res);
        var temp = $(
             '<div class="dn"><p>正在派送中，</p>\
              <p>联系人姓名：'+ res.tel +'</p>\
              <p>房间地址为：</p>\
              <p>租赁时间为：'+ res.star + ' - ' + res.end +'</p></div>'
            );
        $('#statusinfo').append(temp);
        temp.fadeIn();
      });
  });

});
