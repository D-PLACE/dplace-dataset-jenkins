from setuptools import setup


setup(
    name='cldfbench_jenkins',
    py_modules=['cldfbench_jenkins'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-jenkins=cldfbench_jenkins:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
