import { Request, Response } from "express";
import { container, injectable, inject } from "tsyringe";
import { CreateParticipantUseCase } from "../../application/use-cases/create-participant.usecase";
import { ParticipantRepository } from "../../domain/repositories/participant.repository";

@injectable()
class ParticipantsController {
    constructor(
        private createParticipantUseCase: CreateParticipantUseCase,
        @inject("ParticipantRepository") private participantRepo: ParticipantRepository
    ) {}

    public create = async (req: Request, res: Response) => {
        const { name } = req.body;
        const participant = await this.createParticipantUseCase.execute({ name });
        res.status(201).json(participant);
    };

    public list = async (req: Request, res: Response) => {
        // res.status(200).json(await this.participantRepo.list());
        const participants = await this.participantRepo.list();
        res.status(200).json(participants);

    }
}

export default container.resolve(ParticipantsController);
