from rest_framework.views import APIView
from rest_framework.response import Response
from Backend.TERRAPIN.serializers import IPGeolocationSerializer
from .models import IPGeolocation, SecurityInfo, Connection, TimeZone
import requests

class GeolocationView(APIView):
    def get(self, request, ip, format=None):
        try:
            geolocation = IPGeolocation.objects.get(ip=ip)
        except IPGeolocation.DoesNotExist:
            response = requests.get(f'httpS://api.ipstack.com/{ip}?access_key=YOUR_ACCESS_KEY')
            geodata = response.json()

            security_info = SecurityInfo.objects.create(
                is_proxy=geodata['security']['is_proxy'],
                proxy_type = geodata['security']['proxy_type'],
                is_crawler = geodata['security']['is_crawler'],
                crawler_name = geodata['security']['crawler_name'],
                is_tor = geodata['security']['is_tor'],
                threat_level = geodata['security']['threat_level'],
                threat_types = geodata['security']['threat_types']
            )

            connection = Connection.objects.create(
                asn = geodata['connection']['asn'],
                isp = geodata['connection']['isp']
            )
            
            timezone = TimeZone.objects.create(
                current_time = geodata['timezone']['current_time'],
                gmt_offset = geodata['timezone']['gmt_offset'],
                code = geodata['timezone']['code'],
                is_daylight_saving = geodata['timezone']['is_daylight_saving']
            ) 
            
            geolocation = IPGeolocation.objects.create(
                ip=ip,
                hostname=geodata['hostname'],
                type=geodata['type'],
                latitude=geodata['latitude'],
                longitude=geodata['longitude'],
                country_code=geodata['country_code'],
                country_name=geodata['country_name'],
                region_code=geodata['region_code'],
                region_name=geodata['region_name'],
                city=geodata['city'],
                zip=geodata['zip'],
                security_info=security_info,
                connection=connection,
                timezone=timezone
            )
                

        geolocation_serializer = IPGeolocationSerializer(geolocation)
        return Response(geolocation_serializer.data)