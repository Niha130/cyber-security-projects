chrome.storage.local.get("blocked", function(data) {
    document.getElementById("count").innerText =
        "Blocked: " + (data.blocked || 0);
});
