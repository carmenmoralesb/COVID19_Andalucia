$(function () {
  $("#something").on("input", function () {
    var url = "/app/municipio/detail/" + 123;
    var opt = $('option[value="' + $(this).val() + '"]');
    if (opt.attr("id") != null && opt.attr("id") != undefined) {
      document.location.href = url.replace("123", opt.attr("id"));
    }
  });
});
