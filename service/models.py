from main.models import *

# Create your models here.
class Service(BaseModel):
    titre=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    detail=QuillField(blank=True,null=True,max_length=200)
    image=models.ImageField(upload_to='services',blank=True,null=True)
    statut=models.BooleanField(default=False)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)