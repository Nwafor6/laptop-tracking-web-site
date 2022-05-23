function AlertFunction() {
    var labID = document.forms["form"]["lab ID"].value;
    var PCnum= document.forms["form"]["PC num"].value;
    var description = document.forms["form"]["description"].value;
    var problem = document.forms["form"]["problem"].value;
    var date = document.forms["form"]["dates"].value;
    if (labID == "") {
        alert("lab ID  must be filled out");
        return false;
      }
      if (PCnum == "") {
        alert("PC num  must be filled out");
        return false;
      }
      if (description == "") {
        alert("description must be filled out");
        return false;
      }
      if (problem == "") {
        alert("problem  must be filled out");
        return false;
      }
      if (date == "") {
        alert("date must be filled out");
        return false;
      }
      if (date != ""&&problem != ""&&description != ""&&PCnum != ""&&labID!="") {
        confirm("You are report a problem.");
        return true;
      }
}