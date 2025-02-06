import { BaseEntity, Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { Veiculo } from "./veiculo.entity";

@Entity()
export class Montadora extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: number

    @Column()
    nome: String

    @OneToMany(() => Veiculo, veiculo => veiculo.montadora)
    veiculos: Veiculo[]
}