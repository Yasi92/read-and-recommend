$(document).ready(function () {


  const cards = document.querySelectorAll('.book-card');

  cards.forEach((card) => {

    card.classList.add('show');

  });


  $('.sidenav').sidenav({
    edge: "right"
  });



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


  $(function () {
    //Calling function after Page Load
    AddReadMore();
  });



  // This function display books added by user on profile page in a max number and loads more books on click  
  $(".collection-item").slice(0, 6).show();

  if ($(".collection-item:hidden").length != 0) {
    $(".loadMoreBooks").show();
  }

  $(".loadMoreBooks").on("click", function () {
    $(".collection-item:hidden").slice(0, 6).show();

    if ($(".collection-item:hidden").length == 0) {
      $(".loadMoreBooks").fadeOut();
    }

  })



  $('.modal').modal();

  var date = new Date().getFullYear();
  document.getElementById("year").innerHTML = date;



  // The history back button is learned form https://css-tricks.com/snippets/javascript/go-back-button/ and w3school 
  $(".back-btn").on("click", function (e) {
    e.preventDefault();
    window.history.go(-1);
    return false;

  })


  // Get the height of header and footer on different screen size to push 
  // the footer to the bottom of the page regardless of the size of content.
  // The method has been learned from (https://www.youtube.com/watch?v=US_3XvufMLU) and manipulated by me to make it responsive to all screen sizes.
  var header = document.querySelector("header").offsetHeight;
  var footer = document.querySelector("footer").offsetHeight;

  document.getElementById("main").style.minHeight = "calc( 100vh - " + header + "px" + " - " + footer + "px )";


  // This function display reviews added by user on profile page in a max number and loads more reviews on click  
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





  //check if window scroll is < 100
  if ($(window).scrollTop() < 100) {
    $('#myBtn').hide();
  }

  $("body").on("scroll", function () {
    if ($(this).scrollTop() > 500) {
      $('#myBtn').fadeIn();
    } else {
      $('#myBtn').fadeOut();
    }
  });

  $("#myBtn").click(function () {
    $("html, body").animate({
      scrollTop: 0
    }, 1000);
    return false;
  })


  // Fixing the back-to-top button on top of the footer
  document.getElementById("myBtn").style.bottom = footer + "px ";




  if (document.referrer.includes("add_book")) {
    $(".back-btn").hide();
    $(".bottom-bordered-row").css("margin-top", "3rem");
  }





})