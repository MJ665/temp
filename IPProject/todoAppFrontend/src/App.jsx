
// infinite server request is going in the fetch call  is the issue in this code


// import { useState } from 'react'
// import {CreateTodo} from "./components/CreateTodo"
// import {Todos} from "./components/Todos"
// import './App.css'

//  function App() {
// const [todos,setTodos]= useState ([])

//  fetch("http://localhost:3000/todos").then(async(response)=>{
//   const json  = await response.json()
//   console.log(JSON.stringify(json.todos))
//   setTodos (json.todos)
// })

//   return (
//     <div>
//           <CreateTodo></CreateTodo>
//           <Todos todos = {[{
//             title: "1", description:"11", completed:true
//           },{
//             title: "2", description:"22", completed:false
//           }]}></Todos>
//           <Todos todos = {todos}></Todos>
//       hi there
//     </div>
//   )
// }

// export default App













// porper older code had infinite server request is going in the fetch call solved by gpt
import { useState, useEffect } from 'react';
import { CreateTodo } from './components/CreateTodo';
import { Todos } from './components/Todos';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3000/todos');
        const data = await response.json();
        setTodos(data.todos);
      } catch (error) {
        setError('Error fetching todos');
        console.error('Error fetching todos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <CreateTodo setTodos={setTodos} />
      {loading ? (
        <p>Loading...</p>
      ) : error ? (
        <p>{error}</p>
      ) : (
        <Todos todos={todos} setTodos={setTodos} />
      )}
    </div>
  );
}

export default App;
