const express = require("express");
const router = express.Router();
const { createTodo, updateTodo } = require("../types/validation");
const Todo = require("../models/todo");

router.post("/", async (req, res) => {
    try {
        const { title, description, completed, priority } = req.body;
        const todoCreation = createTodo.safeParse({ title, description, completed, priority });

        if (!todoCreation.success) {
            return res.status(400).json({ error: todoCreation.error });
        }

        const newTodo = await Todo.create({ title, description, completed, priority });
        res.json(newTodo);
    } catch (error) {
        console.error("Error creating todo:", error);
        res.status(500).json({ error: "Internal server error" });
    }
});

router.get("/", async (req, res) => {
    try {
        const todos = await Todo.find({}).sort({ priority: 1 }); // Sort by priority
        res.status(200).json({ todos });
    } catch (error) {
        console.error("Error fetching todos:", error);
        res.status(500).json({ error: "Internal server error" });
    }
});

router.put("/:id", async (req, res) => {
    const parsePayload = updateTodo.safeParse({ ...req.body, id: req.params.id });

    if (!parsePayload.success) {
        return res.status(400).json({ error: parsePayload.error });
    }

    try {
        const updatedTodo = await Todo.findByIdAndUpdate(req.params.id, req.body, { new: true });

        if (!updatedTodo) {
            return res.status(404).json({ error: "Todo not found" });
        }

        res.status(200).json(updatedTodo);
    } catch (error) {
        console.error("Error updating todo:", error);
        res.status(500).json({ error: "Internal server error" });
    }
});

router.delete("/:id", async (req, res) => {
    try {
        const deletedTodo = await Todo.findByIdAndDelete(req.params.id);

        if (!deletedTodo) {
            return res.status(404).json({ error: "Todo not found" });
        }

        res.status(200).json({ msg: "Todo deleted" });
    } catch (error) {
        console.error("Error deleting todo:", error);
        res.status(500).json({ error: "Internal server error" });
    }
});

module.exports = router;
