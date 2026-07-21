let editingTaskId = null;

document.getElementById("taskForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const token = localStorage.getItem("token");

    const taskData = {
        title: document.getElementById("title").value,
        description: document.getElementById("description").value
    };

    let response;

    if (editingTaskId === null) {

        response = await fetch("/tasks/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            },
            body: JSON.stringify(taskData)
        });

    } else {

        response = await fetch(`/tasks/${editingTaskId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + token
            },
            body: JSON.stringify({
                title: taskData.title,
                description: taskData.description,
                completed: false
            })
        });

    }

    const data = await response.json();

    if (response.ok) {

        alert(editingTaskId === null
            ? "Task created successfully!"
            : "Task updated successfully!");

        document.getElementById("taskForm").reset();

        editingTaskId = null;

        document.querySelector("#taskForm button").textContent = "Add Task";

        loadTasks();

    } else {

        alert(data.detail);

    }
});

async function loadTasks() {

    const token = localStorage.getItem("token");

    const response = await fetch("/tasks/", {
        method: "GET",
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    const tasks = await response.json();

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const safeTitle = task.title.replace(/'/g, "\\'");
        const safeDescription = (task.description || "").replace(/'/g, "\\'");

        taskList.innerHTML += `
            <div class="task-card">
                <h3>${task.title}</h3>
                <p>${task.description || "No description provided."}</p>

                <button onclick="editTask(${task.id}, '${safeTitle}', '${safeDescription}')">
                    Edit
                </button>

                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>
            </div>
        `;

    });

}

function editTask(id, title, description) {

    editingTaskId = id;

    document.getElementById("title").value = title;
    document.getElementById("description").value = description;

    document.querySelector("#taskForm button").textContent = "Update Task";

}

async function deleteTask(id) {

    const token = localStorage.getItem("token");

    const response = await fetch(`/tasks/${id}`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    const data = await response.json();

    if (response.ok) {

        alert(data.detail);

        loadTasks();

    } else {

        alert(data.detail);

    }

}

loadTasks();

document.getElementById("logoutBtn").addEventListener("click", function () {

    localStorage.removeItem("token");

    window.location.href = "/";

});