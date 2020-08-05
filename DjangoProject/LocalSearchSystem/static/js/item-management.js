$(document).ready(function(){
	var actions = $("table td:last-child").html();

    $('#item_table').DataTable( {
        "pagingType": "full_numbers"
    } );
});

function delItem(itemId){
    var con = confirm('Are you sure you want to delete the item?')
    if(con==true){
//        location.href = '/WikiNews/item/del/'+itemId;
        location.href='/wikinews/item/del/'+itemId;
    }
    else{
    alert("no!")
    }
}

function itemDetail(itemId){

    location.href = '/wikinews/itemdetails/'+ itemId;
}

$(document).on("click", ".edit", function(){
		$("#edititemId").val(($(this).parents("tr").find("td:nth-child(1)").text()))
		$("#edititemtitle").val(($(this).parents("tr").find("td:nth-child(2)").text()))

 });
