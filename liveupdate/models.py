from django.db import models
from django.contrib import admin

# Create your models here.
class Update(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return "[ %s ] %s " % (
            self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            self.text
        )



class ViewAllTypeFields(models.Model):
    aggregate_field = models.Aggregate()
    bigint_field = models.BigIntegerField()
    # auto_field = models.AutoField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=10)
    comma_separ_field = models.CommaSeparatedIntegerField(max_length=500)
    date_field = models.DateField(auto_now_add=True)
    datetime_field = models.DateTimeField(auto_now=False)
    decimal_field = models.DecimalField(max_digits=20, decimal_places=5)
    duration_field = models.DurationField()
    email_field = models.EmailField(max_length=254)
    # file_field = models.FileField(upload_to='file/%Y/%m/%d')
    # file_path_field = models.Model(path=None)
    float_field = models.FloatField()
    # image_field = models.ImageField(height_field=350, width_field=300)
    integer_field = models.IntegerField()
    ip_field = models.GenericIPAddressField(null=True)
    null_bool_field = models.NullBooleanField()
    positive_integer_field = models.PositiveIntegerField()
    slug = models.SlugField(max_length=50)
    text = models.TextField(max_length=100)
    time = models.TimeField(auto_now=True)
    url_field = models.URLField(max_length=200)
    # foreign_key_field = models.ForeignKey('Update')
    # many_to_many = models.ManyToManyField('self')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return str(self.text)
