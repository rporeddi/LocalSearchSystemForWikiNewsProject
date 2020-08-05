function newUser(){
    location.href = '/user/newuser'
}

function delUser(userId) {
	var con = confirm('Are you sure you want to delete this User?');
	if (con === true) {
		location.href = '/user/del/' + userId;
	} else {
		alert("no!");
	}
}

$(document).ready(function() {
	var actions = $("table td:last-child").html();

	$('#user_table').DataTable({
		"pagingType": "full_numbers"
	});
});

$(document).on("click", ".edit", function(){
		$("#edituserid").val(($(this).parents("tr").find("td:nth-child(1)").text()))
		$("#editusername").val(($(this).parents("tr").find("td:nth-child(2)").text()))
		$("#editpassword").val(($(this).parents("tr").find("td:nth-child(3)").text()))
		var admin_checked = $(this).parents("tr").find("td:nth-child(4)").text()
        if(admin_checked == "True") {
            $("#editisadmin").prop('checked', true)
        } else {
            $("#editisadmin").prop('checked', false)
        }
 });
