from django.test import TestCase
from django.urls import reverse

from apps.learning.python_playground import extract_python_starter
from apps.sandbox.python_executor import python_executor
from tests.helpers import make_course, make_lecture, make_module, make_user


class PythonSandboxTests(TestCase):
    def test_executor_print(self):
        result = python_executor.execute('print("hi")\nprint(2+2)')
        self.assertTrue(result.ok, msg=result.stderr)
        self.assertIn("hi", result.stdout)
        self.assertIn("4", result.stdout)

    def test_executor_blocks_open(self):
        result = python_executor.execute('open("x.txt","w")')
        self.assertFalse(result.ok)
        self.assertTrue(result.stderr)

    def test_executor_blocks_os(self):
        result = python_executor.execute("import os\nprint(os.getcwd())")
        self.assertFalse(result.ok)

    def test_extract_starter_from_pre(self):
        html = "<p>x</p><pre>print(1)\nprint(2)</pre>"
        self.assertEqual(extract_python_starter(html), "print(1)\nprint(2)")

    def test_run_endpoint_on_python_lecture(self):
        course = make_course("python", published=True, visible=True, title="Python")
        module = make_module(course, slug="py-m1")
        lecture = make_lecture(module, slug="py-lec")
        lecture.content = "<pre>print(1)</pre>"
        lecture.save(update_fields=["content"])
        user = make_user("py-student@example.com", role="student")
        self.client.force_login(user)
        url = reverse("learning:run_python", kwargs={"pk": lecture.pk})
        res = self.client.post(url, {"code": 'print("ok")'})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["ok"], msg=data)
        self.assertIn("ok", data["stdout"])

    def test_run_endpoint_rejects_non_python_course(self):
        course = make_course("sql", published=True, visible=True)
        module = make_module(course, slug="sql-m1")
        lecture = make_lecture(module, slug="sql-lec")
        user = make_user("sql-student@example.com", role="student")
        self.client.force_login(user)
        url = reverse("learning:run_python", kwargs={"pk": lecture.pk})
        res = self.client.post(url, {"code": "print(1)"})
        self.assertEqual(res.status_code, 400)

    def test_lecture_page_shows_playground(self):
        course = make_course("python", published=True, visible=True, title="Python")
        module = make_module(course, slug="py-m1")
        lecture = make_lecture(module, slug="py-lec")
        lecture.content = "<p>Hi</p><pre>print(9)</pre>"
        lecture.save(update_fields=["content"])
        user = make_user("py-page@example.com", role="student")
        self.client.force_login(user)
        res = self.client.get(reverse("learning:lecture", kwargs={"pk": lecture.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "python-playground")
        self.assertContains(res, "Python ni ishga tushirish")
