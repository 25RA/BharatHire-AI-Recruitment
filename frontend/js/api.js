/* ==========================================================
   BharatHire
   api.js
   Central API Service
   ========================================================== */

"use strict";

/* ==========================================================
   Configuration
   ========================================================== */

const API_CONFIG = {

    BASE_URL: "http://127.0.0.1:8000",

    TIMEOUT: 30000

};

/* ==========================================================
   Generic Request Function
   ========================================================== */

async function request(endpoint, options = {}) {

    const controller = new AbortController();

    const timeout = setTimeout(() => {

        controller.abort();

    }, API_CONFIG.TIMEOUT);

    try {

        const response = await fetch(

            API_CONFIG.BASE_URL + endpoint,

            {

                ...options,

                signal: controller.signal

            }

        );

        clearTimeout(timeout);

        if (!response.ok) {

            throw new Error(

                `HTTP ${response.status}`

            );

        }

        return await response.json();

    }

    catch (error) {

        clearTimeout(timeout);

        console.error("API Error:", error);

        throw error;

    }

}

/* ==========================================================
   Health Check
   ========================================================== */

async function getServerStatus() {

    return request("/");

}

/* ==========================================================
   Analytics
   ========================================================== */

async function getAnalytics() {

    return request("/analytics");

}

/* ==========================================================
   Leaderboard
   ========================================================== */

async function getLeaderboard(limit = 100) {

    return request(

        `/leaderboard?limit=${limit}`

    );

}

/* ==========================================================
   Candidate Details
   ========================================================== */

async function getCandidate(id) {

    return request(`/candidate/${id}`);

}

/* ==========================================================
   Run Ranking Pipeline
   ========================================================== */

async function runRanking() {

    return request("/rank", {

        method: "POST"

    });

}

/* ==========================================================
   Generic GET
   ========================================================== */

async function get(endpoint) {

    return request(endpoint);

}

/* ==========================================================
   Generic POST
   ========================================================== */

async function post(endpoint, data) {

    return request(endpoint, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(data)

    });

}

/* ==========================================================
   Generic Upload
   ========================================================== */

async function upload(endpoint, formData) {

    return request(endpoint, {

        method: "POST",

        body: formData

    });

}

/* ==========================================================
   Helper
   ========================================================== */

function isOnline() {

    return navigator.onLine;

}

/* ==========================================================
   Format Error
   ========================================================== */

function parseError(error) {

    if (error.name === "AbortError") {

        return "Request Timeout";

    }

    if (!navigator.onLine) {

        return "No Internet Connection";

    }

    return error.message || "Unknown Error";

}

/* ==========================================================
   API Object
   ========================================================== */

const BharatHireAPI = {

    getServerStatus,

    getAnalytics,

    getLeaderboard,

    getCandidate,

    runRanking,

    get,

    post,

    upload,

    isOnline,

    parseError

};

/* ==========================================================
   Export
   ========================================================== */

window.API = BharatHireAPI;