
$(document).ready(function()
    {
      $('table.sorted').tablesorter(
      {
        headers: {
          0: { sorter: 'anchor_text'},
          1: { sorter: 'anchor_text'},
          3: { sorter: false },
          4: { sorter: false }
        },
        sortList: [[0,0], [1,0]],
        widgets: ['zebra']
      });
    }
);

