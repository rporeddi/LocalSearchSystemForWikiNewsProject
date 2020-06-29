
//This function is used to validate the login form once user entered credentials and hit login button
function validateIndexingForm() {
    
    if(document.getElementById('itemname').checked || document.getElementById('itemdescription').checked || document.getElementById('itemurl').checked){
        
          window.location.href = "Item-Management.html";   
    }
    
    else{
        alert('Please select any feature');
    }
   
  
}

