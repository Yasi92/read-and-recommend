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



// This method has been borrowed from (https://www.freakyjolly.com/custom-jquery-function-read-more-and-read-less/)

  function AddReadMore() {
    //This limit you can set after how much characters you want to show Read More.
    var carLmt = 380;
    // Text to show when text is collapsed
    var readMoreTxt = " ... Read More";
    // Text to show when text is expanded
    var readLessTxt = " Read Less";


    //Traverse all selectors with this class and manupulate HTML part to show Read More
    $(".addReadMore").each(function() {
      
      var allstr = $(this).text();
      if (allstr.length > carLmt) {
          var firstSet = allstr.substring(0, carLmt);
          var secdHalf = allstr.substring(carLmt, allstr.length);
          var strtoadd = firstSet + "<span class='SecSec'>" + secdHalf +
          "</span><span class='readMore'  title='Click to Show More'>" +
          readMoreTxt + "</span><span class='readLess' title='Click to Show Less'>" +
          readLessTxt + "</span>";
          $(this).html(strtoadd);
      }

    });
    //Read More and Read Less Click Event binding
    $(document).on("click", ".readMore,.readLess", function() {
        $(this).closest(".addReadMore").toggleClass("showlesscontent showmorecontent");
    });
}


$(function() {
    //Calling function after Page Load
    AddReadMore();
});

// This function display books on home page in a max number and loads more books on click 
// The method has been learned from this tutorial (https://www.youtube.com/watch?v=XFXDZrjimrY)

$(".book-card").slice(0, 18).show();

$(".loadMore").on("click", function(){
  $(".book-card:hidden").slice(0, 18).show();

  if($(".card-book:hidden").length == 0){
    $(".loadMore").fadeOut();
  }
})

// This function display books added by user on profile page in a max number and loads more books on click  
$(".collection-item").slice(0, 6).show();

if($(".collection-item:hidden").length != 0){
  $(".loadMoreBooks").show();
}

$(".loadMoreBooks").on("click", function(){
  $(".collection-item:hidden").slice(0, 6).show();

  if($(".collection-item:hidden").length == 0){
    $(".loadMoreBooks").fadeOut();
  }
})

// This function display books added by user on profile page in a max number and loads more books on click  
$(".collection-item-review").slice(0, 4).show();
if($(".collection-item-review:hidden").length != 0){
  $(".loadMoreReview").show();
}


$(".loadMoreReview").on("click", function(){
  $(".collection-item-review:hidden").slice(0, 4).show();

  if($(".collection-item-review:hidden").length == 0){
    $(".loadMoreReview").fadeOut();
  }
})



});