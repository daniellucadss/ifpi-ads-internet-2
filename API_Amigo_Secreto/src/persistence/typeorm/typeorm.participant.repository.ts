import { Repository } from "typeorm";
import { AppDataSource } from "../../data-source";
import { Participant } from "../../domain/entities/participant.entity";
import { ParticipantRepository } from "../../domain/repositories/participant.repository";

export class TypeORMParticipantRepository implements ParticipantRepository {
    private repository: Repository<Participant>;

    constructor() {
        this.repository = AppDataSource.getRepository(Participant);
    }

    async create(entity: Participant): Promise<Participant> {
        return await this.repository.save(entity);
    }

    async list(): Promise<Participant[]> {
        return await this.repository.find();
    }
}



