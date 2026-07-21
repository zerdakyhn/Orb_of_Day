document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const formData = new FormData();
    formData.append("username", email);
    formData.append("password", password);

    const response = await fetch("/users/login", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("token", data.access_token);
        alert("Login successful!");
        window.location.href = "/dashboard";
    } else {
        alert(data.detail);
    }
});