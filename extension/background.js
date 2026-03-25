var blockedDomains = [
    "doubleclick.net",
    "google-analytics.com",
    "googletagmanager.com",
    "facebook.com",
    "ads.twitter.com"
];

var blockedCount = 0;

// Initialize storage
browser.storage.local.set({ blocked: 0 });

// Listen to all outgoing requests
browser.webRequest.onBeforeRequest.addListener(
    function(details) {

        for (let domain of blockedDomains) {

            if (details.url.includes(domain)) {

                blockedCount++;

                // Update storage
                browser.storage.local.set({ blocked: blockedCount });

                // Log in console
                console.log("Blocked:", details.url);

                // Block request
                return { cancel: true };
            }
        }

    },
    { urls: ["<all_urls>"] },
    ["blocking"]
);
