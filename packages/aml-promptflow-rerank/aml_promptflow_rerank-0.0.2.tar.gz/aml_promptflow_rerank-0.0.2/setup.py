from setuptools import find_packages, setup

PACKAGE_NAME = "aml-promptflow-rerank"

setup(
    name=PACKAGE_NAME,
    version="0.0.2",
    description="This is my tools package",
    packages=find_packages(),
    entry_points={
        "package_tools": ["rerank_tool = rerank.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
    install_requires=[
        "azure.ai.ml>=1.5.0",
        "azure.identity>=1.12.0",
        "azureml.rag[azure]>=0.2.28,!=0.2.31",  # noqa: E501
        "requests>=2.28.1",
        "requests-cache~=1.1.1",
        "ruamel.yaml>=0.17.10,<1.0.0",
        "rank-bm25>=0.2.2,<0.3",
    ],
)