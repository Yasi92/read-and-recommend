$(document).ready(function () {

  // It toggles the book cards and fade them into the window on page load.
  var cards = document.querySelectorAll('.book-card');

  cards.forEach((card) => {

    card.classList.add('show');

  });


  // Sets the side nav to open from the right side of the window
  $('.sidenav').sidenav({
    edge: "right"
  });


  // Initialize the form select in materialize
  $('select').formSelect();


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
    $(".addReadMore").each(function () {
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
    $(document).on("click", ".readMore,.readLess", function () {
      $(this).closest(".addReadMore").toggleClass("showlesscontent showmorecontent");
    });
  }


  //Calling function after Page Load
  $(function () {
    AddReadMore();
  });


  // The load More button and slicing items on the profile page and books.html is learned from [here](https://www.youtube.com/watch?v=XFXDZrjimrY)
  // This function display books added by user on profile page in limited numbers and loads more books on click  
  // It slices the books added by the user on the profile page
  $(".collection-item").slice(0, 6).show();


  // It displays the loadmore buttton if there are hidden books in the list
  if ($(".collection-item:hidden").length != 0) {
    $(".loadMoreBooks").show();
  }

  // It displays more books on click on the loadMore button
  $(".loadMoreBooks").on("click", function () {
    $(".collection-item:hidden").slice(0, 6).show();

    if ($(".collection-item:hidden").length == 0) {
      $(".loadMoreBooks").fadeOut();
    }
  })


  // This function display reviews added by user on profile page in a limited numbers and loads more reviews on click  
  $(".collection-item-review").slice(0, 4).show();


  if ($(".collection-item-review:hidden").length != 0) {
    $(".loadMoreReview").show();
  }


  $(".loadMoreReview").on("click", function () {
    $(".collection-item-review:hidden").slice(0, 4).show();

    if ($(".collection-item-review:hidden").length == 0) {
      $(".loadMoreReview").fadeOut();
    }
  })



  // Calls the modals
  $('.modal').modal();


  // Gets the year we are in, to display in the footer
  var date = new Date().getFullYear();
  document.getElementById("year").innerHTML = date;


  // The history back button is learned form https://css-tricks.com/snippets/javascript/go-back-button/ and w3school 
  $(".back-btn").on("click", function () {
    window.history.go(-1);
    return false;
  })

  $(".edit-back-btn").on("click", function () {
    window.history.go(-1);
    return false;
  })


  /* The method has been learned from this tutorial (https://www.youtube.com/watch?v=US_3XvufMLU) and
   manipulated by me to make it responsive to all screen sizes.*/

  /* Get the height of header and footer on different screen size to push 
    the footer to the bottom of the page regardless of the size of content.*/
  setInterval(function(){
    var header = document.querySelector("header").offsetHeight;
    var footer = document.querySelector("footer").offsetHeight;
    document.getElementById("main").style.minHeight = "calc( 100vh - " + header + "px" + " - " + footer + "px )";


    // This fixes the position of the back-to-top button on top of the footer
    document.getElementById("myBtn").style.bottom = footer + "px ";
  }, 500);  

  
  /* The back to top button is learned from this thread on stackoverflow
   (https://stackoverflow.com/questions/14249998/jquery-back-to-top)*/

  //check if window scroll is < 100
  if ($(window).scrollTop() < 100) {
    $('#myBtn').hide();
  }


  // Checks if the window scroll is more than 500 and then displays the button
  $("body").on("scroll", function () {
    if ($(this).scrollTop() > 500) {
      $('#myBtn').fadeIn();
    } else {
      $('#myBtn').fadeOut();
    }
  });

  // Scrolls up to the top of the page on click
  $("#myBtn").click(function () {
    $("html, body").animate({
      scrollTop: 0
    }, 1000);
    return false;
  })


  // It hides the back button on the books.html if the previous url is add_book
  // And adds margin-top to the row
  if (document.referrer.includes("add_book")) {
    $(".back-btn").hide();
    $(".bottom-bordered-row").css("margin-top", "3rem");
  }

})