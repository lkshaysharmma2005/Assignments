function setDarkorLight() {
  if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
    document.body.classList.add("dark");
    document.body.classList.remove("light");
  } else {
    document.body.classList.add("light");
    document.body.classList.remove("dark");
  }
}
setDarkorLight();

window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function(){
  setDarkorLight();
});


let btn = document.querySelector("#toggleTheme")

btn.addEventListener("click", function(){
  document.body.classList.toggle("dark");
  if(document.body.classList.contains("dark")){
    localStorage.setItem("theme", "dark")
  }
  else{
    localStorage.setItem("theme", "light")
  }
});