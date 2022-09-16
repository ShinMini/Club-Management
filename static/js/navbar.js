
// main link => home, member, club
const home = document.getElementById("home");
const member = document.getElementById("member");
const club = document.getElementById("club");

// link href add
home.href = 'http://localhost:5000';

/* ----------------------------*/

// 버튼 클릭시 아래로 드롭다운 display: block;
function myFunction1() {
   document.getElementById("myDropdown1").classList.toggle("show");
}
function myFunction2() {
   document.getElementById("myDropdown2").classList.toggle("show");
}

// 버튼 클릭시 발생 이벤트 
window.onclick = function (event) {
   if (!event.target.matches(".dropbtn")) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      // 하위 element 개수만큼 class controll
      for (i = 0; i < dropdowns.length; i++) {
         var openDropdown = dropdowns[i];
         if (openDropdown.classList.contains("show")) {
            openDropdown.classList.remove("show");
         }
      }
   }
};