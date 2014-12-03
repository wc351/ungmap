from django.conf.urls import patterns, include, url
from apps.map import json_views


urlpatterns = patterns('',
                       url(r'^campus', json_views.CampusCollection.as_view(), name='campus'),
                       url(r'^building', json_views.BuildingCollection.as_view(), name='buildings'),
                       url(r'^faculty', json_views.FacultyCollection.as_view(), name='faculty'),
                       url(r'^recreation', json_views.RecreationCollection.as_view(), name='recreation'),
                       url(r'^classrooms', json_views.ClassroomCollection.as_view(), name='classrooms'),
                       url(r'^parkinglots', json_views.ParkinglotCollection.as_view(), name='parkinglots'),
                       url(r'^parkingspots', json_views.ParkingSpotCollection.as_view(), name='parkingspots'),
                       url(r'^parkinglines', json_views.ParkingLotLinesCollection.as_view(), name='parkinglines'),
                       url(r'^callboxes', json_views.CallBoxCollection.as_view(), name='callboxes'),

                       )
