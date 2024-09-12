$(document).ready(function () {
  var innerRepeater = $(".inner-repeater").repeater({
    repeaters: [
      {
        selector: ".deep-inner-repeater",
      },
      {
        selector: ".deep-inner-repeater1",
      },
    ],
  });

  // Uncomment and use $repeater.setList to set initial values
});
