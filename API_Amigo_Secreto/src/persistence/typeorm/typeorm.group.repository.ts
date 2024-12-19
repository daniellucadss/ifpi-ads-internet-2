import { Repository } from "typeorm";
import { AppDataSource } from "../../data-source";
import { Group } from "../../domain/entities/group.entity";
import { GroupRepository } from "../../domain/repositories/group.repository";

export class TypeORMGroupRepository implements GroupRepository {
    private repository: Repository<Group>;

    constructor() {
        this.repository = AppDataSource.getRepository(Group);
    }

    async create(entity: Group): Promise<Group> {
        return await this.repository.save(entity);
    }

    async list(): Promise<Group[]> {
        return await this.repository.find();
    }
}



