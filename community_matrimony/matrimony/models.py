from django.db import models

# Create your models here.



class States(models.Model):
    # table to store state names
    state_name = models.CharField(max_length= 60)

    def __str__(self):
        return self.state_name

class District(models.Model):
    district_name= models.CharField(max_length=50)
    district_state=models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name


class Kula_osa(models.Model):

    #table to store kula/osa names
    kula_name = models.CharField(max_length= 60)
    kula_in_states = models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.kula_name


class Appuser(models.Model):

    # user registration details.
    user_type= models.CharField(max_length= 30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    mobile_no=models.CharField(max_length=10)
    state=models.ForeignKey('States', on_delete=models.CASCADE)
    district = models.ForeignKey('District', on_delete=models.CASCADE)
    city=models.CharField(max_length=40)
    kula_osa=models.ForeignKey('Kula_osa', on_delete=models.CASCADE) 
    address=models.CharField(max_length=100) 
    created_date_time = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.mobile_no


def user_directory_path(instance, filename): 

	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
	return 'user_{0}/{1}'.format(instance.user.id, filename) 



class groom_bride_details(models.Model):
    
    # table to store groom/bride details.
    name = models.CharField(max_length= 40)
    DOB = models.DateField()
    height = models.FloatField()
    occupation= models.CharField(max_length= 40)
    Father_name = models.CharField(max_length=40)
    mother_name = models.CharField( max_length=40)
    profile_pic = models.ImageField(upload_to = user_directory_path)
    created_date_time = models.DateTimeField(auto_now_add=True) 
    appuser = models.ForeignKey('Appuser', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



