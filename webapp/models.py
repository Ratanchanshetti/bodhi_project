from django.db import models
#model --class name 
#charfield is function--data type
class carousel(models.Model):
    heading=models.CharField(max_length=50,null=True)
    description=models.TextField(max_length=200,null=True)
    img=models.ImageField(upload_to='img/carousel',null=True)
    #submitted time date and updated time date is saved by these two 
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'carousel'

class functionality(models.Model):
    main_heading=models.CharField(max_length=50,null=True)
    Title=models.CharField(max_length=50,null=True)
    content=models.TextField(max_length=200,null=True)
    gif=models.ImageField(upload_to='img/functionality',null=True)
    #submitted time date and updated time date is saved by these two 
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'functionality'

class cleints(models.Model):
    c_title=models.CharField(max_length=50,null=True)
    c_img=models.ImageField(upload_to='img/cleints',null=True)
    #submitted time date and updated time date is saved by these two 
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'cleints'

class About_us(models.Model):
    A_title=models.CharField(max_length=50,null=True)
    A_description=models.TextField(max_length=200,null=True)
    Aa_description=models.TextField(max_length=200,null=True)
    Ab_description=models.TextField(max_length=200,null=True)
    A_img=models.ImageField(upload_to='img/About_us',null=True)
    #submitted time date and updated time date is saved by these two 
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:'About_us'
        #this is for the display on the django -admin titel function
    def __str__(self):
        return self.A_title


    

# Create your models here.
