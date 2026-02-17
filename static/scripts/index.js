const fileInput = document.getElementById("fileInput");
const themeIcon = document.getElementById("themeIcon");
const fileName = document.getElementById("fileName");

function toggleTheme(){
    document.body.classList.toggle("light");
    themeIcon.textContent =
        document.body.classList.contains("light") ? "🌞" : "🌙";
}

const uploadContent = document.getElementById("uploadContent");

fileInput.addEventListener("change", function(){

    if(fileInput.files.length > 0){

        const file = fileInput.files[0];

        if(file.type !== "application/pdf"){
            alert("Only PDF allowed");
            return;
        }

        uploadContent.innerHTML = `
            <img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="40">
            <p>${file.name}</p>
        `;
    }
});





async function uploadAndSend() {

    startScoreAnimation();

    const file = fileInput.files[0];
    const jobTitle = document.getElementById("jobTitle").value || "Software Engineer";

    if (!file) {
        alert("Please upload a resume PDF");
        return;
    }

    try {

        let scores = [];

        // 1️⃣ Upload Resume to Affinda
        const formData = new FormData();
        formData.append("file", file);
        formData.append("workspace", "rIRsmLKt");
        formData.append("extractor", "resume-v4");

        const affindaResponse = await fetch(
            "https://api.affinda.com/v3/documents",
            {
                method: "POST",
                headers: {
                    "Authorization": "Bearer aff_21dc93ca7b75f57abffe080aadf36fb58114bc35"
                },
                body: formData
            }
        );

        const affindaData = await affindaResponse.json();

        if (!affindaResponse.ok) {
            console.error("Affinda Error:", affindaData);
            return;
        }

        const rawText = affindaData.data.rawText || "";

        // 2️⃣ Extract Sections
        const structuredData = {
            summary: rawText,
            education: extractSection(rawText, "EDUCATION", null) || "no_mentionings_properly",
            skills: extractSection(rawText, "SKILLS", null) || "no_mentionings_properly",
            projects: extractSection(rawText, "PROJECTS", null) || "no_mentionings_properly",
            experience: extractSection(rawText, "EXPERIENCE", null) || "no_mentionings_properly",
            certifications: extractSection(rawText, "CERTIFICATIONS", null) || "no_mentionings_properly",
            achievements: extractSection(rawText, "ACHIEVEMENTS", null) || "no_mentionings_properly"
        };

        console.log("Structured Data:", structuredData);

        // ================= EDUCATION =================
        fetch("/education-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.education,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const educationCard = cards[1];
            const percentage = educationCard.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            educationCard.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            educationCard.appendChild(ul);
        })
        .catch(error => console.error("Error:", error));


        // ================= SKILLS =================
        fetch("/skills-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.skills,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const skillsCard = cards[2];
            const percentage = skillsCard.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            skillsCard.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            skillsCard.appendChild(ul);
        })
        .catch(error => console.error("Error:", error));


        // ================= PROJECTS =================
        fetch("/projects-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.projects,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[4];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));


        // ================= CERTIFICATIONS =================
        fetch("/certifications-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.certifications,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[5];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));


        // ================= ACHIEVEMENTS =================
        fetch("/achievements-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.achievements,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[6];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean.replace(/^\d+\.\s*/, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));


        // ================= EXPERIENCE =================
        fetch("/experience-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: structuredData.experience,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[3];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean.replace(/^\d+\.\s*/, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));


        // ================= OVERALL SUMMARY =================
        fetch("/overall-summary-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: rawText,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[0];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            stopScoreAnimation(score);

            document.getElementById("scoreValue").textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));


        // ================= CONTACT / OTHERS =================
        fetch("/others-api/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                data: rawText,
                job_title: jobTitle
            })
        })
        .then(response => response.json())
        .then(data => {

            const cards = document.querySelectorAll(".card");
            const card = cards[7];
            const percentage = card.querySelector(".percentage");

            const score = parseInt(
                (data.score || "").toString().match(/\d+/)?.[0] || 0
            );

            percentage.textContent = score + "%";

            card.querySelectorAll(".good, .bad, ul")
                .forEach(el => el.remove());

            const ul = document.createElement("ul");

            data.result.forEach(line => {
                const clean = line.trim();

                if (/^\d+\./.test(clean)) {
                    const li = document.createElement("li");
                    li.textContent = clean
                        .replace(/^\d+\.\s*/, "")
                        .replace(/\*\*/g, "");
                    ul.appendChild(li);
                }
            });

            card.appendChild(ul);
        })
        .catch(error => console.error(error));

    } catch (error) {
        console.error("Error:", error);
    }
}






let scoreInterval;

function startScoreAnimation() {

    const scoreElement = document.getElementById("scoreValue");

    let value = 0;
    let direction = 1;

    scoreInterval = setInterval(() => {

        scoreElement.textContent = value + "%";

        value += direction * 5;

        if (value >= 100) direction = -1;
        if (value <= 0) direction = 1;

    }, 30);
}




function stopScoreAnimation(finalScore) {

    clearInterval(scoreInterval);
    document.getElementById("scoreValue").textContent = finalScore + "%";
}






function extractSection(text, startKeyword, endKeyword) {

    if (!text) return "";

    const upperText = text.toUpperCase();

    const startIndex = upperText.indexOf(startKeyword.toUpperCase());
    if (startIndex === -1) return "";

    let endIndex = upperText.length;

    if (endKeyword) {
        const tempEnd = upperText.indexOf(endKeyword.toUpperCase(), startIndex + startKeyword.length);
        if (tempEnd !== -1) {
            endIndex = tempEnd;
        }
    }

    return text.substring(startIndex, endIndex).trim();
}



