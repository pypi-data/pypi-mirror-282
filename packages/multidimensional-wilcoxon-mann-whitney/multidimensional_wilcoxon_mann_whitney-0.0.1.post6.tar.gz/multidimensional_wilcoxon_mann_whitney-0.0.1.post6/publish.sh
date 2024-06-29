git add -u && git commit -m "up" && git push
python -m build
python3 -m twine upload --repository pypi dist/*