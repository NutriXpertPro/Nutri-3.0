from django.core.management.base import BaseCommand
from diets.models import AlimentoTACO

class Command(BaseCommand):
    help = 'Importa dados da Tabela TACO para o banco de dados'

    def handle(self, *args, **options):
        # Dados TACO básicos para demonstração
        alimentos = [
            {
                'codigo': '001',
                'nome': 'Arroz branco cozido',
                'energia_kcal': 128,
                'proteina_g': 2.5,
                'lipidios_g': 0.1,
                'carboidrato_g': 26.2,
                'fibra_g': 1.6,
                'sodio_mg': 1,
                'grupo': 'Cereais'
            },
            {
                'codigo': '002',
                'nome': 'Feijão preto cozido',
                'energia_kcal': 77,
                'proteina_g': 4.5,
                'lipidios_g': 0.5,
                'carboidrato_g': 14.0,
                'fibra_g': 8.4,
                'sodio_mg': 2,
                'grupo': 'Leguminosas'
            },
            {
                'codigo': '003',
                'nome': 'Frango grelhado sem pele',
                'energia_kcal': 195,
                'proteina_g': 32.8,
                'lipidios_g': 6.2,
                'carboidrato_g': 0,
                'fibra_g': 0,
                'sodio_mg': 74,
                'grupo': 'Carnes'
            },
            {
                'codigo': '004',
                'nome': 'Ovo de galinha inteiro',
                'energia_kcal': 155,
                'proteina_g': 13.0,
                'lipidios_g': 10.6,
                'carboidrato_g': 1.6,
                'fibra_g': 0,
                'sodio_mg': 142,
                'grupo': 'Ovos'
            },
            {
                'codigo': '005',
                'nome': 'Banana nanica',
                'energia_kcal': 87,
                'proteina_g': 1.3,
                'lipidios_g': 0.1,
                'carboidrato_g': 22.8,
                'fibra_g': 2.0,
                'sodio_mg': 2,
                'grupo': 'Frutas'
            },
            {
                'codigo': '006',
                'nome': 'Batata doce cozida',
                'energia_kcal': 77,
                'proteina_g': 0.6,
                'lipidios_g': 0.1,
                'carboidrato_g': 18.4,
                'fibra_g': 2.2,
                'sodio_mg': 4,
                'grupo': 'Tubérculos'
            },
            {
                'codigo': '007',
                'nome': 'Aveia em flocos',
                'energia_kcal': 394,
                'proteina_g': 13.9,
                'lipidios_g': 8.5,
                'carboidrato_g': 67.0,
                'fibra_g': 9.1,
                'sodio_mg': 5,
                'grupo': 'Cereais'
            },
            {
                'codigo': '008',
                'nome': 'Leite desnatado',
                'energia_kcal': 35,
                'proteina_g': 3.4,
                'lipidios_g': 0.1,
                'carboidrato_g': 4.9,
                'fibra_g': 0,
                'sodio_mg': 44,
                'grupo': 'Lácteos'
            },
            {
                'codigo': '009',
                'nome': 'Pão de forma integral',
                'energia_kcal': 253,
                'proteina_g': 11.0,
                'lipidios_g': 4.8,
                'carboidrato_g': 43.0,
                'fibra_g': 6.9,
                'sodio_mg': 489,
                'grupo': 'Cereais'
            },
            {
                'codigo': '010',
                'nome': 'Brócolis cozido',
                'energia_kcal': 25,
                'proteina_g': 3.6,
                'lipidios_g': 0.4,
                'carboidrato_g': 4.0,
                'fibra_g': 3.4,
                'sodio_mg': 8,
                'grupo': 'Hortaliças'
            }
        ]
        
        importados = 0
        atualizados = 0
        
        for alimento_data in alimentos:
            alimento, created = AlimentoTACO.objects.get_or_create(
                codigo=alimento_data['codigo'],
                defaults=alimento_data
            )
            
            if created:
                importados += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Importado: {alimento.nome}')
                )
            else:
                # Atualizar dados existentes
                for key, value in alimento_data.items():
                    setattr(alimento, key, value)
                alimento.save()
                atualizados += 1
                self.stdout.write(
                    self.style.WARNING(f'Atualizado: {alimento.nome}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nImportação concluída! {importados} novos alimentos importados, {atualizados} atualizados.'
            )
        )