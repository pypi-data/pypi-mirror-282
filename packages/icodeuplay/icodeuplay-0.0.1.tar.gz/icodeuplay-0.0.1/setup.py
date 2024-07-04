# setup.py

from setuptools import setup, find_packages

setup(
    name="icodeuplay",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
      "python-dotenv",
      "openai",
      "openai-whisper",
      "gtts",
      # Adicione aqui qualquer dependência da sua biblioteca
    ],
    author="Márcio Alves Barroso",
    author_email="marciobarroso@gmail.com",
    description="Utilitary Python Library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/icodeuplay/icodeuplay",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
