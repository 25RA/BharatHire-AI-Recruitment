/* ==========================================================
   BharatHire
   dashboard.js
   Backend Integrated
   Part 1
   ========================================================== */

"use strict";

/* ==========================================================
   Global State
   ========================================================== */

let dashboardMetrics = {};

let leaderboard = [];

/* ==========================================================
   DOM Ready
   ========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        await initializeDashboard();

    }

);

/* ==========================================================
   Dashboard Initialization
   ========================================================== */

async function initializeDashboard() {

    await checkBackend();

    await loadDashboard();

}

/* ==========================================================
   Backend Status
   ========================================================== */

async function checkBackend() {

    const status = document.getElementById(

        "dashboardBackend"

    );

    if (!status) return;

    try {

        await API.getServerStatus();

        status.textContent = "Online";

        status.className = "risk-low";

    }

    catch (error) {

        status.textContent = "Offline";

        status.className = "risk-high";

        console.error(error);

    }

}

/* ==========================================================
   Load Dashboard
   ========================================================== */

async function loadDashboard() {

    try {

        dashboardMetrics = await API.getAnalytics();
        console.log("Analytics:", dashboardMetrics);

        const leaderboardResponse = await API.getLeaderboard(100);
        console.log("Leaderboard Response:", leaderboardResponse);

        leaderboard = leaderboardResponse.results || [];
        console.log("Leaderboard:", leaderboard);

        console.log("Before KPI");
        updateKPICards();
        console.log("After KPI");
        
        console.log("Before Leaderboard");
        renderLeaderboard();
        console.log("After Leaderboard");
        
        console.log("Before Charts");
        updateCharts();
        console.log("After Charts");

    }

    catch (error) {

        console.error(error);

        notify("Unable to load dashboard.");

    }

}

/* ==========================================================
   KPI Cards
   ========================================================== */

function updateKPICards() {

    setValue(

        "totalCandidates",

        dashboardMetrics.candidates_processed

    );

    setValue(

        "recommendedCount",

        dashboardMetrics.recommendations

            ? (

                dashboardMetrics.recommendations["Elite Match"] || 0

              )

              +

              (

                dashboardMetrics.recommendations["Strong Shortlist"] || 0

              )

            : 0

    );

    setValue(

        "averageScore",

        dashboardMetrics.average_score

    );

    setValue(

        "confidenceScore",

        dashboardMetrics.confidence

            ?

            dashboardMetrics.confidence.average + "%"

            :

            "--"

    );

}

/* ==========================================================
   Helper
   ========================================================== */

function setValue(id, value) {

    const element =

        document.getElementById(id);

    if (!element) return;

    element.textContent = value;

}

/* ==========================================================
   Charts
   ========================================================== */

function updateCharts() {

    if (

        typeof ChartManager ===

        "undefined"

    ) return;

    ChartManager.updateDashboardCharts({

        recommendations:

            dashboardMetrics.recommendations,

        componentScores:

            dashboardMetrics.component_scores,

        confidence:

            dashboardMetrics.confidence

                ?

                dashboardMetrics.confidence.average

                :

                0

    });

}
/* ==========================================================
   Leaderboard Table
   ========================================================== */

function renderLeaderboard(list = leaderboard) {

    const tbody = document.getElementById(

        "candidateTableBody"

    );

    if (!tbody) return;

    tbody.innerHTML = "";

    if (!list.length) {

        tbody.innerHTML = `

        <tr>

            <td colspan="5">

                No candidates found.

            </td>

        </tr>

        `;

        return;

    }

    list.forEach(candidate => {

        let badge = "badge-secondary";

        switch (candidate.recommendation) {

            case "Elite Match":
                badge = "badge-success";
                break;

            case "Strong Shortlist":
                badge = "badge-primary";
                break;

            case "Shortlist":
                badge = "badge-info";
                break;

            case "Needs Manual Review":
                badge = "badge-warning";
                break;

            default:
                badge = "badge-danger";

        }

        tbody.innerHTML += `

        <tr>

            <td>

                ${candidate.candidate_id}

            </td>

            <td>

                ${candidate.overall_score.toFixed(2)}

            </td>

            <td>

                ${candidate.confidence}%

            </td>

            <td>

                <span class="badge ${badge}">

                    ${candidate.recommendation}

                </span>

            </td>

            <td>

                <button

                    class="icon-btn"

                    onclick="openCandidate('${candidate.candidate_id}')">

                    View

                </button>

            </td>

        </tr>

        `;

    });

}

/* ==========================================================
   Candidate Page
   ========================================================== */

function openCandidate(candidateId) {

    window.location.href =

        `candidate.html?id=${candidateId}`;

}

/* ==========================================================
   Search
   ========================================================== */

function initializeSearch() {

    const search = document.getElementById(

        "candidateSearch"

    );

    if (!search) return;

    search.addEventListener(

        "input",

        () => {

            const value =

                search.value

                .toLowerCase()

                .trim();

            const filtered =

                leaderboard.filter(candidate =>

                    String(candidate.candidate_id)

                    .toLowerCase()

                    .includes(value)

                );

            renderLeaderboard(filtered);

        }

    );

}

/* ==========================================================
   Recommendation Filter
   ========================================================== */

function initializeFilter() {

    const filter = document.getElementById(

        "recommendationFilter"

    );

    if (!filter) return;

    filter.addEventListener(

        "change",

        () => {

            if (

                filter.value === "all"

            ) {

                renderLeaderboard();

                return;

            }

            const filtered =

                leaderboard.filter(

                    candidate =>

                    candidate.recommendation ===

                    filter.value

                );

            renderLeaderboard(filtered);

        }

    );

}

/* ==========================================================
   Run AI Pipeline
   ========================================================== */

function initializePipelineButton() {

    const button = document.getElementById(

        "runPipelineBtn"

    );

    const modal = document.getElementById(

        "pipelineModal"

    );

    const confirm = document.getElementById(

        "confirmPipeline"

    );

    if (button && modal) {

        button.addEventListener(

            "click",

            () => {

                modal.classList.add(

                    "active"

                );

            }

        );

    }

    if (!confirm) return;

    confirm.addEventListener(

        "click",

        async () => {

            confirm.disabled = true;

            confirm.textContent =

                "Running...";

            try {

                notify(

                    "Running AI Ranking Pipeline..."

                );

                await API.runRanking();

                notify(

                    "Pipeline completed successfully."

                );

                modal.classList.remove(

                    "active"

                );

                await loadDashboard();

            }

            catch (error) {

                console.error(error);

                notify(

                    "Pipeline execution failed."

                );

            }

            finally {

                confirm.disabled = false;

                confirm.textContent =

                    "Run Pipeline";

            }

        }

    );

}

/* ==========================================================
   Refresh
   ========================================================== */

async function refreshDashboard() {

    await loadDashboard();

}

/* ==========================================================
   Notification Helper
   ========================================================== */

function notify(message) {

    if (

        typeof showToast ===

        "function"

    ) {

        showToast(

            message,

            "success"

        );

    }

    else {

        console.log(message);

    }

}
/* ==========================================================
   Charts Integration
   ========================================================== */

function updateCharts() {

    if (

        typeof ChartManager ===

        "undefined"

    ) return;

    ChartManager.updateDashboardCharts({

        recommendations:

            dashboardMetrics.recommendations ||

            {},

        componentScores:

            dashboardMetrics.component_scores ||

            {},

        confidence:

            dashboardMetrics.confidence

                ?

                dashboardMetrics.confidence.average

                :

                0

    });

}

/* ==========================================================
   Dashboard Buttons
   ========================================================== */

function initializeButtons() {

    document

        .querySelectorAll(".glass-btn")

        .forEach(button => {

            const text =

                button.textContent.trim();

            if (

                text ===

                "Refresh"

            ) {

                button.addEventListener(

                    "click",

                    refreshDashboard

                );

            }

        });

}

/* ==========================================================
   Keyboard Shortcuts
   ========================================================== */

function initializeKeyboardShortcuts() {

    document.addEventListener(

        "keydown",

        event => {

            if (

                event.ctrlKey &&

                event.key.toLowerCase()

                === "r"

            ) {

                event.preventDefault();

                refreshDashboard();

            }

        }

    );

}

/* ==========================================================
   Auto Refresh
   ========================================================== */

function initializeAutoRefresh() {

    setInterval(

        async () => {

            await loadDashboard();

        },

        60000

    );

}

/* ==========================================================
   Initialize Events
   ========================================================== */

function initializeDashboardEvents() {

    renderLeaderboard();

    initializeSearch();

    initializeFilter();

    initializePipelineButton();

    initializeButtons();

    initializeKeyboardShortcuts();

    initializeAutoRefresh();

}

/* ==========================================================
   Dashboard Startup
   ========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        await initializeDashboard();

        initializeDashboardEvents();

        console.log(

            "%cBharatHire Dashboard Connected",

            "color:#4F7CFF;font-size:16px;font-weight:bold;"

        );

    }

);

/* ==========================================================
   Public API
   ========================================================== */

window.Dashboard = {

    refresh:

        refreshDashboard,

    render:

        renderLeaderboard,

    reload:

        loadDashboard

};