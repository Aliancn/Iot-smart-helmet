var myObj = { name : "菜鸟教程", site : "www.runoob.com" };
console.log(myObj);

document.getElementById("queryButton").addEventListener("click", function(event) {
  event.preventDefault(); // 确保 preventDefault() 生效
  
  console.log("查询按钮被点击了"); // 添加此行以打印消息

  var department = document.getElementById("departmentSelect").value;
  var position = document.getElementById("positionSelect").value;
  var location = document.getElementById("locationSelect").value;
  var name = document.getElementById("nameInput").value;

  var table = document.getElementById("workerTable");
  var rows = table.getElementsByTagName("tr");

  for (var i = 1; i < rows.length; i++) {
    var worker = rows[i];
    var workerDepartment = worker.cells[4].innerHTML;
    var workerPosition = worker.cells[3].innerHTML; //待修改
    var workerLocation = worker.cells[5].innerHTML;
    var workerName = worker.cells[1].innerHTML;

    // 显示所有行
    worker.style.display = "";

    // 根据筛选条件隐藏不符合条件的行
    if (
      (department === "所有" || workerDepartment === department) &&
      (position === "所有" || workerPosition === position) &&
      (location === "所有" || workerLocation === location) &&
      (name === "" || workerName.includes(name))
    ) {
      worker.style.display = "";
    } else {
      worker.style.display = "none";
    }
  }
}, { passive: false }); // 明确设置 passive 为 false