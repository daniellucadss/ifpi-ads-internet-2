import { Participant } from "./participant.entity";

export class Match {
    id: number;
    giverId: Participant;
    receiverId: Participant;

    constructor(id: number, giverId: Participant, receiverId: Participant) {
        this.id = id;
        this.giverId = giverId;
        this.receiverId = receiverId;
    }
}