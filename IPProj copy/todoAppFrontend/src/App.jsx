import { useState, useEffect } from 'react';
import { CreateTodo } from './components/CreateTodo';
import { Todos } from './components/Todos';
import './App.css';
import 'tailwindcss/tailwind.css';
import { Navbar } from './components/Navbar';

function App() {
  const [todos, setTodos] = useState([]);
  const [priority, setPriority] = useState("all");

  const fetchData = async (priority) => {
    try {
      let url = 'http://localhost:3000/todos';
      if (priority !== "all") {
        url += `/sort/${priority}`;
      }
      const response = await fetch(url);
      const data = await response.json();
      setTodos(data.todos);
    } catch (error) {
      console.error('Error fetching todos:', error);
    }
  };

  useEffect(() => {
    fetchData(priority);
  }, [priority]);

  return (
    <div className="bg-gradient-to-r from-green-400 to-blue-500  container mx-auto p-4">
      <Navbar>. </Navbar>
      <br />
      <CreateTodo onTodoCreated={() => fetchData(priority)} />
      <div className="my-4">
        <label className="font-bold mr-2">Filter by Priority: </label>
        <select 
          onChange={(e) => setPriority(e.target.value)} 
          value={priority}
          className="p-2 border rounded"
        >
          <option value="all">All</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>
      <Todos todos={todos} onTodoUpdated={() => fetchData(priority)} />
    </div>
  );
}

export default App;
