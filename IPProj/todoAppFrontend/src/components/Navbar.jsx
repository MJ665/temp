import { Link } from 'react-router-dom';

// Example logo import (replace with your actual logo path)
import Logo from '../assets/logo.jpeg';

export function Navbar() {
  return (
    <nav className="bg-blue-400 border   rounded-3xl p-4 shadow-md">
      <div className="container mx-auto flex justify-center  items-center">


          <img src={Logo} alt="Logo" className="h-28 mr-4" />
          <span className="text-white  font-serif text-4xl font-bold">Task Prioritizer</span>
      </div>
    </nav>
  );
}
