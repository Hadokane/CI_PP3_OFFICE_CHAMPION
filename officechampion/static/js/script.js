document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
});

// function to remove alerts onclick
function removeNode() {
    const myDiv = document.getElementById("alertCard");
    const parent = myDiv.parentNode;
    parent.removeChild(myDiv);
}
