function AlertFunction() {
    let Laporatoryname = document.forms["form"]["Laporatory name"].value;
    var LaporatoryID = document.forms["form"]["Laporatory ID"].value;
    var Numberofbuilding = document.forms["form"]["Number of building"].value;
    var Numberoffloor = document.forms["form"]["number of floor"].value;
    var NumberofPCs = document.forms["form"]["number of PCs"].value;
    var Lapcpacity = document.forms["form"]["lap cpacity"].value;
    var Chairsnumbers = document.forms["form"]["chairs numbers"].value;
    var status = document.forms["form"]["status"].value;
    if (Laporatoryname == "") {
        alert("Name must be filled out");
        return false;
      }
      if (LaporatoryID == "") {
        alert("ID must be filled out");
        return false;
      }
      if (Numberofbuilding == "") {
        alert("Number of building must be filled out");
        return false;
      }
      if (Numberoffloor == "") {
        alert("Number of floor must be filled out");
        return false;
      }
      if (NumberofPCs == "") {
        alert("Number of PCs must be filled out");
        return false;
      }
      if (Lapcpacity == "") {
        alert("Lap cpacity must be filled out");
        return false;
      }
      if (Chairsnumbers == "") {
        alert("Chairs numbers must be filled out");
        return false;
      }
      if (status == "") {
        alert("status must be filled out");
        return false;
      }
      if(LaporatoryID!=""&&Laporatoryname!=""&&status != ""&&Chairsnumbers != ""&&Lapcpacity != ""&&NumberofPCs != ""&&Numberoffloor != ""&&Numberofbuilding != ""){
    confirm("Are you sure you want to add this laboratry and laboratry's data from the sysem ?");
return true;
}
}