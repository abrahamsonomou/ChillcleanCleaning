from main.models import *

# Create your models here.
class Temoignage(BaseModel):
    nom=models.CharField(max_length=200)
    contenu=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to='Temoignage',blank=True,null=True)
    statut=models.BooleanField(default=False,verbose_name="Statut")
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Temoignage'
        verbose_name_plural = 'Temoignages'
    
    def __str__(self) -> str:
        return self.nom
