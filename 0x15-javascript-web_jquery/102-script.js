$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/',
      type: 'GET',
      data: {
        lang: $('INPUT#language_code').val()
      },
      success: function (result) {
        $('DIV#hello').empty();
        $('DIV#hello').append(result.hello);
      }
    });
  });
});
