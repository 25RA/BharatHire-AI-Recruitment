/* ==========================================================
   BharatHire
   particles.js
   Premium AI Particle Background
   ========================================================== */

"use strict";

/* ==========================================================
   Canvas
   ========================================================== */

const canvas = document.getElementById("particleCanvas");

if (canvas) {

    const ctx = canvas.getContext("2d");

    let particles = [];

    const mouse = {

        x: null,
        y: null,
        radius: 150

    };

    /* ==========================================================
       Resize Canvas
       ========================================================== */

    function resizeCanvas() {

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

    }

    resizeCanvas();

    window.addEventListener("resize", resizeCanvas);

    /* ==========================================================
       Mouse Tracking
       ========================================================== */

    window.addEventListener("mousemove", (event) => {

        mouse.x = event.clientX;
        mouse.y = event.clientY;

    });

    window.addEventListener("mouseout", () => {

        mouse.x = null;
        mouse.y = null;

    });

    /* ==========================================================
       Particle Class
       ========================================================== */

    class Particle {

        constructor() {

            this.reset();

        }

        reset() {

            this.x = Math.random() * canvas.width;

            this.y = Math.random() * canvas.height;

            this.radius = Math.random() * 2 + 1;

            this.speedX = (Math.random() - 0.5) * 0.5;

            this.speedY = (Math.random() - 0.5) * 0.5;

        }

        update() {

            this.x += this.speedX;

            this.y += this.speedY;

            if (this.x < 0 || this.x > canvas.width)
                this.speedX *= -1;

            if (this.y < 0 || this.y > canvas.height)
                this.speedY *= -1;

            if (mouse.x !== null) {

                const dx = this.x - mouse.x;
                const dy = this.y - mouse.y;

                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < mouse.radius) {

                    this.x += dx / 30;

                    this.y += dy / 30;

                }

            }

        }

        draw() {

            ctx.beginPath();

            ctx.arc(

                this.x,

                this.y,

                this.radius,

                0,

                Math.PI * 2

            );

            ctx.fillStyle = "rgba(120,170,255,0.8)";

            ctx.fill();

        }

    }

    /* ==========================================================
       Create Particles
       ========================================================== */

    function createParticles() {

        particles = [];

        let total = 90;

        if (window.innerWidth < 768)
            total = 45;

        if (window.innerWidth > 1700)
            total = 130;

        for (let i = 0; i < total; i++) {

            particles.push(new Particle());

        }

    }

    createParticles();

    window.addEventListener("resize", createParticles);

    /* ==========================================================
       Connection Lines
       ========================================================== */

    function connectParticles() {

        for (let a = 0; a < particles.length; a++) {

            for (let b = a + 1; b < particles.length; b++) {

                const dx = particles[a].x - particles[b].x;

                const dy = particles[a].y - particles[b].y;

                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 130) {

                    const opacity = 1 - distance / 130;

                    ctx.beginPath();

                    ctx.moveTo(

                        particles[a].x,

                        particles[a].y

                    );

                    ctx.lineTo(

                        particles[b].x,

                        particles[b].y

                    );

                    ctx.strokeStyle =
                        `rgba(79,124,255,${opacity * 0.25})`;

                    ctx.lineWidth = 1;

                    ctx.stroke();

                }

            }

        }

    }

    /* ==========================================================
       Animation Loop
       ========================================================== */

    function animate() {

        ctx.clearRect(

            0,

            0,

            canvas.width,

            canvas.height

        );

        particles.forEach((particle) => {

            particle.update();

            particle.draw();

        });

        connectParticles();

        requestAnimationFrame(animate);

    }

    animate();

}