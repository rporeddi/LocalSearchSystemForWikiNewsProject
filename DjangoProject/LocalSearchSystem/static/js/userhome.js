
var form = document.getElementById('search_form');
form.onsubmit = function () {
    var keyword = document.getElementById("keyword").value;

    localStorage.setItem("search_keyword", keyword);
    //form.action = "search.html";
};