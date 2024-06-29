from setuptools import setup, find_packages

setup(
    name="rgrader",
    version='0.0.8',
    packages=find_packages(),
    description="A simple grader for python problems",
    install_requires=[],
    entry_points={
        'console_scripts': [
            "grade = rgrader:grade"
        ]
    }
)
