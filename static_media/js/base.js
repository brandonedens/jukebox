
// Custom tablesorter parser to extract text from anchor elements
$.tablesorter.addParser({
	id: "anchor_text",
	is: function(s) {
		return false;
	},
	format: function(s) {
      return $(s).text();
	},
	type: "text"
});

$(document).ready(
  function()
  {
    $(".messages").fadeIn('slow');
    $(".button").append('<span></span>');
  });

