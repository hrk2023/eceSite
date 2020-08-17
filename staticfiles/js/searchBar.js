const searchFun = () => {
    let filter = document.getElementById('myInput').value.toUpperCase();

    let desc = document.getElementsByClassName("myTable");
    let display = document.getElementsByClassName("display");
    
    for(let i=0; i< display.length; i++) {
        let value = display[i].innerText;
        if(value) {
            if(value.toUpperCase().indexOf(filter) > -1) {
                console.log("found");
                display[i].style.display = "";
            }
            else {
                console.log("not found");
                display[i].style.display = "none";
            }
        }   
    }
};