var form = document.getElementById('search_form');
form.onsubmit = function () {
    var input = document.getElementById("search_result").value;
    if(input == "") {
        alert("Please enter keyword")
    } else {
        localStorage.setItem("search_data", input); 
        form.action = "search-result.html";   
    }
};