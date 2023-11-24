# geoip2

##### Cloud Development Kit (CDK) v2

```python
        region = Stack.of(self).region

        censys = _lambda.LayerVersion.from_layer_version_arn(
            self, 'geoip2',
            layer_version_arn = 'arn:aws:lambda:'+region+':070176467818:layer:geoip2:1'
        )
```

##### AWS Lambda Layer for Python Library

 1. ```cd bundle```
 2. ```mkdir python```
 3. ```cd python```
 4. ```pip3 install geoip2 -t .```
 5. ```cd ..```
 6. ```zip -r geoip2.zip .```
 7. ```rm -R python```
 