# Python Workflow

Below are a few tools you should *always* use when developing a Python module!

## virtualenv

Always use `virtualenv env` in the topmost directory of your program. This creates a new instance of Python in a local directory named `env` and associates all installed packages with that version of Python. This helps prevent packages from different Python applications from interfering with each other. Avoid ever installing packages locally, except for virtualenv itself.

`env` is the name of the environment - you can name it something else if you desire.

To activate the virtual environment, use `Scripts/activate.bat` . To deactivate it, use `Scripts/deactivate.bat`.

## pip

Always use `pip freeze` to generate a `requirements.txt`. Then, you or your collaborators can use `pip install -r requirements.txt` when they need to work on the program from a different environment.

To keep your app safe from unexpected behavior, always use `package==1.3`, not `package` or `package>=1.3`.

## git

Use it. Upload your `pip`-generated requirements.txt, but don't upload your virtual environment directoy.

## unittest

Use `unittest` (or some other testing framework, like `pytest`) to write tests for your code. Below is a basic example of a unit testing class.

    import unittest

    class TestStringMethods(unittest.TestCase):

        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when separator is not string
            with self.assertRaises(TypeError):
                s.split(2)

        if __name__ == '__main__':
            unittest.main()

You should write unit tests as you develop your code. Ideally, small functions should be written, and each should be tested individually for correct behavior. Integration testing can be done upon completion.

A comprehensive list of `unittest`'s assert functions can be found in `unittest_assert_functions/`

## [setuptools](https://setuptools.readthedocs.io/en/latest/)

Use `setuptools` to package your module and make it easily installable. Create a `MANIFEST.in` file to specify what to include in your module.

Afterwards, you can install the project in editable mode into a virtual environment using `pip install -e .`.