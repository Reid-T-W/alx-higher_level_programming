$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (result) {
      $('DIV#hello').append(result.hello);
    }
  });
});
