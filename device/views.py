from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from urllib.parse import urlparse, urljoin
import requests, json, base64
from device import models

# Create your views here.
def index(request):
  return render(request,'index.html')
  #return HttpResponse("Sample device app!")

def _nexusinfo(request):
  u = urlparse(request.build_absolute_uri())
  my_domain = u.scheme + '://' + u.netloc
  device_url = reverse('index')
  device_preview_url = my_domain + settings.STATIC_URL + 'images/devices.png'
  return JsonResponse({
        "Name":"Sample Device App",
        "Resources":[
           {
             "Name": "Registered Devices",
             "Details": "<p>List user registered devices</p>",
             "ContentUrl": urljoin(my_domain, device_url),
             "PreviewImage": urljoin(my_domain,device_preview_url),
           }
         ]
       })

def authenticate(request):
  if "token" not in request.GET:
    return JsonResponse({"err":{"message":"Invalid request"}})
  token = request.GET["token"]
  headers = {'Accept': 'application/json', 'authorization': 'JWT ' + token}
  serverUrl = deriveServerUrl(token) #IMPORTANT: Use your url instead of deriving from token. Deriving url from token is insecure
  if serverUrl == "":
    serverUrl = "https://mycompany.nexus.support.com"
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

def subscriberDevices(request, consumer):
  udevices = models.getByConsumer(consumer)
  #return JsonArrayResponse(udevices)
  return HttpResponse(json.dumps(udevices), content_type="application/json")

def deriveServerUrl(jwt):
  try:
    jwtParts = jwt.split(".")
    c = json.loads(base64.b64decode(jwtParts[1]).decode("utf-8"))
    #
    return "https://"+c["t"]+"."+c["d"]
  except:
    return ""

