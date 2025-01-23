// src/components/List.tsx
import React, { useContext, useEffect } from 'react';
import { DataContext } from '../context/DataContext';
import { Link } from 'react-router-dom';

const List: React.FC = () => {
  const { data, deleteItem } = useContext(DataContext);

  return (
    <div>
      {data.map(item => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <Link to={`/edit/${item.id}`}>Edit</Link>
          <button onClick={() => deleteItem(item.id)}>Deletar</button>
        </div>
      ))}
    </div>
  );
};

export default List;
