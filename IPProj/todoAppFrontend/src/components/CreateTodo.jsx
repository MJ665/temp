import React, { useState } from "react";

export function CreateTodo({ onTodoCreated }) {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const [priority, setPriority] = useState("low");
  const [deadline, setDeadline] = useState("");

  const handleSubmit = async () => {
    try {
      await fetch("http://localhost:3000/todos", {
        method: "POST",
        body: JSON.stringify({
          title: title,
          description: desc,
          completed: false,
          priority: priority,
          deadline: deadline
        }),
        headers: {
          "Content-Type": "application/json"
        }
      });
      onTodoCreated();
    } catch (error) {
      console.error("Error creating todo:", error);
    }
  };

  return (
    <div className="p-4 bg-gray-100 rounded-md shadow-md max-w-lg mx-auto">
      <h2 className="text-xl font-bold mb-4">Create a New Todo</h2>
      <input
        id="title"
        onChange={(e) => setTitle(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="text"
        placeholder="Title"
      />
      <input
        id="desc"
        onChange={(e) => setDesc(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="text"
        placeholder="Description"
      />
      <select
        id="priority"
        onChange={(e) => setPriority(e.target.value)}
        value={priority}
        className="p-2 m-2 w-full border rounded"
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>
      <input
        id="deadline"
        onChange={(e) => setDeadline(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="date"
      />
      <button
        className="p-2 m-2 w-full bg-blue-500 text-white rounded"
        onClick={handleSubmit}
      >
        Add a Task
      </button>
    </div>
  );
}
