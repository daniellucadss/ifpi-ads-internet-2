import { Request, Response } from "express";
import { container, injectable, inject } from "tsyringe";
import { GroupRepository } from "../../domain/repositories/group.repository";
import { Group } from "../../domain/entities/group.entity";
import { ParticipantRepository } from "../../domain/repositories/participant.repository";
import { Participant } from "../../domain/entities/participant.entity";

@injectable()
class GroupsController {
    constructor(
        @inject("GroupRepository") private groupRepo: GroupRepository,
        @inject("ParticipantRepository") private participantRepo: ParticipantRepository
    ) {}
    public async list(req: Request, res: Response) {
        const groups = await this.groupRepo.list();
        res.status(200).json({ groups });
    }

    public async create(req: Request, res: Response){
        const { name, participants } = req.body;
        const group = new Group(name);
        const createdGroup = await this.groupRepo.create(group);

        res.status(201).json(createdGroup);
    }
}

export default container.resolve(GroupsController);