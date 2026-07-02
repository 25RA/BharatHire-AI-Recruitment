/* ==========================================================
   BharatHire
   app.js
   Part 1
   Landing Page Controller
   ========================================================== */

"use strict";

/* ==========================================================
   DOM Ready
   ========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initializeApplication();

});

/* ==========================================================
   Initialize
   ========================================================== */

function initializeApplication(){

    initializeLoader();

    initializeNavbar();

    initializeSpotlight();

    initializeScrollReveal();

    initializeCounters();

    initializeSmoothScroll();

    initializeScrollTop();

    initializeBackendStatus();

}

/* ==========================================================
   Loader
   ========================================================== */

function initializeLoader(){

    const loader = document.getElementById("loader");

    if(!loader) return;

    window.addEventListener("load",()=>{

        setTimeout(()=>{

            loader.style.opacity="0";

            loader.style.visibility="hidden";

            loader.style.pointerEvents="none";

        },700);

    });

}

/* ==========================================================
   Sticky Navbar
   ========================================================== */

function initializeNavbar(){

    const header=document.querySelector("header");

    if(!header) return;

    window.addEventListener("scroll",()=>{

        if(window.scrollY>60){

            header.classList.add("navbar-scrolled");

        }

        else{

            header.classList.remove("navbar-scrolled");

        }

    });

}

/* ==========================================================
   Mouse Spotlight
   ========================================================== */

function initializeSpotlight(){

    const spotlight=document.getElementById("spotlight");

    if(!spotlight) return;

    document.addEventListener("mousemove",(event)=>{

        spotlight.style.left=event.clientX+"px";

        spotlight.style.top=event.clientY+"px";

    });

}

/* ==========================================================
   Smooth Scroll
   ========================================================== */

function initializeSmoothScroll(){

    const links=document.querySelectorAll('a[href^="#"]');

    links.forEach(link=>{

        link.addEventListener("click",(event)=>{

            event.preventDefault();

            const target=document.querySelector(

                link.getAttribute("href")

            );

            if(target){

                target.scrollIntoView({

                    behavior:"smooth",

                    block:"start"

                });

            }

        });

    });

}

/* ==========================================================
   Scroll Reveal
   ========================================================== */

function initializeScrollReveal(){

    const elements=document.querySelectorAll(

        ".feature-card,.metric-card,.timeline-item,.cta-box,.glass-panel,.section-title"

    );

    elements.forEach(element=>{

        element.classList.add("reveal");

    });

    const observer=new IntersectionObserver(

        (entries)=>{

            entries.forEach(entry=>{

                if(entry.isIntersecting){

                    entry.target.classList.add("active");

                }

            });

        },

        {

            threshold:.15

        }

    );

    elements.forEach(element=>{

        observer.observe(element);

    });

}

/* ==========================================================
   Animated Counters
   ========================================================== */

function initializeCounters(){

    animateCounter(

        "candidateCounter",

        100000,

        "",

        2200

    );

    animateCounter(

        "accuracyCounter",

        99.2,

        "%",

        1800

    );

    animateCounter(

        "recommendationCounter",

        850,

        "",

        1800

    );

}

function animateCounter(

    id,

    target,

    suffix="",

    duration=2000

){

    const element=document.getElementById(id);

    if(!element) return;

    let start=0;

    const increment=target/(duration/16);

    function update(){

        start+=increment;

        if(start>=target){

            element.textContent=

            target+suffix;

            return;

        }

        if(Number.isInteger(target)){

            element.textContent=

            Math.floor(start)+suffix;

        }

        else{

            element.textContent=

            start.toFixed(1)+suffix;

        }

        requestAnimationFrame(update);

    }

    update();

}

/* ==========================================================
   Scroll To Top
   ========================================================== */

function initializeScrollTop(){

    const button=document.getElementById("scrollTop");

    if(!button) return;

    window.addEventListener("scroll",()=>{

        if(window.scrollY>500){

            button.classList.add("show");

        }

        else{

            button.classList.remove("show");

        }

    });

    button.addEventListener("click",()=>{

        window.scrollTo({

            top:0,

            behavior:"smooth"

        });

    });

}

/* ==========================================================
   Backend Status
   ========================================================== */

async function initializeBackendStatus(){

    const status=document.getElementById("backendStatus");

    if(!status) return;

    try{

        const response=await API.getServerStatus();

        status.textContent="Online";

        status.style.color="#00D98B";

        console.log("Backend:",response);

    }

    catch(error){

        status.textContent="Offline";

        status.style.color="#FF5D73";

        console.error(error);

    }

}
/* ==========================================================
   Toast Notification System
   ========================================================== */

function showToast(message, type = "success") {

    let container = document.querySelector(".toast-container");

    if (!container) {

        container = document.createElement("div");
        container.className = "toast-container";

        document.body.appendChild(container);

    }

    const toast = document.createElement("div");

    toast.className = `toast ${type}`;

    toast.innerHTML = `
        <span class="toast-message">${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {

        toast.style.opacity = "0";
        toast.style.transform = "translateX(100%)";

        setTimeout(() => {

            toast.remove();

        }, 300);

    }, 3500);

}

/* ==========================================================
   CTA Buttons
   ========================================================== */

function initializeCTAButtons() {

    const dashboardButtons = document.querySelectorAll(
        ".primary-btn"
    );

    dashboardButtons.forEach(button => {

        button.addEventListener("click", () => {

            if (button.dataset.skip)
                return;

            console.log("Opening Dashboard");

        });

    });

}

/* ==========================================================
   Load Analytics Preview
   ========================================================== */

async function loadAnalyticsPreview() {

    try {

        const analytics = await API.getAnalytics();

        console.log("Analytics:", analytics);

        if (
            analytics.total_candidates &&
            document.getElementById("candidateCounter")
        ) {

            document.getElementById(
                "candidateCounter"
            ).textContent = analytics.total_candidates;

        }

    }

    catch (error) {

        console.error(error);

    }

}

/* ==========================================================
   Window Online
   ========================================================== */

window.addEventListener("online", () => {

    showToast(
        "Internet Connection Restored",
        "success"
    );

});

/* ==========================================================
   Window Offline
   ========================================================== */

window.addEventListener("offline", () => {

    showToast(
        "You are Offline",
        "error"
    );

});

/* ==========================================================
   Keyboard Shortcuts
   ========================================================== */

document.addEventListener("keydown", event => {

    if (event.key === "/") {

        const search = document.querySelector(
            "input[type='search']"
        );

        if (search) {

            event.preventDefault();

            search.focus();

        }

    }

    if (
        event.ctrlKey &&
        event.key.toLowerCase() === "k"
    ) {

        event.preventDefault();

        showToast(
            "Quick Search Coming Soon",
            "warning"
        );

    }

});

/* ==========================================================
   Visibility Change
   ========================================================== */

document.addEventListener(
    "visibilitychange",
    () => {

        if (document.hidden) {

            console.log(
                "Application in Background"
            );

        }

        else {

            console.log(
                "Application Active"
            );

        }

    }
);

/* ==========================================================
   Refresh Backend Status
   ========================================================== */

setInterval(async () => {

    const status =
        document.getElementById("backendStatus");

    if (!status)
        return;

    try {

        await API.getServerStatus();

        status.textContent = "Online";

        status.style.color = "#00D98B";

    }

    catch {

        status.textContent = "Offline";

        status.style.color = "#FF5D73";

    }

}, 30000);

/* ==========================================================
   Utility Functions
   ========================================================== */

function debounce(callback, delay = 300) {

    let timeout;

    return (...args) => {

        clearTimeout(timeout);

        timeout = setTimeout(() => {

            callback(...args);

        }, delay);

    };

}

function throttle(callback, limit = 150) {

    let waiting = false;

    return (...args) => {

        if (waiting)
            return;

        callback(...args);

        waiting = true;

        setTimeout(() => {

            waiting = false;

        }, limit);

    };

}

/* ==========================================================
   Back To Top Keyboard
   ========================================================== */

document.addEventListener("keydown", event => {

    if (event.key === "Home") {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    }

});

/* ==========================================================
   Application Boot
   ========================================================== */

window.addEventListener("load", () => {

    initializeCTAButtons();

    loadAnalyticsPreview();

    console.log(
        "%cBharatHire Loaded Successfully",
        "color:#4F7CFF;font-size:16px;font-weight:bold;"
    );

});