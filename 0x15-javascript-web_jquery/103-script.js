$(document).ready(function () {
  function translate () {
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
  }
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
  $('INPUT#btn_translate').click(translate);
});
