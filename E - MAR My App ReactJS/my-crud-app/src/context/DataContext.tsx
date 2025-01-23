// src/context/DataContext.tsx
import React, { createContext, ReactNode, useEffect, useState } from 'react';
import axios from 'axios';

interface Item {
  id: number;
  name: string;
}

interface DataContextType {
  data: Item[];
  addItem: (item: { name: string }) => void;
  updateItem: (id: number, item: { name: string }) => void;
  deleteItem: (id: number) => void;
}

export const DataContext = createContext<DataContextType>({} as DataContextType);

const DataProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [data, setData] = useState<Item[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://localhost:5000/api/tasks');
      setData(response.data);
    };

    fetchData();
  }, []);

  const addItem = async (item: { name: string }) => {
    const response = await axios.post('http://localhost:5000/api/tasks', item);
    setData([...data, response.data]);
  };

  const updateItem = async (id: number, item: { name: string }) => {
    const response = await axios.put(`http://localhost:5000/api/tasks/${id}`, item);
    setData(data.map(task => (task.id === id ? response.data : task)));
  };

  const deleteItem = async (id: number) => {
    await axios.delete(`http://localhost:5000/api/tasks/${id}`);
    setData(data.filter(task => task.id !== id));
  };

  return (
    <DataContext.Provider value={{ data, addItem, updateItem, deleteItem }}>
      {children}
    </DataContext.Provider>
  );
};

export default DataProvider;
