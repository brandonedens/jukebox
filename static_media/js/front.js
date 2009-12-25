
$(document).ready(
  function() {

    $('.panel').hover(
      function() {
        $(".cover", this).stop().animate({top:'-200px'},
                                         {queue:false,duration:300});
      },
      function() {
        $(".cover", this).stop().animate({top:'0px'},
                                         {queue:false,duration:300});
      });
});

