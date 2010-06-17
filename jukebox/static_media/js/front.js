
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

    $('table.sorted').tablesorter(
    {
      headers: {
          0: { sorter: true },
          1: { sorter: 'anchor_text' },
          2: { sorter: 'anchor_text' },
          3: { sorter: true }
        },
        sortList: [[0,0], [1,0]],
        widgets: ['zebra']
    });
});

