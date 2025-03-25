const apiBase = "http://127.0.0.1:5000/employees";

function createEmployee() {
    const data = {
        firstname: document.getElementById("firstname").value,
        lastname: document.getElementById("lastname").value,
        age: parseInt(document.getElementById("age").value),
        salary: parseInt(document.getElementById("salary").value),
    };

    fetch(apiBase + "/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => alert("Employee Created: " + data))

        .catch((error) => console.error("Error:", error));
}

function getEmployees() {
    fetch(apiBase + "/")
        .then((response) => response.json())
        .then((data) => {
            const list = document.getElementById("employees-list");
            list.innerHTML = "";
            data.forEach((employee) => {
                const li = document.createElement("li");
                li.textContent = `ID: ${employee.id}, Name: ${employee.firstname} ${employee.lastname}, Age: ${employee.age}, Salary: ${employee.salary}`;
                list.appendChild(li);
            });
        })
        .catch((error) => console.error("Error:", error));
}

function getEmployee() {
    const id = document.getElementById("get-id").value;
    fetch(`${apiBase}/${id}`)
    .then((response) => response.json())
    .then((data) => {
        if (data.id == undefined){
            alert(data);
        }else{
            const employee = document.getElementById("employee")
            employee.innerHTML="";
            employee.textContent = `ID: ${data.id}, Name: ${data.firstname} ${data.lastname}, Age: ${data.age}, Salary: ${data.salary}`;
            }
    })
     .catch((error) => console.error("Error:", error));

}

function updateEmployee() {
    const id = document.getElementById("update-id").value;
    const data = {
        firstname: document.getElementById("update-firstname").value || undefined,
        lastname: document.getElementById("update-lastname").value || undefined,
        age: parseInt(document.getElementById("update-age").value) || undefined,
        salary: parseInt(document.getElementById("update-salary").value) || undefined,
    };

    fetch(`${apiBase}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => alert("Employee Updated: " + data))
        .catch((error) => console.error("Error:", error));
}

function deleteEmployee() {
    const id = document.getElementById("delete-id").value;

    fetch(`${apiBase}/${id}`, {
        method: "DELETE",
    })
        .then((response) => response.json())
        .then((data) => alert("Employee Deleted: " + data))
        .catch((error) => console.error("Error:", error));
}