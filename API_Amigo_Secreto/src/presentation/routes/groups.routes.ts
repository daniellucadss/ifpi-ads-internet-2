import { Application } from "express";
import { CommonRoute } from "./common.route";
import GroupsController from "../controllers/groups.controller";

export class GroupsRoute extends CommonRoute {
    constructor(app: Application, suffix: string) {
        super(app, 'Groups Routes', suffix);
    }
    
    configureRoutes(): Application {
        this.app
            .route(this.suffix)
            .post(GroupsController.create)
        ;

        this.app.route(`${this.suffix}/:id`).get().put().delete().patch();

        return this.app;
    }
}