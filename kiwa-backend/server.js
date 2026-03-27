const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Test route
app.get("/", (req, res) => {
    res.send("Kiwa Energy Backend is running 🚀");
});

// Contact route
app.post("/contact", (req, res) => {
    const { name, email, message } = req.body;

    console.log("New Message:");
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Message:", message);

    res.send("Message received successfully!");
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});