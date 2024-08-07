$(
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const name = data.name;
      $('#character').append(name);
    }
  })
);
