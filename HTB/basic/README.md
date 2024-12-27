# some basic code for the hack the box challenges

```bash
#learning GET requests
curl 'http://somewebenepoint/search.php?search=flag' -H 'Authorization: Basic YWRtaW46YWRtaW4='~

#learning post requests
curl -X POST -d '{"search":"flag"}' -b 'PHPSESSID=nhi8b45vnkipqffnhggfo8e0ea' 'somewebenepoint/search.php'  -H 'Content-Type: application/json'

#CRUD

#POST
curl -X POST -d '{"city_name":"flag"}' 'http://somewebenepoint/api.php/city'  -H 'Content-Type: application/json'

#PUT
curl -X PUT -d '{"city_name":"flag", "country_name":"flag"}' 'http://somewebenepoint/api.php/city/flag'  -H 'Content-Type: application/json'


#DELETE
curl -X DELETE 'http://somewebenepoint/api.php/city/portland'  -H 'Content-Type: application/json'
```
