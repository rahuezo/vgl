function view_image(source, category, text) {
  var new_tag = '<a href="#" data-toggle="modal" data-target="#large-img-viewer" id="enlarge-img-btn" onclick="set_modal_image(this);">'
  var cat = category;

  $('#main-img-holder' + cat).html(new_tag + '<img src="' + source + '"></a>');
  $('.main-img-text').text(text);
}

function set_gallery_category(text) {
  $('.gallery-category').text(text);
}

// pick a default gallery viewer to show
function pick_default_viewer() {
  var default_gallery_viewer_id = $('.gallery-wrapper').get()[0].id;

  $('#' + default_gallery_viewer_id).addClass('active-display');
}

function set_modal_image(element) {
  var img_src = $(element).find('img').prop('src');

  $("#enlarged-image").attr("src", img_src);
}

function truncate_text(text, element) {
  var text_length = text.length;
  var optimal_length = 350;
  var seemore_btn_div = $(element + ' .reviewer-comment-text');

  if (text_length > optimal_length) {
    seemore_btn_div.append(text.substring(0, optimal_length));
    seemore_btn_div.append('…<br><br><a class="see-more btn btn-success" data-toggle="modal" data-target="#review-see-more"\
    value="' + element + '" onclick="show_focus_review(this);">See More</a>');
  }else {
    seemore_btn_div.text(text);
  }
}

function fix_review_size() {
  var number_of_reviews = $('.review-container').length;

  for (var i = 0; i < number_of_reviews; i++){
    var current_review = "#review" + (i + 1);
    var full_text = $(current_review + ' .full-text').attr('value');

    truncate_text(full_text, current_review);
  }
}

function show_focus_review(element) {
  var focused_review = $(element).attr('value');
  var review_modal = '#review-see-more';
  var review_modal_header = review_modal + ' .modal-header';
  var review_modal_body = review_modal + ' .modal-body';

  var modal_image = $(focused_review + ' img').attr('src');
  var modal_title = $(focused_review + ' strong').text();
  var modal_text = $(focused_review + ' .full-text').val();
  var modal_star_score = $(focused_review + ' .review-star-score').html();
  var modal_post_date = $(focused_review + ' .review-post-date').text().match(/Posted on: [aA-zZ]+ [0-9]{1,2}, [0-9]{4}/);

  $(review_modal_header).html('<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>');
  $(review_modal_header).append('<div class="text-left"><strong>' + modal_title + '</strong></div>');
  $(review_modal_header).append('<img src="' + modal_image + '" class="review-modal-img pull-left">');
  $(review_modal_header).append('<div class="pull-right">' + modal_star_score + "</div><br>");
  $(review_modal_header).append('<div class="pull-right">' + modal_post_date + "</div>");

  $(review_modal_body).html('<i class="fa fa-quote-left fa-2x fa-pull-left quote" aria-hidden="true"></i><br><div class="text-justify modal-review-text">' + modal_text + '</div><i class="fa fa-quote-right fa-2x fa-pull-right quote" aria-hidden="true"></i><br>');
}

$(document).ready(function() {
  fix_review_size();

  $('.cat-view-btn').click(function() {
    var corresponding_viewer_id = $(this).prop('name');
    var corresponding_viewer = $('#' + corresponding_viewer_id);

    $('.gallery-wrapper').removeClass('active-display');

    corresponding_viewer.addClass('active-display');
  });

    // end category view button


  $('.thumbnail-img-btn').click(function() {
    var img_object = $(this).find('img');
    var img_to_view = img_object.prop('src');
    var text_to_view = img_object.prop('title')
    var category = img_object.attr('data-category');

    console.log("CAT: ", category);

    $('.thumbnail-img-btn img').removeClass('current-img-indicator');
    img_object.addClass('current-img-indicator');

    view_image(img_to_view, category, text_to_view);

  });


// gallery

  $(document).scroll(function () {
    console.log($(window).scrollTop());
    if ($(window).scrollTop() > 88) {
      // $('#navbar').addClass('navbar-fixed-top');
      // $('#top-links').addClass('navbar-right');
      // $('#page-brand-onscroll').show();
      // $('.first-gallery-element').addClass('scroll-padding');
    }
    if ($(window).scrollTop() < 88) {
      // $('#navbar').removeClass('navbar-fixed-top');
      // $('#top-links').removeClass('navbar-right');
      // $('#page-brand-onscroll').hide();
      // $('.first-gallery-element').removeClass('scroll-padding');
    }

    if ($(this).scrollTop() > 50) {
          $('#back-to-top').fadeIn();
          console.log("show top");
      } else {
          $('#back-to-top').fadeOut();
          console.log("hide top");
      }
      });
      // scroll body to 0px on click
      $('#back-to-top').click(function () {
          $('#back-to-top').tooltip('hide');
          $('body,html').animate({
              scrollTop: 0
          }, 800);
          return false;
      });

      $('#back-to-top').tooltip('show');
  });


$(function() {
    //----- OPEN
    $('[data-popup-open]').on('click', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-open');
        $('[data-popup="' + targeted_popup_class + '"]').fadeIn(350);

        e.preventDefault();
    });

    //----- CLOSE
    $('[data-popup-close]').on('click', function(e)  {
        var targeted_popup_class = jQuery(this).attr('data-popup-close');
        $('[data-popup="' + targeted_popup_class + '"]').fadeOut(350);

        e.preventDefault();
    });
});
