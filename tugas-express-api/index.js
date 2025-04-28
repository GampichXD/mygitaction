const express = require("express");
const cors = require("cors");
const app = express();

app.use(express.json());
app.use(cors());

let products = [
    { id: 1, name: "Laptop", price: 1200 },
    { id: 2, name: "Smartphone", price: 800 }
];

// GET all products
app.get("/products", (req, res) => res.json(products));

// GET product by ID
app.get("/products/:id", (req, res) => {
    const product = products.find(p => p.id == req.params.id);
    product ? res.json(product) : res.status(404).send("Product not found");
});

// POST a new product
app.post("/products", (req, res) => {
    const newProduct = { id: products.length + 1, ...req.body };
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// PUT update a product
app.put("/products/:id", (req, res) => {
    const product = products.find(p => p.id == req.params.id);
    if (!product) return res.status(404).send("Product not found");
    Object.assign(product, req.body);
    res.json(product);
});

// DELETE a product
app.delete("/products/:id", (req, res) => {
    products = products.filter(p => p.id != req.params.id);
    res.send("Product deleted");
});

app.listen(3000, () => console.log("Server running on port 3000"));