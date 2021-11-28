$(document).ready(function () {
  $('.sidenav').sidenav({
    edge: "right",
    draggable: true
  });


  $(document).ready(function () {
    $('select').formSelect();
  });

  // This makes the entire div of book cards clickable.
  // The code is borrowed from https://css-tricks.com/snippets/jquery/make-entire-div-clickable/
  $(".book-card").click(function () {
    window.location = $(this).find("a").attr("href");
    return false;
  });

});