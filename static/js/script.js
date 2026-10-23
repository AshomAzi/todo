const btn = document.getElementById("newTask");
const add = document.getElementById("addnewtask");
const newadd = document.getElementById("newadd")


btn.addEventListener("click", function(){
    add.style.display = "flex"
});

newadd.addEventListener("click", function() {
    add.style.display = "none"
});

document.addEventListener("click", function(e){
    if (!add.contains(e.target) && e.target!= btn) {
        add.style.display = "none"
    }
})