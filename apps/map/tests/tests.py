from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from apps.map.views import MainView
from apps.map.views import DirectoriesView, AboutusView, CampusListView, CampusDetailView, BuildingDetailView, BuildingListView
from apps.map.json_views import CampusCollection, BuildingCollection, FacultyCollection, RecreationCollection
from apps.map.json_views import ClassroomCollection, ParkinglotCollection
from apps.map import models


class PicsTestCase(TestCase):
    def setUp(self):
        pass

    def test_pics_string(self):
        """verifying __str__returns with proper formatting"""
        pics = models.Pics.objects.get(pk=2)
        self.assertEqual(pics.__str__(), "Continuing Education and Performing Arts")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class CampusTestCase(TestCase):
    def setUp(self):
        pass

    def test_campus_string(self):
        """verifying __str__returns with proper formatting"""
        campus = models.Campus.objects.get(pk=1)
        self.assertEqual(campus.__str__(), "Gainesville Campus")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class BuildingTestCase(TestCase):
    def setUp(self):
        pass

    def test_building_string(self):
        """verifying __str__returns with proper formatting"""
        building = models.Building.objects.get(pk=1)
        self.assertEqual(building.__str__(), "Martha T. Nesbitt Academic")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class OfficeTestCase(TestCase):
    def setUp(self):
        pass

    def test_office_string(self):
        """verifying __str__returns with proper formatting"""
        pass

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class FacultyTestCase(TestCase):
    def setUp(self):
        pass

    def test_faculty_string(self):
        """verifying __str__returns with proper formatting"""
        faculty = models.Faculty.objects.get(pk=1)
        self.assertEqual(faculty.__str__(), "Ann Marie Francis")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class ParkinglotTestCase(TestCase):
    def setUp(self):
        pass

    def test_parkinglot_string(self):
        """verifying __str__returns with proper formatting"""
        parkinglot = models.ParkingLots.objects.get(pk=1)
        self.assertEqual(parkinglot.__str__(), "A")

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class ClassroomTestCase(TestCase):
    def setUp(self):
        pass

    def test_classroom_string(self):
        """verifying __str__returns with proper formatting"""
        pass

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class RecreationTestCase(TestCase):
    def setUp(self):
        pass

    def test_recreation_string(self):
        """verifying __str__returns with proper formatting"""
        pass

    def test_absolute_url(self):
        """Verifying get_absolute_url returns the right url."""
        pass


class UrlTests(TestCase):
    """
    Verifying the urls use the correct views
    """
    def test_main_url(self):
        main = resolve(reverse('map:main_page'))
        return self.assertEqual(main.func.__name__,
                                MainView.__name__)

    def test_directories_view(self):
        dir_view = resolve(reverse('map:directories'))
        return self.assertEqual(dir_view.func__name__,
                                DirectoriesView.__name__)

    def test_aboutus_view(self):
        aboutus_view = resolve(reverse('map:aboutus'))
        return self.assertEqual(aboutus_view.func__name__,
                                AboutusView.__name__)

    def test_campus_lview(self):
        campus_lview = resolve(reverse('map:campus_lview'))
        return self.assertEqual(campus_lview.func__name__,
                                CampusListView.__name__)

    def test_campus_dview(self):
        campus_dview = resolve(reverse('map:campus_dview'))
        return self.assertEqual(campus_dview.func__name__,
                                CampusDetailView.__name__)

    def test_building_lview(self):
        building_lview =  resolve(reverse('map:building_lview'))
        return self.assertEqual(building_lview.__name__,
                                BuildingListView.__name__)

    def test_building_dview(self):
        building_dview = resolve(reverse('map:building_dview'))
        return self.assertEqual(building_dview.func__name__,
                                BuildingDetailView.__name__)

    def test_api_campus(self):
        campus = resolve(reverse('map_api:campus_collection'))
        return self.assertEqual(campus.func__name__,
                                CampusCollection.__name__)

    def test_api_buildings(self):
        buildings = resolve(reverse('map_api:buildings_collection'))
        return self.assertEqual(buildings.func__name__,
                                BuildingCollection.__name__)

    def test_api_faculty(self):
        faculty = resolve(reverse('map_api:faculty_collection'))
        return self.assertEqual(faculty.func__name__,
                                FacultyCollection.__name__)

    def test_api_recreation(self):
        recreation = resolve(reverse('map_api:recreation_collection'))
        return self.assertEqual(recreation.func__name__,
                                RecreationCollection.__name__)

    def test_api_classrooms(self):
        classrooms = resolve(reverse('map_api:classrooms_collection'))
        return self.assertEqual(classrooms.func__name__,
                                ClassroomCollection.__name__)

    def test_api_parkinglots(self):
        parkinglots = resolve(reverse('map_api:parkinglots_collection'))
        return self.assertEqual(parkinglots.func__name__,
                                ParkinglotCollection.__name__)
