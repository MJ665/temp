import { useState } from "react";

export function EditTodo({ todo, onSave, onCancel }) {
  const [title, setTitle] = useState(todo.title);
  const [desc, setDesc] = useState(todo.description);
  const [priority, setPriority] = useState(todo.priority);
  const [completed, setCompleted] = useState(todo.completed);
  const [deadline, setDeadline] = useState(todo.deadline ? todo.deadline.slice(0, 10) : "");

  const handleSubmit = async () => {
    try {
      await fetch(`http://localhost:3000/todos/${todo._id}`, {
        method: "PUT",
        body: JSON.stringify({
          title: title,
          description: desc,
          completed: completed,
          priority: priority,
          deadline: deadline
        }),
        headers: {
          "Content-Type": "application/json"
        }
      });
      onSave();
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  return (
    <div className="p-4 bg-gray-100 rounded-md shadow-md">
      <input
        id="title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="text"
        placeholder="Title"
      />
      <input
        id="desc"
        value={desc}
        onChange={(e) => setDesc(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="text"
        placeholder="Description"
      />
      <select
        id="priority"
        value={priority}
        onChange={(e) => setPriority(e.target.value)}
        className="p-2 m-2 w-full border rounded"
      >
        <option value="low">Low</option>
        <option value="medium">Medium</option>
        <option value="high">High</option>
      </select>
      <input
        id="deadline"
        value={deadline}
        onChange={(e) => setDeadline(e.target.value)}
        className="p-2 m-2 w-full border rounded"
        type="date"
      />
      <label className="block my-2">
        <input
          type="checkbox"
          checked={completed}
          onChange={(e) => setCompleted(e.target.checked)}
          className="mr-2"
        />
        Completed
      </label>
      <button
        className="p-2 m-2 w-full bg-blue-500 text-white rounded"
        onClick={handleSubmit}
      >
        Save
      </button>
      <button
        className="p-2 m-2 w-full bg-gray-500 text-white rounded"
        onClick={onCancel}
      >
        Cancel
      </button>
    </div>
  );
}
