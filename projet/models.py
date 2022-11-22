from main.models import *

class ProjetCategorie(BaseModel):
    nom_categorie=models.CharField(max_length=100,verbose_name='Libelle')
    slug=models.SlugField(max_length=200,verbose_name='Slug')

    class Meta:
        verbose_name="Categorie des Projets"

    def __str__(self) -> str:
        return self.nom_categorie
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.nom_categorie)
        
        super().save(*args,**kwargs)

class Projet(BaseModel):
    titre=models.CharField(max_length=100)
    client=models.CharField(blank=True,null=True,max_length=100)
    location=models.CharField(blank=True,null=True,max_length=100)
    surface=models.CharField(blank=True,null=True,max_length=100)
    annee=models.CharField(blank=True,null=True,max_length=100)
    value=models.CharField(blank=True,null=True,max_length=100)
    architect=models.CharField(blank=True,null=True,max_length=100)
    description=QuillField(blank=True,null=True,max_length=200)
    image=models.ImageField(upload_to='Projets_images',blank=True,null=True)
    image1=models.ImageField(upload_to='Projets_images',blank=True,null=True)
    image2=models.ImageField(upload_to='Projets_images',blank=True,null=True)
    image3=models.ImageField(upload_to='Projets_images',blank=True,null=True)
    image4=models.ImageField(upload_to='Projets_images',blank=True,null=True)
    categorie=models.ForeignKey(ProjetCategorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_cProjetategorie')
    statut=models.BooleanField(default=False,verbose_name="Status")

    class Meta:
        ordering=['-updated']
        verbose_name="Projet"

    def __str__(self) -> str:
        return self.titre
