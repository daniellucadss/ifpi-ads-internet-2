import { MyGQLContext } from "./context-graphql";
import { Montadora } from "./montadora.entity";
import { Veiculo } from "./veiculo.entity";

export const resolvers = {
  Query: {
    // montadoras: () => Montadora.find()
    montadoras: async (_: any, __: any, context: MyGQLContext) => {
      console.log(`User: ${context.user}`);
      return await Montadora.find({ relations: ['veiculos'] });
    },
    veiculos: async () => {
      return await Veiculo.find({ relations: ['montadora'] });
    },
    veiculo: async (_: any, { id }: { id: string }) => {
      return await Veiculo.findOne({ 
        where: { id: parseInt(id) },
        relations: ['montadora']
      });
    }
  },
  Mutation: {
    criarMontadora: async (_: any, { nome }: { nome: string }) => {
      try {
        const montadora = Montadora.create({ nome });
        await montadora.save();
        return montadora;
      } catch (error) {
        throw new Error(`Erro ao criar montadora: ${(error as any).message}`);
      }
    },
    criarVeiculo: async (_: any, { modelo, ano, montadoraId }: { modelo: string, ano: number, montadoraId: string }) => {
      try {
        const montadora = await Montadora.findOne({ 
          where: { id: parseInt(montadoraId) }
        });
        
        if (!montadora) {
          throw new Error('Montadora não encontrada');
        }

        const veiculo = Veiculo.create({
          modelo,
          ano,
          montadora
        });

        await veiculo.save();
        return veiculo;
      } catch (error: any) {
        throw new Error(`Erro ao criar veículo: ${error.message}`);
      }
    },
    removerMontadora: async (_: any, { id }: { id: string }) => {
      try {
        const montadora = await Montadora.findOne({ 
          where: { id: parseInt(id) }
        });
        
        if (!montadora) {
          return false;
        }

        await montadora.remove();
        return true;
      } catch (error: any) {
        throw new Error(`Erro ao remover montadora: ${error.message}`);
      }
    },
    removerVeiculo: async (_: any, { id }: { id: string }) => {
      try {
        const veiculo = await Veiculo.findOne({ 
          where: { id: parseInt(id) }
        });
        
        if (!veiculo) {
          return false;
        }

        await veiculo.remove();
        return true;
      } catch (error: any) {
        throw new Error(`Erro ao remover veículo: ${error.message}`);
      }
    },
  },
  Montadora: {
    veiculos: async (montadora: Montadora) => {
      const montadoraCompleta = await Montadora.findOne({
        where: { id: montadora.id },
        relations: ['veiculos']
      });
      return montadoraCompleta ? montadoraCompleta.veiculos : [];
    }
  },
  Veiculo: {
    montadora: async (veiculo: Veiculo) => {
      const veiculoCompleto = await Veiculo.findOne({
        where: { id: veiculo.id },
        relations: ['montadora']
      });
      return veiculoCompleto ? veiculoCompleto.montadora : null;
    }
  }
};