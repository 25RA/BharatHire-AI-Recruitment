/* ==========================================================
   BharatHire
   candidate.js
   Backend Integrated
   Part 1
   ========================================================== */

"use strict";

/* ==========================================================
   Global State
   ========================================================== */

let candidate = {};

let fitChart = null;

let riskChart = null;

/* ==========================================================
   Read Candidate ID
   ========================================================== */

function getCandidateId() {

    const params = new URLSearchParams(

        window.location.search

    );

    return params.get("id");

}

/* ==========================================================
   DOM Ready
   ========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        await initializeCandidatePage();

    }

);

/* ==========================================================
   Initialize
   ========================================================== */

async function initializeCandidatePage() {

    await checkBackend();

    const id = getCandidateId();

    if (!id) {

        showToast(

            "Candidate ID missing.",

            "error"

        );

        return;

    }

    await loadCandidate(id);

}

/* ==========================================================
   Backend Status
   ========================================================== */

async function checkBackend() {

    const status =

        document.getElementById(

            "candidateBackend"

        );

    if (!status) return;

    try {

        await API.getServerStatus();

        status.textContent =

            "Online";

        status.className =

            "status-online";

    }

    catch (error) {

        status.textContent =

            "Offline";

        status.className =

            "status-offline";

    }

}

/* ==========================================================
   Load Candidate
   ========================================================== */

async function loadCandidate(id) {

    showLoading(true);

    try {

        candidate =

            await API.getCandidate(id);

        populateCandidate();

        createCharts();

    }

    catch (error) {

        console.error(error);

        showToast(

            "Unable to load candidate.",

            "error"

        );

    }

    finally {

        showLoading(false);

    }

}
/* ==========================================================
   Populate Candidate
   ========================================================== */

function populateCandidate() {

    /* Summary */

    setText(

        "candidateId",

        candidate.candidate_id

    );

    setText(

        "summaryCandidateId",

        candidate.candidate_id

    );

    setText(

        "overallScore",

        Number(

            candidate.overall_score

        ).toFixed(2)

    );

    setText(

        "summaryOverallScore",

        Number(

            candidate.overall_score

        ).toFixed(2)

    );

    /* Recommendation */

    setText(

        "recommendationBadge",

        candidate.recommendation

    );

    setText(

        "recommendationLabel",

        candidate.recommendation

    );

    setText(

        "summaryRecommendation",

        candidate.recommendation

    );

    /* Confidence */

    setText(

        "confidenceScore",

        Number(

            candidate.confidence

        ).toFixed(1) + "%"

    );

    setText(

        "summaryConfidence",

        Number(

            candidate.confidence

        ).toFixed(1) + "%"

    );

    /* AI Fits */

    setText(

        "technicalFit",

        Number(

            candidate.technical_fit

        ).toFixed(1) + "%"

    );

    setText(

        "experienceFit",

        Number(

            candidate.experience_fit

        ).toFixed(1) + "%"

    );

    setText(

        "behaviorFit",

        Number(

            candidate.behavior_fit

        ).toFixed(1) + "%"

    );

    setText(

        "riskScore",

        Number(

            candidate.risk_score

        ).toFixed(1) + "%"

    );

    /* Component Scores */

    setText(

        "skillScore",

        Number(

            candidate.skill_score

        ).toFixed(1)

    );

    setText(

        "experienceScore",

        Number(

            candidate.experience_score

        ).toFixed(1)

    );

    setText(

        "careerScore",

        Number(

            candidate.career_score

        ).toFixed(1)

    );

    setText(

        "industryScore",

        Number(

            candidate.industry_score

        ).toFixed(1)

    );

    setText(

        "assessmentScore",

        Number(

            candidate.assessment_score

        ).toFixed(1)

    );

    /* Recommendation Description */

    updateRecommendationDescription();

    /* Strengths */

    renderStrengths();

    /* Concerns */

    renderConcerns();

}

/* ==========================================================
   Recommendation Description
   ========================================================== */

function updateRecommendationDescription() {

    const element =

        document.getElementById(

            "recommendationDescription"

        );

    if(!element) return;

    const recommendation =

        candidate.recommendation;

    const descriptions = {

        "Elite Match":

            "Outstanding candidate with exceptional AI evaluation across all hiring dimensions.",

        "Strong Shortlist":

            "Highly recommended candidate with consistently strong performance.",

        "Shortlist":

            "Good candidate suitable for further recruiter evaluation.",

        "Needs Manual Review":

            "Candidate requires manual assessment before a hiring decision.",

        "Not Recommended":

            "Current evaluation indicates a low overall hiring suitability."

    };

    element.textContent =

        descriptions[recommendation] ||

        "AI recommendation generated successfully.";

}

/* ==========================================================
   Strengths
   ========================================================== */

function renderStrengths() {

    const container =

        document.getElementById(

            "strengthsContainer"

        );

    if(!container) return;

    container.innerHTML = "";

    const strengths =

        String(

            candidate.strengths || ""

        )

        .split(";")

        .filter(Boolean);

    strengths.forEach(item => {

        container.innerHTML += `

        <div class="analysis-item success">

            <span>✔</span>

            <p>${item.trim()}</p>

        </div>

        `;

    });

}

/* ==========================================================
   Concerns
   ========================================================== */

function renderConcerns() {

    const container =

        document.getElementById(

            "concernsContainer"

        );

    if(!container) return;

    container.innerHTML = "";

    const concerns =

        String(

            candidate.concerns || ""

        )

        .split(";")

        .filter(Boolean);

    concerns.forEach(item => {

        container.innerHTML += `

        <div class="analysis-item warning">

            <span>⚠</span>

            <p>${item.trim()}</p>

        </div>

        `;

    });

}
/* ==========================================================
   Create Charts
   ========================================================== */

function createCharts() {

    createFitChart();

    createRiskChart();

}

/* ==========================================================
   Fit Analysis Chart
   ========================================================== */

function createFitChart() {

    if (fitChart) {

        fitChart.destroy();

    }

    const canvas =

        document.getElementById(

            "fitChart"

        );

    if (!canvas) return;

    fitChart = new Chart(

        canvas,

        {

            type: "radar",

            data: {

                labels: [

                    "Technical",

                    "Experience",

                    "Behavior"

                ],

                datasets: [

                    {

                        label: "Candidate Fit",

                        data: [

                            Number(candidate.technical_fit),

                            Number(candidate.experience_fit),

                            Number(candidate.behavior_fit)

                        ],

                        backgroundColor:

                            "rgba(79,124,255,.20)",

                        borderColor:

                            "#4F7CFF",

                        pointBackgroundColor:

                            "#4F7CFF",

                        borderWidth: 2

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                scales: {

                    r: {

                        min: 0,

                        max: 100,

                        ticks: {

                            display: false

                        },

                        grid: {

                            color:

                            "rgba(255,255,255,.10)"

                        },

                        angleLines: {

                            color:

                            "rgba(255,255,255,.10)"

                        },

                        pointLabels: {

                            color: "#ffffff",

                            font: {

                                size: 13

                            }

                        }

                    }

                },

                plugins: {

                    legend: {

                        display: false

                    }

                }

            }

        }

    );

}

/* ==========================================================
   Risk Chart
   ========================================================== */

function createRiskChart() {

    if (riskChart) {

        riskChart.destroy();

    }

    const canvas =

        document.getElementById(

            "riskChart"

        );

    if (!canvas) return;

    const risk =

        Number(candidate.risk_score);

    riskChart = new Chart(

        canvas,

        {

            type: "doughnut",

            data: {

                labels: [

                    "Risk",

                    "Safe"

                ],

                datasets: [

                    {

                        data: [

                            risk,

                            100 - risk

                        ],

                        backgroundColor: [

                            "#FF5D73",

                            "#00D98B"

                        ],

                        borderWidth: 0

                    }

                ]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                cutout: "70%",

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        }

    );

}

/* ==========================================================
   Event Listeners
   ========================================================== */

function initializeEvents() {

    const refreshTop =

        document.getElementById(

            "refreshCandidate"

        );

    const refreshBottom =

        document.getElementById(

            "refreshCandidateBottom"

        );

    const backButton =

        document.getElementById(

            "backDashboard"

        );

    if (refreshTop) {

        refreshTop.addEventListener(

            "click",

            async () => {

                await loadCandidate(

                    getCandidateId()

                );

            }

        );

    }

    if (refreshBottom) {

        refreshBottom.addEventListener(

            "click",

            async () => {

                await loadCandidate(

                    getCandidateId()

                );

            }

        );

    }

    if (backButton) {

        backButton.addEventListener(

            "click",

            () => {

                window.location.href =

                    "dashboard.html";

            }

        );

    }

}
/* ==========================================================
   Helper
   ========================================================== */

function setText(id, value) {

    const element = document.getElementById(id);

    if (!element) return;

    element.textContent = value ?? "--";

}

/* ==========================================================
   Loading Overlay
   ========================================================== */

function showLoading(show) {

    const loader = document.getElementById(

        "candidateLoading"

    );

    if (!loader) return;

    loader.classList.toggle(

        "hidden",

        !show

    );

}

/* ==========================================================
   Toast
   ========================================================== */

function showToast(

    message,

    type = "success"

) {

    if (

        typeof window.showToast ===

        "function"

    ) {

        window.showToast(

            message,

            type

        );

        return;

    }

    console.log(

        `[${type.toUpperCase()}] ${message}`

    );

}

/* ==========================================================
   Keyboard Shortcuts
   ========================================================== */

function initializeKeyboardShortcuts() {

    document.addEventListener(

        "keydown",

        async event => {

            /* Ctrl + R */

            if (

                event.ctrlKey &&

                event.key.toLowerCase() === "r"

            ) {

                event.preventDefault();

                await loadCandidate(

                    getCandidateId()

                );

            }

            /* Escape */

            if (

                event.key === "Escape"

            ) {

                window.location.href =

                    "dashboard.html";

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

            await loadCandidate(

                getCandidateId()

            );

        },

        60000

    );

}

/* ==========================================================
   Startup
   ========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    async () => {

        initializeEvents();

        initializeKeyboardShortcuts();

        initializeAutoRefresh();

        console.log(

            "%cCandidate Intelligence Connected",

            "color:#4F7CFF;font-size:15px;font-weight:bold;"

        );

    }

);

/* ==========================================================
   Public API
   ========================================================== */

window.CandidatePage = {

    reload() {

        return loadCandidate(

            getCandidateId()

        );

    },

    refresh() {

        return loadCandidate(

            getCandidateId()

        );

    },

    data() {

        return candidate;

    }

};

/* ==========================================================
   End of File
   ========================================================== */