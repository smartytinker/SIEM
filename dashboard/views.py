from django.shortcuts import render
from incidents.models import Incident
from iocs.models import IOC
from malware.models import MalwareSample

# Create your views here.
# def dashboard(request):
#     incident_count = Incident.objects.count()
#     malware_count = MalwareSample.objects.count()
#     iocs_count = IOC.objects.count()

#     recent_incidents = Incident.objects.order_by('-created_at')[:5]
#     recent_malware = MalwareSample.objects.order_by('-analyzed_at')[:5]
#     recent_iocs = IOC.objects.order_by('-created_at')[:5]

#     context = {
#         "incidents_counts" : incident_count,
#         "malware_counts" : malware_count,
#         "iocs_counts" : iocs_count,
#         "recent_incidents" : recent_incidents,
#         "recent_malware" : recent_malware,
#         "recent_iocs" : recent_iocs,
#     }

#     return render(request, "dashboard/home.html", context)

def dashboard(request):
    incidents = Incident.objects.all()
    incident_count = incidents.count()

    critical_count = incidents.filter(severity="Critical").count()
    high_count = incidents.filter(severity="High").count()
    medium_count = incidents.filter(severity="Medium").count()
    low_count = incidents.filter(severity="Low").count()

    open_incidents = incidents.filter(resolved="False").count()
    recent_incidents = incidents.order_by('-created_at')[:5]

    context = {
        "incident_count" : incident_count,
        "critical_count" : critical_count,
        "high_count" : high_count,
        "medium_count" : medium_count,
        "low_count" : low_count,
        "open_incidents" : open_incidents,
        "recent_incidents" : recent_incidents,
    }

    return render(request, "dashboard/home.html", context)
