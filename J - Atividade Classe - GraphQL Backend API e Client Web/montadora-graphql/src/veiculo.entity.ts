import { BaseEntity, Column, Entity, ManyToOne, PrimaryGeneratedColumn } from "typeorm";
import { Montadora } from "./montadora.entity";

@Entity()
export class Veiculo extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: number

    @Column()
    modelo: string

    @Column()
    ano: number

    @ManyToOne(() => Montadora, montadora => montadora.veiculos)
    montadora: Montadora
} 