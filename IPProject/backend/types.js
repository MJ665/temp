const zod = require("zod");

const createTodo = zod.object({
    title: zod.string(),
    description: zod.string(),
    completed: zod.boolean(),
    priority: zod.enum(['low', 'medium', 'high']).default('low') // Add priority field
});

const updateTodo = zod.object({
    id: zod.string(),
    title: zod.string().optional(),
    description: zod.string().optional(),
    completed: zod.boolean().optional(),
    priority: zod.enum(['low', 'medium', 'high']).optional() // Add priority field
});

module.exports = {
    createTodo,
    updateTodo,
};
