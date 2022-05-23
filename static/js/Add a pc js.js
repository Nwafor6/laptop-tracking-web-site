function myFunction() {
    var PCID = document.forms["form"]["PC ID"].value;
    var LaporatoryID = document.forms["form"]["Laporatory ID"].value;
    var status = document.forms["form"]["status"].value;
    if (PCID == "") {
        alert("PC ID  must be filled out");
        return false;
      }
      if (LaporatoryID == "") {
        alert("Laporatory ID must be filled out");
        return false;
      }
      if (status == "") {
        alert("status must be filled out");
        return false;
      }
      if(LaporatoryID!=""&&status!=""&&PCID!=""){
    confirm("The form was add a pc to Laboratory");
    return true;
      }
}