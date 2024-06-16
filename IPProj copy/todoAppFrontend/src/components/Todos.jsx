import { useState } from "react";
import { EditTodo } from "./EditTodo";

export function Todos({ todos, onTodoUpdated }) {
  const [editingTodo, setEditingTodo] = useState(null);

  const handleComplete = async (id) => {
    try {
      await fetch("http://localhost:3000/completed", {
        method: "PUT",
        body: JSON.stringify({ id: id }),
        headers: {
          "Content-Type": "application/json"
        }
      });
      onTodoUpdated();
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`http://localhost:3000/todos/${id}`, {
        method: "DELETE"
      });
      onTodoUpdated();
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  const handleEdit = (todo) => {
    setEditingTodo(todo);
  };

  const handleCancel = () => {
    setEditingTodo(null);
  };

  const handleSave = () => {
    setEditingTodo(null);
    onTodoUpdated();
  };

  if (editingTodo) {
    return (
      <EditTodo todo={editingTodo} onSave={handleSave} onCancel={handleCancel} />
    );
  }

  return (
    <div className="mt-4 grid grid-cols-1 gap-4">
      {todos.map((todo) => (
        <div key={todo._id} className="p-4 bg-white rounded-md shadow-md">
          <h1 className="text-xl font-bold">{todo.title}</h1>
          <h2 className="text-lg">{todo.description}</h2>
          <h3 className="text-md text-gray-500">{todo.priority} priority</h3>
          <h4 className={todo.completed ? "text-green-500" : "text-red-500"}>
            {todo.completed ? "Completed" : "Incomplete"}
          </h4>
          <h5 className="text-sm">Date Added: {new Date(todo.dateAdded).toLocaleDateString()}</h5>
          <h5 className="text-sm">Deadline: {new Date(todo.deadline).toLocaleDateString()}</h5>
          {!todo.completed && (
              //   className="p-2 m-2 bg-green-500 text-white rounded"
            <button 
              className="p-2 m-2 bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500  rounded"
              onClick={() => handleComplete(todo._id)}
            >
              Mark as Completed
            </button>
          )}
          <button 
            className="p-2 m-2 bg-yellow-500 text-white rounded"
            onClick={() => handleEdit(todo)}
          >
            Edit
          </button>
          <button 
            className="p-2 m-2 bg-red-500 text-white rounded"
            onClick={() => handleDelete(todo._id)}
          >
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}
