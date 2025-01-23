// src/controllers/taskController.js
const taskModel = require('../models/taskModel');

const getTasks = (req, res) => {
  const tasks = taskModel.getTasks();
  res.json(tasks);
};

const getTaskById = (req, res) => {
  const task = taskModel.getTaskById(parseInt(req.params.id));
  if (task) {
    res.json(task);
  } else {
    res.status(404).json({ message: 'Task not found' });
  }
};

const addTask = (req, res) => {
  const newTask = taskModel.addTask(req.body);
  res.status(201).json(newTask);
};

const updateTask = (req, res) => {
  const updatedTask = taskModel.updateTask(parseInt(req.params.id), req.body);
  if (updatedTask) {
    res.json(updatedTask);
  } else {
    res.status(404).json({ message: 'Task not found' });
  }
};

const deleteTask = (req, res) => {
  const deletedTask = taskModel.deleteTask(parseInt(req.params.id));
  if (deletedTask) {
    res.json(deletedTask);
  } else {
    res.status(404).json({ message: 'Task not found' });
  }
};

module.exports = {
  getTasks,
  getTaskById,
  addTask,
  updateTask,
  deleteTask,
};
