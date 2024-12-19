import { MigrationInterface, QueryRunner } from "typeorm";

export class AddParticipantEntity1734619640387 implements MigrationInterface {
    name = 'AddParticipantEntity1734619640387'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "group" ("id" SERIAL NOT NULL, "name" character varying NOT NULL, CONSTRAINT "PK_256aa0fda9b1de1a73ee0b7106b" PRIMARY KEY ("id"))`);
        await queryRunner.query(`CREATE TABLE "participant" ("id" SERIAL NOT NULL, "name" character varying NOT NULL, "groupId" integer, CONSTRAINT "PK_64da4237f502041781ca15d4c41" PRIMARY KEY ("id"))`);
        await queryRunner.query(`ALTER TABLE "participant" ADD CONSTRAINT "FK_dc56154aca4ec8aaaa49e7f6f61" FOREIGN KEY ("groupId") REFERENCES "group"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "participant" DROP CONSTRAINT "FK_dc56154aca4ec8aaaa49e7f6f61"`);
        await queryRunner.query(`DROP TABLE "participant"`);
        await queryRunner.query(`DROP TABLE "group"`);
    }

}
