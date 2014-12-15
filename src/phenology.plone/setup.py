import os

from setuptools import setup, find_packages

version = "1.0dev"


def read(*rnames):
    return open(
        os.path.join(".", *rnames)
    ).read()


long_description = "\n\n".join(
    [read("README.rst"),
     read("docs", "INSTALL.rst"),
     read("docs", "CHANGES.rst")]
)

classifiers = [
    "Framework :: Plone",
    "Framework :: Plone :: 4.0",
    "Framework :: Plone :: 4.1",
    "Framework :: Plone :: 4.2",
    "Framework :: Plone :: 4.3",
    "Programming Language :: Python",
    "Topic :: Software Development"]

name = "phenology.plone"
setup(
    name=name,
    namespace_packages=[
        "phenology"
    ],
    version=version,
    description="Plone theme for CREA Mont Blanc Pheneologie",
    long_description=long_description,
    classifiers=classifiers,
    keywords="",
    author="Eric BREHAULT <eric.brehault@makina-corpus.com>",
    author_email="eric.brehault@makina-corpus.com",
    url="http://www.creamontblanc.org/",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "setuptools",
        "z3c.autoinclude",
        "Plone",
        "chardet",
        "plone.app.upgrade",
        "plone.app.themingplugins",
        "collective.dexteritytextindexer",
        "plone.app.dexterity [relations]",
        "plone.app.referenceablebehavior",
        "plone.directives.dexterity",
        "plone.directives.form",
        "plone.app.theming",
        "plone.app.themingplugins",
        # with_ploneproduct_pacaching
        "plone.app.caching",
        # with_binding_pil
        "Pillow",
        # with_ploneproduct_enewsletter
        "Products.EasyNewsletter",
        # -*- Extra requirements: -*-
        "collective.cover",
    ],
    extras_require={
        "test": ["plone.app.testing", "ipython"]
    },
    entry_points={
        "z3c.autoinclude.plugin": ["target = plone"],
    },
)
# vim:set ft=python:
