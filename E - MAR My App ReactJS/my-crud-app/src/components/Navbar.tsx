// src/components/Navbar.tsx
import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const Navbar: React.FC = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6">Cadastro Genérico</Typography>
        <Button color="inherit" component={Link} to="/">Página Inicial</Button>
        <Button color="inherit" component={Link} to="/add">Adicionar</Button>
      </Toolbar>


    </AppBar>
  );
};

export default Navbar;
