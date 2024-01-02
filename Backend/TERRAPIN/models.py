from django.db import models

class IPGeolocation(models.Model):
    ip = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country_code = models.CharField(max_length=200)
    country_name = models.CharField(max_length=200)
    region_code = models.CharField(max_length=200)
    region_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, null=True, blank=True)
    zip = models.CharField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.ip
    
class SecurityInfo(models.Model):
    is_proxy = models.BooleanField()
    proxy_type = models.CharField(max_length=200, null=True, blank=True)
    is_crawler = models.BooleanField()
    crawler_name = models.CharField(max_length=200, null=True, blank=True)
    crawler_type = models.CharField(max_length=200, null=True, blank=True)
    is_tor = models.BooleanField()
    threat_level = models.CharField(max_length=200)
    threat_types = models.CharField(max_length=200, null=True, blank=True)
    
class Connection(models.Model):
    asn = models.CharField(max_length = 200)
    isp = models.CharField(max_length = 500)
    
class TimeZone(models.Model):
    current_time = models.CharField(max_length = 200 )
    gmt_offset = models.IntegerField()
    code = models.CharField(max_length = 200 )
    is_daylight_saving = models.BooleanField()