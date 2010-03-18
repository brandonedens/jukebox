
$(document).ready(function()
    {
      $('a#copyrighted').click(
        function() {
          $('#id_reason').val("Song is a well known copyrighted song and cannot be accepted into Jukebox until further investigation is performed.");
          return false;
        });
      $('a#too-long').click(
        function() {
          $('#id_reason').val("Song is exceeds the 6 minute duration limit. Please reupload the song in sections with each section being less than 6 minutes in length.");
          return false;
        });
       $('a#poor-quality').click(
        function() {
          $('#id_reason').val("Song is poor in quality either too low a sample rate or encoded with too low a bitrate. Please reencode and upload your audio with higher quality.");
          return false;
        });
    }
);

