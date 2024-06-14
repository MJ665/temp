import { useState } from "react";

export function CreateTodo({ setTodos }) {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const [priority, setPriority] = useState("low");

  const handleAddTodo = async () => {
    try {
      const response = await fetch("http://localhost:3000/todos", {
        method: "POST",
        body: JSON.stringify({
          title,
          description: desc,
          completed: false,
          priority
        }),
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (!response.ok) {
        throw new Error("Error adding todo");
      }

      const newTodo = await response.json();
      setTodos(prevTodos => [...prevTodos, newTodo]);
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  return (
    <div>
      <input
        id="title"
        onChange={(e) => setTitle(e.target.value)}
        style={{ padding: 10, margin: 10, background: "gray", color: "green" }}
        type="text"
        placeholder="Title"
      />
      <input
        id="desc"
        onChange={(e) => setDesc(e.target.value)}
        style={{ padding: 10, margin: 10, background: "black", color: "red" }}
        type="text"
        placeholder="Description"
      />
      <select
        value={priority}
        onChange={(e) => setPriority(e.target.value)}
        style={{ padding: 10, margin: 10 }}
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>
      <button style={{ padding: 10, margin: 10 }} onClick={handleAddTodo}>
        Add a Todo
      </button>
    </div>
  );
}
