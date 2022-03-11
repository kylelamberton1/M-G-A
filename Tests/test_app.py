from flask_testing import TestCase
from application import app, db
from application.models import Movie
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()

        task1 = Movie(director_name="new task", title= "this new task", genre="that new task", plot_summary="final new task")

        db.session.add(task1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        # Will be called after every test
        db.drop_all()

class TestCRUD(TestBase):

    def test_read_tasks(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('new task', str(response.data))
        self.assertIn('this new task', str(response.data))
        self.assertIn('that new task', str(response.data))
        self.assertIn('final new task', str(response.data))

    def test_add_tasks(self):
        response = self.client.post(
            url_for('add'),
            data=dict(director_name="added task", title="this is a added task", genre="that is an added task", plot_summary="final added task"),
            follow_redirects=True
        )
        added_task = Movie.query.get(2)
        self.assertEqual(added_task.director_name, "added task")
        self.assertIn('added task', str(response.data))
        self.assertIn('this is a added task', str(response.data))
        self.assertIn('that is an added task', str(response.data))
        self.assertIn('final added task', str(response.data))

    def test_update_tasks(self):
        response = self.client.post(
            url_for('update', director_name="new task"),
            data=dict(director_name="updated task", title="this is a updated task", genre="that is an updated task", plot_summary="final updated task"),
            follow_redirects=True
        )
        self.assertIn("updated task", str(response.data))
        self.assertIn("this is a updated task", str(response.data))
        self.assertIn("that is an updated task", str(response.data))
        self.assertIn("final updated task", str(response.data))



    def test_delete_tasks(self):
        response = self.client.post(
            url_for('delete', director_name="new task"),
            follow_redirects=True
        )
        self.assertNotIn("new task", str(response.data))
