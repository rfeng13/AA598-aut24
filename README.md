# AA598 Safe Autonomy

Fork this package.
Create a virtual environment and then activate it. Once activated, install the `aa598` package in editable mode. For example,
```
cd path_to_where_you_want_aa598_material
git clone <your forked repo>
cd AA598-aut24
python3 -m venv aa598_venv
source aa598_venv/bin/activate
pip install -e .
```
Alternatively, you can create a new venv via VSCode.

The `aa598` folder contains homework helper code.

The `homework` folder contains the homework starter code.

To start working on a new homework, sync the latest changes from UW-CTRL. Go to your forked repo site, and on the `main` branch, click "Sync fork."  
Then pull from the main branch
```git pull origin main```

To (hopefully) avoid conflicts, create a new branch when starting a new homework. For example, for homework X. After pulling from main,
```
git checkout -b homework_X
```
You can edit the starter code and save and commit your changes on the `homework_X` branch while keeping the `main` branch clean and avoiding merge conflicts when pulling the latest changes.
To commit your own changes/progress

```
git add <files you want to add>
git commit -m <commit message>
git push origin homework_X
```

To switch back to the main branch (after committing and pushing your homework_X changes and syncing with the upstream main branch),

```
git checkout main
```