//隐藏所有行
document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("workerTable");
    var rows = table.getElementsByTagName("tr");
    for (var i = 1; i < rows.length; i++) {
      rows[i].style.display = "none";
    }
  });

//人物查询
  document.getElementById("queryButton").addEventListener("click", function(event) {
    event.preventDefault(); 
  
    var department = document.getElementById("departmentSelect").value;
    var location = document.getElementById("locationSelect").value;
    var name = document.getElementById("nameInput").value;
  
    var table = document.getElementById("workerTable");
    var rows = table.getElementsByTagName("tr");
  
    for (var i = 1; i < rows.length; i++) {
      var worker = rows[i];
      var workerDepartment = worker.cells[3].innerHTML;
      var workerLocation = worker.cells[4].innerHTML;
      var workerName = worker.cells[2].innerHTML;
  
      // 根据筛选条件显示符合条件的行
      if (
        (department === "所有" || workerDepartment === department) &&
        (location === "所有" || workerLocation === location) &&
        (name === "" || workerName.includes(name))
      ) {
        worker.style.display = "";
      } else {
        worker.style.display = "none";
      }
    }
  }, { passive: false }); // 明确设置 passive 为 false
  