const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const User = require('./models/User');
const Task = require('./models/Task');

const app = express();

app.use(bodyParser.json());
app.use(cors({
    origin: 'http://127.0.0.1:5500',
    optionsSuccessStatus: 200
}));

mongoose.connect('mongodb+srv://hackathonmj641:1029384756@cluster0.bomrqhm.mongodb.net/myDatabase112');

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
    console.log('Connected to MongoDB');
});

// User authentication routes
app.post('/createUser', async (req, res) => {
    const { username, password } = req.body;
    const user = new User({ username, password });
    await user.save();
    res.json({ message: 'User created' });
});

app.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username, password });
    if (user) {
        res.json({ message: 'Login successful', userId: user._id });
    } else {
        res.status(401).json({ message: 'Invalid credentials' });
    }
});

// Task management routes
app.get('/tasks/:userId', async (req, res) => {
    const { userId } = req.params;
    const tasks = await Task.find({ userId });
    res.json(tasks);
});

app.post('/tasks', async (req, res) => {
    const { userId, title, priority, dueDate } = req.body;
    const task = new Task({ userId, title, priority, dueDate });
    await task.save();
    res.json({ message: 'Task added' });
});

app.put('/tasks/:id', async (req, res) => {
    const { id } = req.params;
    const { title, priority, dueDate } = req.body;
    await Task.findByIdAndUpdate(id, { title, priority, dueDate });
    res.json({ message: 'Task updated' });
});

app.delete('/tasks/:id', async (req, res) => {
    const { id } = req.params;
    await Task.findByIdAndDelete(id);
    res.json({ message: 'Task deleted' });
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
