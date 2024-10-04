// const express = require('express');
// const bodyParser = require('body-parser');

// const app = express();
// const PORT = 3000;

// // Middleware
// app.use(bodyParser.json());

// let employees = []; // In-memory employee storage

// // Routes

// // Get all employees
// app.get('/employees', (req, res) => {
//     res.json(employees);
// });

// // Add a new employee
// app.post('/employees', (req, res) => {
//     const newEmployee = {
//         id: employees.length + 1,
//         name: req.body.name,
//         position: req.body.position,
//         department: req.body.department,
//     };
//     employees.push(newEmployee);
//     res.status(201).json(newEmployee);
// });

// // Delete an employee by id
// app.delete('/employees/:id', (req, res) => {
//     const employeeId = parseInt(req.params.id);
//     employees = employees.filter(emp => emp.id !== employeeId);
//     res.status(204).send();
// });

// // Start the server
// app.listen(PORT, () => {
//     console.log(`Server is running on http://localhost:${PORT}`);
// });













mongodb+srv://hackathonmj641:1029384756@cluster0.bomrqhm.mongodb.net/