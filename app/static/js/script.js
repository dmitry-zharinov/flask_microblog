$( document ).ready(function() {
    $(".nav li").on("click", function() {
            $(".nav li").removeClass("nav-item active");
            $(this).addClass("nav-item active");
          });
});