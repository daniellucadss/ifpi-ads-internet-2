// src/pages/AddEdit.tsx
import React, { useContext, useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { DataContext } from '../context/DataContext';
import Form from '../components/Form';

const AddEdit: React.FC = () => {
  const { addItem, updateItem, data } = useContext(DataContext);
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [defaultValues, setDefaultValues] = useState<{ name: string } | undefined>(undefined);

  useEffect(() => {
    if (id) {
      const item = data.find(item => item.id === parseInt(id));
      if (item) {
        setDefaultValues({ name: item.name });
      }
    }
  }, [id, data]);

  const handleSubmit = (data: { name: string }) => {
    if (id) {
      updateItem(parseInt(id), data);
    } else {
      addItem(data);
    }
    navigate('/');
  };

  return (
    <div>
      <h1>{id ? 'Edit' : 'Add'}</h1>
      <Form onSubmit={handleSubmit} defaultValues={defaultValues} />
    </div>
  );
};

export default AddEdit;
