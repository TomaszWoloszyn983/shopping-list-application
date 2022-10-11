document.addEventListener('DOMContentLoaded', function() {
    print("Hello from js sidebar")
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });