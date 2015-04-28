# Sample Guided Path App

The main logic is in device/templates/index.html. 

Following are the highlights:

* Include SDK javascript nexusNavigator.js
<code>
<script type="text/javascript" src="//static.nexus.support.com/gpa/v1/nexusNavigator.js"></script>
</code>

* Initialize the neuxs api object

<code>
  var nexusApi = null;
  nexusNavigator.on('ready', function (api) {
    console.log("Nexus API is ready");
    nexusApi = api;
    onReady();
  });
</code>
    
* Load nexus style sheets (optional).

<code>
nexusNavigator.loadCss();
</code>

* Get token for authentication. This should be authenticated from a backend API. Backend authentication is desired because of security reasons.

<code>
    nexusApi.getToken(function(token){
      console.log("AuthenticateUser: Token received. Validating with server");
      var jqxhr = $.ajax( {
        type: "GET",
        url: "/device/authenticate/?token="+token
</code>
* After authentication succeeds, access nexus session details. Similarly other nexus objects can be accessed (refer documentation http://developer.support.com/GPA.html).

<code>
    nexusApi.getSession(function(session){
      getSubscriberDevice(session.consumer, callback);
    });
</code>    
    
* Optionally, if there is a need to push commands to remote connected device over websocket channel, refer following code:

<code>
   //Invoked when nexus is connected to remote device over websocket channel. This is optional.
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
  </code>  
