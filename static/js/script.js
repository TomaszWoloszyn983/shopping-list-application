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
    let elems = document.querySelectorAll('.collapsible');
    M.Collapsible.init(elems);
});

// Modal initialization
document.addEventListener('DOMContentLoaded', function() {
  let elems = document.querySelectorAll('.modal');
  M.Modal.init(elems, {
    opacity:0.8,
    inDuration:300,
    outDUration:400
  });
});
