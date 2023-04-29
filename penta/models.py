from django.db import models
from datetime import datetime
from PIL import Image
from django.utils.safestring import mark_safe

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d")

# Create your models here.

class League(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)


class Teams(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    score=models.IntegerField()
    goals_scored=models.IntegerField()
    goals_lost=models.IntegerField()
    leag=models.ForeignKey(League,on_delete=models.DO_NOTHING)


   

class Plays(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(null=True)
    name1=models.CharField(max_length=25)
    name2=models.CharField(max_length=25)
    score1=models.IntegerField()
    score2=models.IntegerField()

    leag=models.ForeignKey(League,on_delete=models.DO_NOTHING)

    def save(self,*args,**kwargs):
        self.date=get_current_time()
        

        return super(Plays,self).save(*args,**kwargs)





class News(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField()
    image=models.ImageField(upload_to='pics')
    date=models.DateField(null=True)
    
   


    def save(self,*args,**kwargs):
        super().save()

        self.date=get_current_time()
        print("from")
        img = Image.open(self.image.path)
        print("here")
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        return super(News,self).save(*args,**kwargs)


    def image_tag(self):
       print("this is imaage url "+ self.image.url)
       return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />' )


        
