
//This function is used to validate the login form once user entered credentials and hit login button
function validateForm() {
    var user_name = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var admin_user = 'admin'
    var admin_password = 'admin@123'
    var anonymous_user = "anonymous"
    var anonymous_password = "anonymous@123"
    if (user_name === "" & password ==="") {
        alert("Please enter credentials");
    }
    else if (password === "") {
        alert("Password must be filled out");
    }
    else if (user_name === "") {
        alert("User Name must be filled out");
    }
    else if(user_name==admin_user && password == admin_password)
    {
         window.location.href = "user-management.html";    
    }
    else if(user_name == anonymous_user && password == anonymous_password){
        
        window.location.href = "search.html";   
         
    }
    else{
        alert("Invalid User name or Password")
    }
    
    return false
}

