from setuptools import setup, find_packages

setup(
    name='referral',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2',  # or your Django version
    ],
    description="A reusable Django referral system app",
    author="Andrew Oduola",
    author_email="andrewoduola@gmail.com",
    # url="https://github.com/Andrew-oduola/my_referral_app",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
