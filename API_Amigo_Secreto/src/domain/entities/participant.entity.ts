import {Entity, PrimaryGeneratedColumn, Column, ManyToOne } from "typeorm";
import { Group } from './group.entity';

@Entity()
export class Participant {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column({ nullable: false })
    name: string;

    @ManyToOne(() => Group, group => group.participants)
    group!: Group;

    constructor(name: string) {
        this.name = name;
    }
}