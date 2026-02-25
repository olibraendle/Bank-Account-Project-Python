// --- helpers ---

function getToken() {
    return localStorage.getItem("token");
}

function showDashboard(username) {
    document.getElementById("auth-section").classList.add("hidden");
    document.getElementById("dashboard").classList.remove("hidden");
    document.getElementById("display-username").textContent = username;
}

function showAuth() {
    document.getElementById("dashboard").classList.add("hidden");
    document.getElementById("auth-section").classList.remove("hidden");
}

// --- on page load: check if already logged in ---

window.onload = function () {
    const token = getToken();
    const username = localStorage.getItem("username");
    if (token && username) {
        showDashboard(username);
    }
};

// --- login ---

document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("username", username);
        showDashboard(username);
    } else {
        document.getElementById("login-error").textContent = data.error;
    }
});

// --- register ---

document.getElementById("register-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const body = {
        username: document.getElementById("reg-username").value,
        password: document.getElementById("reg-password").value,
        fullname: document.getElementById("reg-fullname").value,
        address:  document.getElementById("reg-address").value,
        email:    document.getElementById("reg-email").value,
    };

    const response = await fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });

    const data = await response.json();
    document.getElementById("register-msg").textContent = response.ok ? data.message : data.error;
});

// --- logout ---

document.getElementById("logout-btn").addEventListener("click", function () {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    showAuth();
});

// --- balance ---

async function loadBalance() {
    const response = await fetch("/balance", {
        headers: { "Authorization": getToken() }
    });
    const data = await response.json();
    document.getElementById("balance-amount").textContent = data.balance;
}

document.getElementById("refresh-balance").addEventListener("click", loadBalance);

// --- deposit ---

document.getElementById("deposit-btn").addEventListener("click", async function () {
    const amount = document.getElementById("deposit-amount").value;

    const response = await fetch("/deposit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({ amount })
    });

    const data = await response.json();
    document.getElementById("deposit-msg").textContent = data.message;
    loadBalance();
});

// --- withdraw ---

document.getElementById("withdraw-btn").addEventListener("click", async function () {
    const amount = document.getElementById("withdraw-amount").value;

    const response = await fetch("/withdraw", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({ amount })
    });

    const data = await response.json();
    document.getElementById("withdraw-msg").textContent = data.message || data.error;
    loadBalance();
});

// --- history ---

document.getElementById("history-btn").addEventListener("click", async function () {
    const response = await fetch("/history", {
        headers: { "Authorization": getToken() }
    });
    const data = await response.json();
    document.getElementById("history-output").textContent = JSON.stringify(data.history, null, 2);
});
