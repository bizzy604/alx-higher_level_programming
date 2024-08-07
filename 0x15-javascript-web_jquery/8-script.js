$(
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const results = data.results;
      $.each(results, function (index, value) {
        const title = value.title;
        $('#list_movies').append('<li>' + title + '</li>');
      });
    }
  })
);
