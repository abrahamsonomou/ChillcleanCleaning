from main.models import *

# Create your models here.
# Contact
class Contact(BaseModel):
    nom=models.CharField(blank=True,null=True,max_length=100,name='nom',verbose_name='Nom')
    email=models.EmailField(blank=True,null=True,max_length=100,name='email',verbose_name='Email')
    sujet=models.CharField(blank=True,null=True,max_length=100,name='sujet',verbose_name='Sujet')
    message=models.TextField(blank=True,null=True,verbose_name='Message',name='message')
    
    class Meta:
        ordering=['-updated']
        verbose_name="Contact" 

    def __str__(self) -> str:
        return self.nom

class NewsLetter(BaseModel):
    email=models.EmailField(blank=True,null=True,max_length=100,verbose_name='Email',name='email')
    
    class Meta:
        verbose_name="NewsLetter"
        ordering=['-updated']

    def __str__(self) -> str:
        return self.email
        