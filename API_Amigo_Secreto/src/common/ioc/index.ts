import { container } from "tsyringe";
import { ParticipantRepository } from "../../domain/repositories/participant.repository";
import { TypeORMParticipantRepository } from "../../persistence/typeorm/typeorm.participant.repository";
import { GroupRepository } from "../../domain/repositories/group.repository";
import { TypeORMGroupRepository } from "../../persistence/typeorm/typeorm.group.repository";

container.register<ParticipantRepository>("ParticipantRepository", TypeORMParticipantRepository);

container.register<GroupRepository>("GroupRepository", {
    useClass: TypeORMGroupRepository
});