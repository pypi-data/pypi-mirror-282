from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hack4u_prueba",
    version="0.1.4",
    packages=find_packages(), #Para encontrar todos los paquetes del módulo que hemos creado
    install_requires=[],
    author="J.A.R.V.I.S.",
    description="Una biblioteca para consultar cursos",
    long_description=long_description,
    long_description_content_type="text/markdown", #Es contaido en markdow #Es contaido en markdown
    url="https://jarviss",
)
