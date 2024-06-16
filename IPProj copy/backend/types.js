const zod = require("zod");

const createTodo = zod.object({
    title: zod.string(),
    description: zod.string(),
    completed: zod.boolean(),
    priority: zod.enum(["low", "medium", "high"]).optional()
});

const updateTodo = zod.object({
    id: zod.string()
});

module.exports = {
    createTodo: createTodo,
    updateTodo: updateTodo
};
