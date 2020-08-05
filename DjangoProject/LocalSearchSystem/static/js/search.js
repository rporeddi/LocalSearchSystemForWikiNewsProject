var searchForm = document.getElementById("search_form");
var search_box = document.getElementById("id_q");
search_box.type = "hidden";
search_box.value = localStorage.getItem("search_keyword");

function loadForm() {
    if (!sessionStorage.getItem("submitted")) {
        console.log("submitting");
        sessionStorage.setItem("submitted", "true");
        searchForm.submit();

    } else {
        console.log("already submitted, not repeating");
        sessionStorage.removeItem("submitted");
    }
}
function itemDetail(itemId){
    location.href = '/wikinews/itemdetails/'+ itemId;
}