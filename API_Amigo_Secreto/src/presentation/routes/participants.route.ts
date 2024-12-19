import { Application } from "express";
import { CommonRoute } from "./common.route";
import ParticipantsController from "../controllers/participants.controller";

export class ParticipantsRoute extends CommonRoute {
    constructor(app: Application, suffix: string) {
        super(app, 'Participants Routes', suffix);
    }

    configureRoutes(): Application {
        this.app
            .route(this.suffix)
            .get(ParticipantsController.list)
            .post(ParticipantsController.create)
        ;

        this.app.route(`${this.suffix}/:id`).get().put().delete().patch();

        return this.app;
    }
}

