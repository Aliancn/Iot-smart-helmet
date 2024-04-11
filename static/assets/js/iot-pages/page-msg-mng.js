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
    console.log("queryButton clicked");
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

  // document.getElementById("sendMsgButton").addEventListener("click", function(event) {
  //   event.preventDefault();

  //   console.log("sendMsgButton clicked");
  //   var workerCheckbox = document.getElementsByName("workerId");
  //     var workerChecked = false;
  //     for (var i = 0; i < workerCheckbox.length; i++) {
  //       if (workerCheckbox[i].checked) {
  //         workerChecked = true;
  //         break;
  //       }
  //     }
  
  //     // 获取消息复选框的状态
  //     var msgCheckbox = document.getElementsByName("msgId");
  //     var msgChecked = false;
  //     for (var i = 0; i < msgCheckbox.length; i++) {
  //       if (msgCheckbox[i].checked) {
  //         msgChecked = true;
  //         break;
  //       }
  //     }
  
  //     // 判断是否勾选了员工和消息
  //     if (!workerChecked) {
  //       alert("没有勾选员工！");
  //     } else if (!msgChecked) {
  //       alert("没有勾选消息！");
  //     } else {
  //       // 两者都勾选了，定位到视图函数
  //       window.location.href = 'send_msg/';
  //     }
  // });
  