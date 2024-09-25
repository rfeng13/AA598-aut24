# AA598 Safe Autonomy

Clone this package.
Create a virtual environment and then activate it. Once activated, install the `aa598` package in editable mode. For example,
```
cd path_to_where_you_want_aa598_material
git clone git@github.com:UW-CTRL/AA598-aut24.git
cd AA598-aut24
python3 -m venv aa598_venv
source aa598/bin/activate
pip install -e .
```
Alternatively, you can create a new venv via VSCode.

The `aa598` folder contains homework helper code.

The `homework` folder contains the homework starter code.

To start working on a homework, first pull the latest changes.
```
git checkout main
git fetch origin main
git merge origin/main
```

To (hopefully) avoid conflicts, create a new branch when starting a new homework. For example, for homework X,
```
git checkout -b homework_X
```
And you can edit the starter code and save commit your changes on the `homework_X` branch whilst keeping the `main` branch clean and avoid merge conflicts when the pull the latest changes.
