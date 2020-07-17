from django.db import models

# Create your models here.


# table to store state names
class states(models.Model):
    state_name = models.CharField(max_length= 60)


#table to store kula/osa names
class kula_osa(models.Model):
    kula_name = models.CharField(max_length= 60)

# user registration details.
class Appuser(models.Model):

    user_type= models.CharField(max_length= 30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    kula_osa=models.CharField(max_length=40)
    mobile_no=models.CharField(max_length=10)
    occupation=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    created_date_time = models.DateTimeField(auto_now_add=True) 


def user_directory_path(instance, filename): 

	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
	return 'user_{0}/{1}'.format(instance.user.id, filename) 



class groom_bride_details(models.Model):
    name = models.CharField(max_length= 40)
    DOB = models.DateField()
    height = models.IntegerField()
    occupation= models.CharField(max_length= 40)
    Father_name = models.CharField(max_length=40)
    mother_name = models.CharField( max_length=40)
    profile_pic = models.ImageField(upload_to = user_directory_path)
    created_date_time = models.DateTimeField(auto_now_add=True) 
    appuser = models.ForeignKey('Appuser', on_delete=models.CASCADE)






