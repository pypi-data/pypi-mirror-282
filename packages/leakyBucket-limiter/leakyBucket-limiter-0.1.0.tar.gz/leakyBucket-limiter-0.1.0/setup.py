from setuptools import setup, find_packages

setup(
    name="leakyBucket-limiter",
    version = "0.1.0",
    description = 'A simple rate limitter using redis',
    author = 'Ashish Sharma',
    author_email = 'sarmaassis@gmail.com',
    url = 'https://github.com/sarmaasis/rate-limiter',
    packages = find_packages(),
    install_requires=[
        'redis',
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>3.8'

)