document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // HAMBURGER MENU
    // =========================
  const menuToggle = document.getElementById("menu-toggle");
    const navLinks = document.querySelector(".nav-links");

   if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", function(e){
        e.stopPropagation();
        navLinks.classList.toggle("active");
    });

    document.addEventListener("click", function(){
        navLinks.classList.remove("active");
    });

    window.addEventListener("scroll", function(){
        navLinks.classList.remove("active");
    });
}
     const whatsappBtn = document.querySelector(".whatsapp-float");

    whatsappBtn.style.opacity = "0";
    whatsappBtn.style.transform = "translateY(50px)";

    setTimeout(() => {
        whatsappBtn.style.transition = "all 0.5s ease";
        whatsappBtn.style.opacity = "1";
        whatsappBtn.style.transform = "translateY(0)";
    }, 500);


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