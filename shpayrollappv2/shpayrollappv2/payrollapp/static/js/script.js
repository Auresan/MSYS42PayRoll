const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})