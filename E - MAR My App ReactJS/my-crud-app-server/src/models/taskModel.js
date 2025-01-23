// src/models/taskModel.js
let tasks = [];
let idCounter = 1;

const getTasks = () => {
  return tasks;
};

const getTaskById = (id) => {
  return tasks.find(task => task.id === id);
};

const addTask = (task) => {
  task.id = idCounter++;
  tasks.push(task);
  return task;
};

const updateTask = (id, updatedTask) => {
  const index = tasks.findIndex(task => task.id === id);
  if (index !== -1) {
    tasks[index] = { ...tasks[index], ...updatedTask };
    return tasks[index];
  }
  return null;
};

const deleteTask = (id) => {
  const index = tasks.findIndex(task => task.id === id);
  if (index !== -1) {
    const [deletedTask] = tasks.splice(index, 1);
    return deletedTask;
  }
  return null;
};

module.exports = {
  getTasks,
  getTaskById,
  addTask,
  updateTask,
  deleteTask,
};
