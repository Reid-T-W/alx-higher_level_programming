$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: function (people) {
    console.log(people);
    $('div#character').append(people.name);
  }
});
