/* jshint esversion: 11 */

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

// Messages Timeout function
let messages = document.getElementById("message");
if (messages == null){
  console.log("No message displayed")
}else {
  setTimeout(function(){ 
        messages.style.display = "none"; 
      }, 3000)
};
// try{
//   setTimeout(function(){ 
//     messages.style.display = "none"; 
//   }, 3000)
// } catch (error) {
//   console.log("Display "+(error));
// };
