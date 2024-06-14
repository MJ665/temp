export function Todos({ todos, setTodos }) {
    const handleDelete = async (id) => {
      try {
        await fetch(`http://localhost:3000/todos/${id}`, { method: "DELETE" });
        setTodos(prevTodos => prevTodos.filter(todo => todo._id !== id));
      } catch (error) {
        console.error("Error deleting todo:", error);
      }
    };
  
    const handleToggleCompletion = async (id, completed) => {
      try {
        const response = await fetch(`http://localhost:3000/todos/${id}`, {
          method: "PUT",
          body: JSON.stringify({ completed: !completed }),
          headers: {
            "Content-Type": "application/json"
          }
        });
  
        if (!response.ok) {
          throw new Error("Error updating todo");
        }
  
        const updatedTodo = await response.json();
        setTodos(prevTodos => prevTodos.map(todo => todo._id === id ? updatedTodo : todo));
      } catch (error) {
        console.error("Error updating todo:", error);
      }
    };
  
    return (
      <div>
        {todos.map((todo) => (
          <div key={todo._id}>
            <h1>{todo.title}</h1>
            <h1>{todo.description}</h1>
            <h1>{todo.completed ? "Completed" : "Mark as Completed"}</h1>
            <h1>Priority: {todo.priority}</h1>
            <button onClick={() => handleToggleCompletion(todo._id, todo.completed)}>
              {todo.completed ? "Mark as Incomplete" : "Mark as Completed"}
            </button>
            <button onClick={() => handleDelete(todo._id)}>Delete</button>
          </div>
        ))}
      </div>
    );
  }
  