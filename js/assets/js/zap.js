$(document).ready(function () {
  $("#strength-slider").on("input change", e => {
    $("#strength-show").html(parseInt(e.target.value / 100))
  })
})