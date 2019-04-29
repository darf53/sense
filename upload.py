import temp
import humi
import json
import urllib.request
import boto3

def UploadCloudWatch(metric,value):
    
    cloudwatch = boto3.client('cloudwatch', region_name='eu-west-1')
    
    response = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': metric,
                'Value': value
            }
        ],
        Namespace = 'Weather'
    )
    
# Uploading local temperature value
UploadCloudWatch("TemperatureIn",temp.temp("c"))

# Uploading local humidity value
UploadCloudWatch("HumidityIn",humi.humidityIn())
