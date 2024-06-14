const mongoose = require('mongoose');

const taskSchema = new mongoose.Schema({
    userId: { type: mongoose.Schema.Types.ObjectId, required: true, ref: 'User' },
    title: { type: String, required: true },
    priority: { type: String, required: true },
    createdDate: { type: Date, default: Date.now },
    dueDate: { type: Date, required: true }
});

module.exports = mongoose.model('Task', taskSchema);
