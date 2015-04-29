# Sample Guided Path App

The main logic is in device/templates/index.html. 

Following are the highlights:

* Include SDK javascript //static.nexus.support.com/gpa/v1/nexusNavigator.js

```html
<script type="text/javascript" src="//static.nexus.support.com/gpa/v1/nexusNavigator.js"></script>
```

* Initialize the nexus api object

```javascript
var nexusApi = null;
nexusNavigator.on('ready', function (api) {
  console.log("Nexus API is ready");
  nexusApi = api;
  onReady();
});
```
    
* Load nexus style sheets (optional).

```javascript
nexusNavigator.loadCss();
```

* Get token for authentication. This token should be authenticated from a backend API. Backend authentication is desired because of security reasons.

```javascript
    nexusApi.getToken(function(token){
      console.log("AuthenticateUser: Token received. Validating with server");
      var jqxhr = $.ajax( {
        type: "GET",
        url: "/device/authenticate/?token="+token
```

```python
def authenticate(request):
.....
  token = request.GET["token"]
  headers = {'Accept': 'application/json', 'authorization': 'JWT ' + token}
.....  
  r = requests.get(serverUrl+"/api/v1/oauth2/verify", verify=False, headers=headers)
  if r.status_code == 400:
    return JsonResponse({"err":{"message":"Invalid Token"}})
  if r.status_code == 403:
    return JsonResponse({"err":{"message":"Authentication Failed"}})
  if r.status_code != 200:
    return JsonResponse({"err":{"message":"Server error"}})
  try:
    data = json.loads(r.text)
  except:
    return JsonResponse({"err":{"message":"Error returned by authenticate"}})
  return JsonResponse(data)
```

* After authentication succeeds, access nexus session details. Similarly other nexus objects can be accessed (refer documentation http://developer.support.com/GPA.html).

```javascript
    nexusApi.getSession(function(session){
      getSubscriberDevice(session.consumer, callback);
    });
```
    
* Optionally, if there is a need to push commands to remote connected device over websocket channel, refer following code:

```javascript
   // Invoked when nexus is connected to remote device over websocket channel. This is optional.
  nexusNavigator.on('task-init', function () {
    console.log("Nexus connected to remote device");
    getData();
  });
  
  // Optional commands can be pushed once the websocket channel is open with remote device. Ex:
      nexusApi.isConnected(function (yes) {
      if (yes) {
        //return getDeviceInfo();
        nexusApi.sendCommand("GET_SYSINFO",1,"getInfo",{},function(o) {
          done(null, o);
        });
      } else {
        console.log("Not connected!!!");
        done(new Error("Not Connected!!!"));
      }
    });
```
