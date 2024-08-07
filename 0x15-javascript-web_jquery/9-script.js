$(
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const value = data.hello;
      $('#hello').append(value);
    }
  })
);
