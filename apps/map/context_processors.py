from apps.map import models


def campusrequest(request):
    campuses = models.Campus.objects.all().order_by('name')
    return {'campuses': campuses}
