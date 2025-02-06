import { MigrationInterface, QueryRunner } from "typeorm";

export class AddVeiculo1738872304285 implements MigrationInterface {
    name = 'AddVeiculo1738872304285'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "veiculo" ("id" SERIAL NOT NULL, "modelo" character varying NOT NULL, "ano" integer NOT NULL, "montadoraId" integer, CONSTRAINT "PK_0fcc9d29b16ed347447f8f9356e" PRIMARY KEY ("id"))`);
        await queryRunner.query(`ALTER TABLE "veiculo" ADD CONSTRAINT "FK_3a1d0867cce4073f4cf073ae59d" FOREIGN KEY ("montadoraId") REFERENCES "montadora"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "veiculo" DROP CONSTRAINT "FK_3a1d0867cce4073f4cf073ae59d"`);
        await queryRunner.query(`DROP TABLE "veiculo"`);
    }

}
