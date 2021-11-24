# Documentation

## How to contribute

Contributions are welcome, and in order to organize contributions have some guide lines outlined below.  

### Coding style
We try to maintain a uniform look of the code following guidelines from [PEP-8](https://www.python.org/dev/peps/pep-0008/), see also [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/).

We also urge contributors to use function annotations as defined in [PEP-3107](https://www.python.org/dev/peps/pep-3107/).

### Merging to the main branch 
I you would like to merge anything to the main branch follow this simplified development process.
 
First clone the repo and created your own branch
````bash
git clone git@github.com:aidotse/EdgeLab.git
cd EdgeLab
git checkout -b your_branch_name
````
For your branch use a descriptive name, that summarize what new in the branch. 

While you work on your branch remember to rebase regularly, that is 
````bash
git fetch
git rebase -i origin/main
````

Note that at the moment where is no organized testing of the code in this repo. 

In order to merge to master branch we follow the process outlined here: [Merge Branches into Master Branch in GitHub using Pull Requests](https://developers.sap.com/tutorials/webide-github-merge-pull-request.html), and summarized below.

Push your branch to the repo, first time
````bash
git push --set-upstream origin your_branch_name
````
and then 
````bash
git push
````










