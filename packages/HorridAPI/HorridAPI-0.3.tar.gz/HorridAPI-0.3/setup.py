from setuptools import setup, find_packages


with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
    


# Setting up
setup(
    name="HorridAPI",
    version='0.3',
    author="Horrid",
    author_email="narutomalayalam@gmail.com",
    description="Horrid api",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/Mishel-Tg/HorridAPI",
    download_url="https://github.com/Mishel-Tg/HorridAPI/blob/main/README.md",
    install_requires=["requests"],
    keywords=['python', "HorridAPI","mrz_bots", "telegram", "WhatsAppbot"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    project_urls={
        "Tracker": "https://github.com/Mishel-Tg/HorridAPI/issues",
        "Community": "https://t.me/XBOTSUPPORTS",
        "Source": "https://github.com/Mishel-Tg/HorridAPI",
    },
    python_requires="~=3.7",
)
