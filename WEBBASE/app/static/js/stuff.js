function toggle_popup(id){ //define a function "toggle popup" which needs to know what popup to toggle, so inthe brackets it takes the id of the popup
    target=document.getElementById(id);
    b=document.getElementById("blurbg");
    
    if (target.style.display!='block'){
        target.style.display='block';
        b.style.display='block';
    }
    else{
        target.style.display='none';
        b.style.display='none';
    }
}