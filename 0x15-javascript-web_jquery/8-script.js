$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function (movies) {
    $.each(movies.results, function (i, result) {
      $('UL#list_movies').append('<li>' + result.title + '</li>');
    });
  }
});
