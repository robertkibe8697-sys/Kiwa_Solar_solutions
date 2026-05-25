document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // HAMBURGER MENU
    // =========================
    const hamburger = document.getElementById("menu-toggle");
    const navLinks = document.getElementById("navLinks");

    if (hamburger && navLinks) {
        hamburger.addEventListener("click", () => {
            navLinks.classList.toggle("active");
        });
    }

    // =========================
    // CONTACT FORM
    // =========================
    const form = document.querySelector("#contact-form");

    console.log("Form found:", form);

    if (form) {

        const submitBtn = form.querySelector("button[type='submit']");
        const messageBox = document.getElementById("responseMessage");
        const btnText = document.getElementById("btnText");

        form.addEventListener("submit", async function (e) {

            // Prevent page refresh
            e.preventDefault();

            console.log("FORM SUBMITTED");

            // Disable button while sending
            if (submitBtn) {
                submitBtn.disabled = true;
            }

            // Change button text
            if (btnText) {
                btnText.innerText = "Sending...";
            }

            // Collect form data
            const data = {
                name: form.querySelector("input[name='name']").value,
                email: form.querySelector("input[name='email']").value,
                message: form.querySelector("textarea[name='message']").value
            };

            try {

                // Send data to Django backend
                const res = await fetch("/api/contact/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                });

                // Handle server errors
                if (!res.ok) {
                    throw new Error(`Server error: ${res.status}`);
                }

                // Convert response to JSON
                const responseData = await res.json();

                console.log(responseData);

                // Show success message
                if (messageBox) {
                    messageBox.innerText = responseData.message || "Message sent successfully!";
                    messageBox.style.color = "green";
                }

                // Clear form
                form.reset();

            } catch (error) {

                console.error("ERROR:", error);

                // Show error message
                if (messageBox) {
                    messageBox.innerText = "Error sending message";
                    messageBox.style.color = "red";
                }

            } finally {

                // Re-enable button
                if (submitBtn) {
                    submitBtn.disabled = false;
                }

                // Restore button text
                if (btnText) {
                    btnText.innerText = "Send Message";
                }
            }
        });
    }
});