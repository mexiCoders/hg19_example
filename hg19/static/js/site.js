function menu(){
    var arr = location.pathname.split("/")
    switch (arr[2]){
        case "":
            document.getElementById("index").className = "active"
            break;
        case "exact":
            document.getElementById("exact").className = "active"
            break;
        case "search":
            document.getElementById("search").className = "active"
            break;
        case "lalignment":
            document.getElementById("alignment").className = "active"
            break;
        default:
            document.getElementById("index").className = "active"
            break;


    }
}

window.onload=function(){menu();};
