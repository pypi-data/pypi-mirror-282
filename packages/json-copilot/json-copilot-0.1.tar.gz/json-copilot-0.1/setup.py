from setuptools import setup, find_packages

setup(
    name='json-copilot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit',
        'openai',
        'jsonschema'
        # Add any other dependencies here
    ],
)
