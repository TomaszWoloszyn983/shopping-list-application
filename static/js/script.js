document.addEventListener("DOMContentLoaded", function() {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

});

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initialization
  document.addEventListener('DOMContentLoaded', function() {
    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
});

// Modal initialization
document.addEventListener('DOMContentLoaded', function() {
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal, {
    opacity:0.8,
    inDuration:300,
    outDUration:400
  });
});


