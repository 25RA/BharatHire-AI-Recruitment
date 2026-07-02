/* ==========================================================
   BharatHire
   charts.js
   Backend Integrated
   Part 1
   ========================================================== */

"use strict";

/* ==========================================================
   Chart Storage
   ========================================================== */

const DashboardCharts = {};

/* ==========================================================
   Destroy Existing Chart
   ========================================================== */

function destroyChart(name){

    if(DashboardCharts[name]){

        DashboardCharts[name].destroy();

        DashboardCharts[name]=null;

    }

}

/* ==========================================================
   Global Chart Theme
   ========================================================== */

Chart.defaults.color="#b6bfd6";

Chart.defaults.font.family="Inter";

Chart.defaults.borderColor=

"rgba(255,255,255,.08)";

const chartOptions={

    responsive:true,

    maintainAspectRatio:false,

    plugins:{

        legend:{

            labels:{

                color:"#ffffff"

            }

        }

    }

};

/* ==========================================================
   Recommendation Distribution
   ========================================================== */

function createRecommendationChart(

    recommendations={}

){

    destroyChart(

        "recommendation"

    );

    const canvas=

    document.getElementById(

        "recommendationChart"

    );

    if(!canvas) return;

    DashboardCharts.recommendation=

    new Chart(

        canvas,

        {

            type:"doughnut",

            data:{

                labels:[

                    "Elite Match",

                    "Strong Shortlist",

                    "Shortlist",

                    "Needs Manual Review",

                    "Not Recommended"

                ],

                datasets:[{

                    data:[

                        recommendations["Elite Match"] || 0,

                        recommendations["Strong Shortlist"] || 0,

                        recommendations["Shortlist"] || 0,

                        recommendations["Needs Manual Review"] || 0,

                        recommendations["Not Recommended"] || 0

                    ],

                    backgroundColor:[

                        "#00D98B",

                        "#4F7CFF",

                        "#7C5CFF",

                        "#FFC857",

                        "#FF5D73"

                    ],

                    borderWidth:0

                }]

            },

            options:{

                ...chartOptions,

                cutout:"68%"

            }

        }

    );

}
/* ==========================================================
   Component Score Chart
   ========================================================== */

function createComponentChart(
    scores = {}
){

    destroyChart("components");

    const canvas =
        document.getElementById(
            "componentChart"
        );

    if(!canvas) return;

    DashboardCharts.components =
    new Chart(
        canvas,
        {
            type:"bar",

            data:{

                labels:[

                    "Skill",

                    "Experience",

                    "Career",

                    "Behavior",

                    "Industry",

                    "Assessment"

                ],

                datasets:[{

                    label:"Average Score",

                    data:[

                        scores.skill_score || 0,

                        scores.experience_score || 0,

                        scores.career_score || 0,

                        scores.behavior_score || 0,

                        scores.industry_score || 0,

                        scores.assessment_score || 0

                    ],

                    borderRadius:10,

                    backgroundColor:[

                        "#4F7CFF",

                        "#6A8DFF",

                        "#7C5CFF",

                        "#00D98B",

                        "#FFC857",

                        "#FF8A5B"

                    ]

                }]

            },

            options:{

                ...chartOptions,

                scales:{

                    y:{

                        beginAtZero:true,

                        max:100

                    }

                }

            }

        }

    );

}

/* ==========================================================
   Confidence Gauge
   ========================================================== */

function updateConfidenceGauge(
    confidence = 0
){

    const gauge =
        document.getElementById(
            "confidenceValue"
        );

    if(gauge){

        gauge.textContent =
            `${Number(confidence).toFixed(1)}%`;

    }

}

/* ==========================================================
   Update Dashboard Charts
   ========================================================== */

function updateDashboardCharts(data){

    createRecommendationChart(

        data.recommendations

    );

    createComponentChart(

        data.componentScores

    );

    updateConfidenceGauge(

        data.confidence

    );

}

/* ==========================================================
   Resize Handling
   ========================================================== */

window.addEventListener(

    "resize",

    () => {

        Object.values(

            DashboardCharts

        ).forEach(chart => {

            if(chart){

                chart.resize();

            }

        });

    }

);

/* ==========================================================
   Public API
   ========================================================== */

window.ChartManager = {

    updateDashboardCharts,

    recommendationChart:
        createRecommendationChart,

    componentChart:
        createComponentChart,

    confidenceGauge:
        updateConfidenceGauge

};

/* ==========================================================
   End of File
   ========================================================== */