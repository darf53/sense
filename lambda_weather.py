import json
import urllib.request
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    cloudwatch = boto3.client('cloudwatch', region_name='eu-west-1')
    
    body = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Gent,BE&APPID=XXXXXXXXXX')
    data = json.load(body)
    temp = round((data['main']['temp']-273.15),2)
    pressure = (data['main']['pressure'])
    humidity = (data['main']['humidity'])
    
    response = cloudwatch.put_metric_data(
        MetricData = [
            {
                'MetricName': 'TemperatureOut',
                'Dimensions': [
                    {
                        'Name': 'TemperatureOutside',
                        'Value': 'CoolService'
                    },
                    {
                        'Name': 'APP_VERSION',
                        'Value': '1.0'
                    },
                ],
                'Unit': 'None',
                'Value': temp
            },
            {
                'MetricName': 'Pressure',
                'Unit': 'None',
                'Value': pressure
            },
            {
                'MetricName': 'Humidity',
                'Unit': 'None',
                'Value': humidity
            },
        ],
        Namespace = 'Weather'
    )
    
    return {
        'temperature in Gent': temp,
        'pressure in Gent': pressure,
        'humidity in Gent': humidity
    }

