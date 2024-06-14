const express = require("express");
const app = express();
const path = require("path");
const dotenv = require("dotenv");
dotenv.config({ path: path.resolve(__dirname, "./.env") });
const port = parseInt(process.env.PORT);

const jwtPassword = process.env.JWT_PASSWORD;

const { createTodo, updateTodo } = require("./types");

const { todo } = require("./db");

const cors = require("cors");
app.use(express.json());
app.use(cors({ origin: "http://localhost:5173" }));

// Create a new todo
app.post("/todos", async function (req, res) {
    try {
      const { title, description, completed, priority, deadline } = req.body;
      const todoCreation = await createTodo.safeParse({
        title: title,
        description: description,
        completed: completed,
        priority: priority,
        deadline: new Date(deadline)
      });
      if (!todoCreation.success) {
        res.status(400).json({ err: "todo not safeparsed", error: todoCreation.error });
      } else {
        await todo.create({
          title: title,
          description: description,
          completed: completed,
          priority: priority,
          deadline: deadline
        });
        res.json({ msg: "todo created" });
      }
    } catch (error) {
      console.error("JSON parsing error:", error);
      res.status(400).json({ error: "Invalid JSON format", err: error });
    }
  });
  
  app.put("/todos/:id", async function (req, res) {
    const { id } = req.params;
    const { title, description, completed, priority, deadline } = req.body;
    try {
      const updatedTodo = await todo.findByIdAndUpdate(
        id,
        { title, description, completed, priority, deadline },
        { new: true }
      );
      if (!updatedTodo) {
        return res.status(404).json({ msg: "Todo not found" });
      }
      res.status(200).json({ msg: "todo updated", todo: updatedTodo });
    } catch (err) {
      res.status(400).json({ msg: "update todo failed", error: err });
    }
  });
  

// Get all todos
app.get("/todos", async function (req, res) {
    try {
        const todos = await todo.find({});
        res.status(200).json({ todos });
    } catch (err) {
        res.status(400).json({ msg: "can't get the todo" });
    }
});

// Update a todo (mark as completed)
app.put("/completed", async function (req, res) {
    const { id } = req.body;
    const parsePayload = updateTodo.safeParse({ id });
    if (!parsePayload.success) {
        res.status(400).json({ msg: "not able to parse the update todo", err: parsePayload.error });
    } else {
        try {
            const updatedTodo = await todo.findByIdAndUpdate(id, { completed: true }, { new: true });
            if (!updatedTodo) {
                return res.status(404).json({ msg: "Todo not found" });
            }
            res.status(200).json({ msg: "todo updated", todo: updatedTodo });
        } catch (err) {
            res.status(400).json({ msg: "update todo failed" });
        }
    }
});

// Delete a todo
app.delete("/todos/:id", async function (req, res) {
    try {
        const { id } = req.params;
        const deletedTodo = await todo.findByIdAndDelete(id);
        if (!deletedTodo) {
            return res.status(404).json({ msg: "Todo not found" });
        }
        res.status(200).json({ msg: "todo deleted" });
    } catch (err) {
        res.status(400).json({ msg: "delete todo failed" });
    }
});

// Sort todos by priority
app.get("/todos/sort/:priority", async function (req, res) {
    try {
        const { priority } = req.params;
        const todos = await todo.find({ priority }).sort({ completed: 1, title: 1 });
        res.status(200).json({ todos });
    } catch (err) {
        res.status(400).json({ msg: "can't get sorted todos" });
    }
});




// app.put("/todos/:id", async function (req, res) {
//     const { id } = req.params;
//     const { title, description, completed, priority } = req.body;
//     try {
//         const updatedTodo = await todo.findByIdAndUpdate(
//             id,
//             { title, description, completed, priority },
//             { new: true }
//         );
//         if (!updatedTodo) {
//             return res.status(404).json({ msg: "Todo not found" });
//         }
//         res.status(200).json({ msg: "todo updated", todo: updatedTodo });
//     } catch (err) {
//         res.status(400).json({ msg: "update todo failed", error: err });
//     }
// });






app.listen(port, () => {
    console.log("we are running server on " + port);
});

module.exports = {
    port: "qafdadsfaedfadsfdsfe",
    jwtPassword: jwtPassword,
};
