import { Entity, PrimaryGeneratedColumn, Column, OneToMany } from "typeorm";
import { Participant } from './participant.entity';

@Entity()
export class Group {
    @PrimaryGeneratedColumn()
    public id!: number;

    @Column()
    public name: string;

    @OneToMany(() => Participant, participant => participant.group)
    public participants!: Participant[];

    constructor(name: string) {
        this.name = name;
    }
}
