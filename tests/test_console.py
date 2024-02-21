#!/usr/bin/python3
"""Testing HBNBCommand class module"""
import os
import unittest
from models import storage
import uuid
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.base_model import Base
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import sys


class TestConsole(unittest.TestCase):
    """Testing BaseModem Class"""

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_prompt(self):
        self.assertEqual(HBNBCommand.prompt, "")

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_EOF(self):
        with patch("sys.stdout", new=StringIO()):
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().emptyline()
            self.assertEqual(otpt.getvalue().strip(), "")

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"BaseModel.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create City")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"City.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Place")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Place.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create User")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"User.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create State")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"State.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Review")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Review.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create Amenity")
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Amenity.{class_id}"
            self.assertIn(thekey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd('create Amenity name="Hello" num=123.123')
            class_id = f"{otpt.getvalue().strip()}"
            self.assertIsInstance(uuid.UUID(class_id), uuid.UUID)
            thekey = f"Amenity.{class_id}"
            self.assertIn(thekey, storage.all().keys())

    def test_create_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create ")
            error_message = "** class name missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create abcd")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.create()")
            error_message = "*** Unknown syntax: User.create()"
            self.assertEqual(otpt.getvalue().strip(), error_message)

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"show BaseModel {class_id}")
            obj_str = storage.all()[f"BaseModel.{class_id}"].__str__()
            self.assertEqual(otpt.getvalue().strip(), obj_str)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"BaseModel.show(\"{class_id}\")")
            obj_str = storage.all()[f"BaseModel.{class_id}"].__str__()
            self.assertEqual(otpt.getvalue().strip(), obj_str)

    def test_show_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show ")
            error_message = "** class name missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show abcd")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show User")
            error_message = "** instance id missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("show User 12434")
            error_message = "** no instance found **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(".User(\"1234\")")
            error_message = "*** Unknown syntax: .User(\"1234\")"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("abcd.show(1234)")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.show()")
            error_message = "** instance id missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.show(\"1234\")")
            error_message = "** no instance found **"
            self.assertEqual(otpt.getvalue().strip(), error_message)

    def test_destroy(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"destroy BaseModel {class_id}")
            self.assertNotIn(f"BaseModel.{class_id}", storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            class_id = f"{otpt.getvalue().strip()}"
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(f"BaseModel.destroy(\"{class_id}\")")
            self.assertNotIn(f"BaseModel.{class_id}", storage.all().keys())

    def test_destroy_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("destroy ")
            error_message = "** class name missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("destroy abcd")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("destroy User")
            error_message = "** instance id missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("destroy User 12434")
            error_message = "** no instance found **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(".User(\"1234\")")
            error_message = "*** Unknown syntax: .User(\"1234\")"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("abcd.destroy(1234)")
            error_message = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.destroy()")
            error_message = "** instance id missing **"
            self.assertEqual(otpt.getvalue().strip(), error_message)
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("User.destroy(\"1234\")")
            error_message = "** no instance found **"
            self.assertEqual(otpt.getvalue().strip(), error_message)

    def test_all(self):
        with patch("sys.stdout", new=StringIO()):
            HBNBCommand().onecmd(HBNBCommand().precmd("create State name='mo salah'"))
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(HBNBCommand().precmd("State.all()"))
            result = []
            for model, obj in storage.all().items():
                if "State" in model:
                    result.append(obj.__str__())
            self.assertEqual(otpt.getvalue().strip(), f"{result}")

    def test_all_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(HBNBCommand().precmd("abcd.all()"))
            error = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error)

    def test_count(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(HBNBCommand().precmd("State.count()"))
            x = int(otpt.getvalue().strip())
            HBNBCommand().onecmd(HBNBCommand().precmd("create State name='mo salah'"))
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(HBNBCommand().precmd("State.count()"))
            y = int(otpt.getvalue().strip())
            self.assertEqual(y - x, 1)

    def test_count_errors(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd(HBNBCommand().precmd("abcd.count()"))
            error = "** class doesn't exist **"
            self.assertEqual(otpt.getvalue().strip(), error)

    def test_update(self):
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            bs_id = otpt.getvalue().strip()
        with patch("sys.stdout", new=StringIO()):
            HBNBCommand().onecmd(f"update BaseModel "
                                 f"{bs_id} fname \"mohamed\"")

            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "fname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].fname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].fname,
                             "mohamed")
            HBNBCommand().onecmd(f"update BaseModel "
                                 f"{bs_id} sname \"nour eldean\"")

            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "sname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].sname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].sname,
                             "nour eldean")
            HBNBCommand().onecmd(f"update BaseModel "
                                 f"{bs_id} age 30")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "age"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].age,
                                  int)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].age,
                             30)
            HBNBCommand().onecmd(f"update BaseModel "
                                 f"{bs_id} height 1.79")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "height"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].height,
                                  float)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].height,
                             1.79)
            HBNBCommand().onecmd(f"BaseModel.destroy({bs_id})")
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            bs_id = otpt.getvalue().strip()
        with patch("sys.stdout", new=StringIO()):
            HBNBCommand().onecmd(f"BaseModel.update(\"{bs_id}\", \"fname\","
                                 f" \"mohamed\")")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "fname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].fname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].fname,
                             "mohamed")
            HBNBCommand().onecmd(f"BaseModel.update(\"{bs_id}\", \"sname\","
                                 f" \"nour eldean\")")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "sname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].sname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].sname,
                             "nour eldean")
            HBNBCommand().onecmd(f"BaseModel.update(\"{bs_id}\", \"age\","
                                 f" 30)")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "age"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].age,
                                  int)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].age,
                             30)
            HBNBCommand().onecmd(f"BaseModel.update(\"{bs_id}\", \"height\","
                                 f" 1.79)")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "height"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].height,
                                  float)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].height,
                             1.79)
            HBNBCommand().onecmd(f"BaseModel.destroy({bs_id})")
        with patch("sys.stdout", new=StringIO()) as otpt:
            HBNBCommand().onecmd("create BaseModel")
            bs_id = otpt.getvalue().strip()
        with patch("sys.stdout", new=StringIO()):
            dic_obj = {"fname": "mohamed", "sname": "nour eldean",
                       "age": 30, "height": 1.79}
            HBNBCommand().onecmd(f"BaseModel.update(\"{bs_id}\", {dic_obj})")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "fname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].fname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].fname,
                             "mohamed")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "sname"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].sname,
                                  str)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].sname,
                             "nour eldean")
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "age"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].age,
                                  int)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].age,
                             30)
            self.assertTrue(hasattr(storage.all()[f"BaseModel.{bs_id}"],
                                    "height"))
            self.assertIsInstance(storage.all()[f"BaseModel.{bs_id}"].height,
                                  float)
            self.assertEqual(storage.all()[f"BaseModel.{bs_id}"].height,
                             1.79)
            HBNBCommand().onecmd(f"BaseModel.destroy({bs_id})")


if __name__ == "__main__":
    unittest.main()
