from django.db import models
from datetime import datetime
from PIL import Image
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

def upload_to(instance,filename):
    return 'posts/{filename}'.format(filename=filename)

def upload_logo_to(instance,filename):
    return 'icons/{filename}'.format(filename=filename)

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d")

# Create your models here.

class League(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Teams(models.Model):
    id=models.AutoField(primary_key=True)
    logo=models.ImageField(upload_to=upload_logo_to)
    name=models.CharField(max_length=20)
    score=models.IntegerField()
    goals_scored=models.IntegerField()
    goals_lost=models.IntegerField()
    leag=models.ForeignKey(League,on_delete=models.DO_NOTHING)


    def image_tag(self):
       return mark_safe(f'<img src="{self.logo.url}" width="70" height="70" />' )

    def __str__(self):
        return self.name


class Plays(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(null=True)
    name1=models.ForeignKey(Teams,on_delete=models.DO_NOTHING,related_name="name1")
    name2=models.ForeignKey(Teams,on_delete=models.DO_NOTHING,related_name="name2")
    score1=models.IntegerField()
    score2=models.IntegerField()

    leag=models.ForeignKey(League,on_delete=models.DO_NOTHING)

    def save(self,*args,**kwargs):

        super().save()

        team1=Teams.objects.filter(name=self.name1).first()
        team2=Teams.objects.filter(name=self.name2).first()

        team1.goals_scored+=self.score1
        team1.goals_lost+=self.score2
       

        team2.goals_scored+=self.score2
        team2.goals_lost+=self.score1
        
        if self.score1>self.score2:
            team1.score+=3
        elif self.score1==self.score2:
            team1.score+=1
            team2.score+=1
        else:
            team2.score+=3

        team1.save()
        team2.save()

        self.date=get_current_time()
        

        return super(Plays,self).save(*args,**kwargs)
    
    def __str__(self):
        return f"{self.name1} vs {self.name2} on {self.date}"





class News(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField()
    image=models.ImageField(upload_to=upload_to)
    text=models.TextField()
    date=models.DateField(null=True)
    
   
    def image_tag(self):
       print("this is imaage url "+ self.image.url)
       return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />' )


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


  


        
