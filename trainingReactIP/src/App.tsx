
import './App.css'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import {Dashboard } from "./components/Dashboard"
function App() {



  return (
    <>

<BrowserRouter>
<Routes>
  

<Route path ="/project" element={<Dashboard></Dashboard>}></Route>
  </Routes></BrowserRouter>
    </>
        
  )
}

export default App


