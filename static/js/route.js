// SEARCH ONE
function searchMember() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         data = this.responseText;

         if (data == "해당 조회 결과가 없습니다.") {
            document.getElementById("searchList").style.display = "none";

            document.getElementById("noData").innerHTML = data;
            document.getElementById("noData").style.display = "block";
         } else {
            data = JSON.parse(data);
            document.getElementById("noData").style.display = "none";

            document.getElementById("id").innerHTML = data.member_id;
            document.getElementById("name").innerHTML = data.member_name;
            document.getElementById("age").innerHTML = data.age;
            document.getElementById("phone").innerHTML = data.phone;
            document.getElementById("gender").innerHTML = data.gender;
            document.getElementById("club").innerHTML = data.club_name;
            document.getElementById("rating").innerHTML = data.rating;
            document.getElementById("enroll").innerHTML = data.enroll;

            document.getElementById("searchList").style.display = "block";
         }
      }
   };
   xhttp.open("POST", "search/one");
   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

   queryString = "memid=" + document.getElementById("searchId").value
      + "&memname=" + document.getElementById("searchName").value
      + "&age=" + document.getElementById("searchAge").value;
   xhttp.send(queryString);
}

// SEARCH ALL
function searchAllMember() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         result = this.responseText;
         let data = JSON.parse(result);

         let table = document.getElementById("memberTable");

         for (let i = 0; i < data.length; i++) {
            temp = JSON.parse(data[i]);
            let tr = document.createElement("tr");
            tr.className = "rows";

            let td_id = document.createElement("td");
            td_id.innerHTML = temp.member_id;

            let td_name = document.createElement("td");
            td_name.innerHTML = temp.member_name;

            let td_age = document.createElement("td");
            td_age.innerHTML = temp.age;

            let td_phone = document.createElement("td");
            td_phone.innerHTML = temp.phone

            let td_gender = document.createElement("td");
            td_gender.innerHTML = temp.gender;

            let td_club_name = document.createElement("td");
            td_club_name.innerHTML = temp.club_name

            let td_rating = document.createElement("td");
            td_rating.innerHTML = temp.rating

            let td_enroll = document.createElement("td");
            td_enroll.innerHTML = temp.enroll

            tr.appendChild(td_id);
            tr.appendChild(td_name);
            tr.appendChild(td_age);
            tr.appendChild(td_phone);
            tr.appendChild(td_gender);
            tr.appendChild(td_club_name);
            tr.appendChild(td_rating);
            tr.appendChild(td_enroll);

            table.appendChild(tr);
         }
         document.getElementById("searchAllList").style.display = "block";
      }
   };
   xhttp.open("POST", "search/all");
   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   console.log("=============searchall==================")
   xhttp.send();
}


// UPDATE NAME
function updateMember() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         data = this.responseText;
         alert("회원 정보 수정을 완료했습니다.");
      }
   };
   xhttp.open("POST", "update/enroll");
   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   queryString =
      "&memid=" +
      document.getElementById("searchId").value +
      "&memname=" +
      document.getElementById("newMemberName").value
   xhttp.send(queryString);
}

// DELETE ONE
function deleteMember() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         alert("응답" + this.responseText);
      }
   };
   xhttp.open("POST", "delete/enroll");
   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );
   queryString = "memid=" + document.getElementById("checkmemid").value;
   console.log(queryString);
   xhttp.send(queryString);
}

// CREATE(INSERT) ONE
function insertMember() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         alert("응답" + this.responseText);
      }
   };
   xhttp.open("POST", "insert/enroll"); //http://ip:port/insert

   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );

   queryString =
      "&memid=" +
      document.getElementById("newMemberId").value +
      "&memname=" +
      document.getElementById("newMemberName").value +
      "&age=" +
      document.getElementById("newAge").value +
      "&phone=" +
      document.getElementById("newPhone").value +
      "&gender=" +
      document.getElementById("newGender").value +
      "&clubName=" +
      document.getElementById("newClubName").value +
      "&rating=" +
      document.getElementById("newRating").value +
      "&enroll=" +
      document.getElementById("newEnroll").value;

   console.log(queryString);

   xhttp.send(queryString);
}

// ================ CLUB ==========================
// ================ CLUB ==========================

// SEARCH ONE Club
function searchClub() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         data = this.responseText;
         alert("응답");

         if (data == "해당 조회 결과가 없습니다.") {
            document.getElementById("searchList").style.display = "none";
            document.getElementById("noData").innerHTML = data;
            document.getElementById("noData").style.display = "block";
         } else {
            data = JSON.parse(data);

            document.getElementById("noData").style.display = "none";
            document.getElementById("id").innerHTML = data.club_id;
            document.getElementById("name").innerHTML = data.club_name;

            document.getElementById("searchList").style.display = "block";
         }
      }
   };
   xhttp.open("POST", "search/one");
   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );
   queryString = "clubid=" + document.getElementById("searchId").value
      + "clubname=" + document.getElementById("searchName").value;

   // console.log(document.getElementById("searchId"))
   console.log(queryString);
   xhttp.send(queryString);
}

// SEARCH ALL
function searchAllClub() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         result = this.responseText;
         let data = JSON.parse(result);

         let table = document.getElementById("clubTable");

         for (let i = 0; i < data.length; i++) {
            temp = JSON.parse(data[i]);
            let tr = document.createElement("tr");
            tr.className = "rows";

            let td_id = document.createElement("td");
            td_id.innerHTML = temp.club_id;

            let td_name = document.createElement("td");
            td_name.innerHTML = temp.club_name;

            tr.appendChild(td_id);
            tr.appendChild(td_name);

            table.appendChild(tr);
         }
         document.getElementById("searchAllList").style.display = "block";
      }
   }
   xhttp.open("POST", "search/all");
   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   xhttp.send("all");
}


// CHECK A Club
function searchClubId() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         alert(this.responseText);
      }
   };
   xhttp.open("POST", "search/check");
   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );
   queryString =
      "clubid=" + document.getElementById("ClubId").value;

   console.log(queryString);
   xhttp.send(queryString);
}



// UPDATE NAME
function updateClub() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         alert("클럽 정보 수정을 완료했습니다.");
      }
   };
   xhttp.open("POST", "update/enroll");
   xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
   queryString =
      "&clubid=" +
      document.getElementById("ClubId").value +
      "&clubname=" +
      document.getElementById("newClubName").value;
   xhttp.send(queryString);
}

// DELETE ONE
function deleteClub() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
         alert("삭제되었습니다.");
      }
   };
   xhttp.open("POST", "delete/enroll");
   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );
   queryString = "clubid=" + document.getElementById("checkclubid").value;
   console.log(queryString);
   xhttp.send(queryString);
}

// CREATE(INSERT) ONE
function insertClub() {
   const xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
      }
   };
   xhttp.open("POST", "insert/enroll"); //http://ip:port/insert

   xhttp.setRequestHeader(
      "Content-type",
      "application/x-www-form-urlencoded"
   );

   queryString =
      "&clubid=" +
      document.getElementById("newClubId").value +
      "&clubname=" +
      document.getElementById("newClubName").value;

   console.log(queryString);

   xhttp.send(queryString);
}
