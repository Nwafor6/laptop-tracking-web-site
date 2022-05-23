function validateForm() {
    let LaboratoryName = document.forms["form"]["Laboratory's Name"].value;
let LaboratoryID = document.forms["form"]["Laboratory's ID"].value;
    if (LaboratoryName == "") {
      alert("Name must be filled out");
      return false;
    }
    if (LaboratoryID == "") {
      alert("ID must be filled out");
      return false;
    }
    if(LaboratoryID!=""&&LaboratoryName!=""){
        confirm("Are you sure you want to delete this laboratry's data from the sysem ?");
    return true;
}
}
