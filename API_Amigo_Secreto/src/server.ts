import 'reflect-metadata';
import "dotenv/config";
import "../src/common/ioc";
import express, { Request, Response } from 'express';
import { CommonRoute } from './presentation/routes/common.route';
import { ParticipantsRoute } from './presentation/routes/participants.route';
import { GroupsRoute } from './presentation/routes/groups.routes';

import { AppDataSource } from './data-source';

const app = express();

AppDataSource.initialize();

app.use(express.json());

app.get('/', (req: Request, res: Response) => {
    res.status(200).json({ message: 'API Amigo Oculto' });
});

const routes: CommonRoute[] = [];
routes.push(new ParticipantsRoute(app, '/participants')), 
routes.push(new GroupsRoute(app, '/groups'));

app.listen(3000, () => {
    for (let route of routes) {
        console.log(`Rotas configuradas: ${route.getName()}`);
    }

    console.log('Servidor online em 127.0.0.1:3000');
});