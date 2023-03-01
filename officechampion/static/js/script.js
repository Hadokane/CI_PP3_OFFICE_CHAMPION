document.addEventListener("DOMContentLoaded", function () {
    // Materialize auto initialise 
    M.AutoInit();

    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // select input initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select, options);
    M.FormSelect.getInstance(select)
});

// function to remove alerts onclick
function removeNode() {
    const myDiv = document.getElementById("alertCard");
    const parent = myDiv.parentNode;
    parent.removeChild(myDiv);
};
