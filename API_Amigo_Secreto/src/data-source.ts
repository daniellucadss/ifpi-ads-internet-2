import "reflect-metadata";
import { DataSource } from "typeorm";
import { User } from "./domain/entities/user.entity";
import { Participant } from "./domain/entities/participant.entity";
import { Group } from "./domain/entities/group.entity";
import { Match } from "./domain/entities/match.entity";

export const AppDataSource = new DataSource({
  type: "postgres",
  host: process.env.DB_HOST,
  port: Number(process.env.DB_PORT),
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  synchronize: false,
  logging: true,
  entities: [User, Participant, Group, Match], 
  migrations: ["src/persistence/typeorm/migrations/**/*.ts"],
});

AppDataSource.initialize()
  .then(() => {
    console.log("DS inicializado com sucesso!");
  })
  .catch((err: unknown) => {
    console.log("Erro ao inicializar DS", err);
  });
