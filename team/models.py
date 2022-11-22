from main.models import *
# Team    
class Team(BaseModel):
    nom=models.CharField(max_length=200,name="nom")
    email=models.EmailField(blank=True,null=True,max_length=200)
    fonction=models.CharField(blank=True,null=True,max_length=200,)
    detail=models.TextField(blank=True,null=True)
    photo=models.ImageField(upload_to='teams',blank=True,null=True)
    twitter=models.CharField(blank=True,null=True,max_length=200)
    facebook=models.CharField(blank=True,null=True,max_length=200)
    instagram=models.CharField(blank=True,null=True,max_length=200)
    linkdin=models.CharField(blank=True,null=True,max_length=200)
    youtube=models.CharField(blank=True,null=True,max_length=200)
    statut=models.BooleanField(default=False,verbose_name="Statut")

    class Meta:
        verbose_name="Team"

    def __str__(self) -> str:
        return self.nom
