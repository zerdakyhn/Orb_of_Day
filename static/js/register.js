document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const userData = {
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };

    const response = await fetch("/users/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(userData)
    });

    const data = await response.json();

    if (response.ok) {
        alert("Registration successful!");

        window.location.href = "/";
    } else {
        alert(data.detail);
    }
});