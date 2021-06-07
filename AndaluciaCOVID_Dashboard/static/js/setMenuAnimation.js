$(document).ready(function () {
  sidebarStatus = false;
  $(".closebtn").click(function () {
    if (sidebarStatus == false) {
      $("#nav").animate(
        {
          marginLeft: "0px",
          opacity: "1",
        },
        1000
      );
      $(".main").animate(
        {
          marginLeft: "200px",
          opacity: "1",
        },
        1000
      );
      sidebarStatus = true;
    } else {
      $("#nav").animate(
        {
          marginLeft: "-150px",
          opacity: "1",
        },
        1000
      );
      $(".main").animate(
        {
          marginLeft: "0px",
          opacity: "1",
        },
        1000
      );
      sidebarStatus = false;
    }
  });
});
