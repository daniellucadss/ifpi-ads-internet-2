import { container, inject, injectable } from "tsyringe";
import { Participant } from "../../domain/entities/participant.entity";
import { ParticipantRepository } from "../../domain/repositories/participant.repository";

interface CreateParticipantRequest {
    name: string;
}

@injectable()
export class CreateParticipantUseCase {
    constructor(
        @inject("ParticipantRepository") private participantRepo: ParticipantRepository
    ) {}

    async execute({
        name,
      }: CreateParticipantRequest): Promise<Participant> {
        const ParticipantCreated = await this.participantRepo.create(
          new Participant(name)
        );
    
        return ParticipantCreated;
    }
}

export default container.resolve(CreateParticipantUseCase);