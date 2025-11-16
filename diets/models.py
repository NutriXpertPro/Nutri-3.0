from django.db import models
from patients.models import PatientProfile

# Create your models here.


class AlimentoTACO(models.Model):
    """Modelo para armazenar dados da Tabela TACO de Composição de Alimentos"""
    codigo = models.CharField(max_length=10, unique=True, help_text="Código do alimento na TACO")
    nome = models.CharField(max_length=200, help_text="Nome do alimento")
    
    # Composição nutricional por 100g
    energia_kcal = models.FloatField(help_text="Energia em kcal por 100g")
    proteina_g = models.FloatField(help_text="Proteína em gramas por 100g")
    lipidios_g = models.FloatField(help_text="Lipídios em gramas por 100g")
    carboidrato_g = models.FloatField(help_text="Carboidrato em gramas por 100g")
    fibra_g = models.FloatField(default=0, help_text="Fibra em gramas por 100g")
    
    # Minerais
    calcio_mg = models.FloatField(null=True, blank=True, help_text="Cálcio em mg por 100g")
    ferro_mg = models.FloatField(null=True, blank=True, help_text="Ferro em mg por 100g")
    sodio_mg = models.FloatField(null=True, blank=True, help_text="Sódio em mg por 100g")
    
    # Vitaminas
    vitamina_c_mg = models.FloatField(null=True, blank=True, help_text="Vitamina C em mg por 100g")
    
    # Categorização
    grupo = models.CharField(max_length=50, help_text="Grupo alimentar (ex: Cereais, Carnes, etc.)")
    
    # Unidades de medida mais comuns
    unidade_caseira = models.CharField(max_length=50, null=True, blank=True, help_text="Unidade caseira (ex: 1 xícara, 1 fatia)")
    peso_unidade_caseira_g = models.FloatField(null=True, blank=True, help_text="Peso em gramas da unidade caseira")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Alimento TACO"
        verbose_name_plural = "Alimentos TACO"
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['grupo']),
        ]
    
    def __str__(self):
        return self.nome
    
    @property
    def calorias(self):
        """Alias para energia_kcal para compatibilidade"""
        return self.energia_kcal
    
    @property
    def carboidratos(self):
        """Alias para carboidrato_g para compatibilidade"""
        return self.carboidrato_g
    
    @property
    def proteinas(self):
        """Alias para proteina_g para compatibilidade"""
        return self.proteina_g
    
    @property
    def gorduras(self):
        """Alias para lipidios_g para compatibilidade"""
        return self.lipidios_g


class Diet(models.Model):
    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name="diets",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=255)
    meals = models.JSONField()
    substitutions = models.JSONField(null=True, blank=True)
    
    # Metas nutricionais
    meta_calorias = models.PositiveIntegerField(null=True, blank=True, help_text="Meta de calorias diárias")
    meta_carboidratos = models.PositiveIntegerField(null=True, blank=True, help_text="Meta de carboidratos em gramas")
    meta_proteinas = models.PositiveIntegerField(null=True, blank=True, help_text="Meta de proteínas em gramas")
    meta_gorduras = models.PositiveIntegerField(null=True, blank=True, help_text="Meta de gorduras em gramas")
    
    # TMB e GCDT calculados
    tmb_calculado = models.PositiveIntegerField(null=True, blank=True, help_text="Taxa Metabólica Basal calculada")
    gcdt_calculado = models.PositiveIntegerField(null=True, blank=True, help_text="Gasto Calórico Diário Total calculado")
    
    # Configurações utilizadas no cálculo
    formula_tmb = models.CharField(
        max_length=20, 
        choices=[
            ('harris-benedict', 'Harris-Benedict'),
            ('mifflin-st-jeor', 'Mifflin-St Jeor'),
            ('katch-mcardle', 'Katch-McArdle'),
        ],
        null=True, 
        blank=True
    )
    nivel_atividade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, help_text="Fator de atividade física")
    objetivo = models.CharField(
        max_length=10,
        choices=[
            ('manter', 'Manter peso'),
            ('perder', 'Perder peso'),
            ('ganhar', 'Ganhar peso'),
        ],
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Status do plano
    is_active = models.BooleanField(default=True, help_text="Se o plano está ativo")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Plano Alimentar"
        verbose_name_plural = "Planos Alimentares"

    def __str__(self):
        return f"{self.name} - {self.patient.user.name}"
    
    @property
    def total_refeicoes(self):
        """Retorna o número total de refeições configuradas"""
        return len(self.meals) if self.meals else 0
    
    @property
    def tem_substituicoes(self):
        """Verifica se há substituições configuradas"""
        return bool(self.substitutions and len(self.substitutions) > 0)
