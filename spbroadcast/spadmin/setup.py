from setuptools import setup, find_packages

setup(
        name='tomato',
        version='1.0.0.0',
        description="beehoo_celery task",
        author="Cooler",
        url="http://www.beehoo.cn",
        license="LGPL",
        packages=find_packages(),
        # packages=['utils', 'monitor','itztasks'],
        py_modules=[],
        scripts=[
            # 'bin/startup.sh'
            # 'tomato.py',
            # 'tasks.py',
        ],
        entry_points={
            'console_scripts': [
                # 'tomato=tomato:main'
            ]
        },
        include_package_data=True,
        zip_safe=False,
        install_requires=[

        ]
)
