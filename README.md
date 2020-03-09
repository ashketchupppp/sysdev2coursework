# Systems Development Group Coursework: Dartmouth 

This is the main repository for our systems development coursework code.

git is a version control system, github is the central place for storing git repositories.
to use github you should make an account on this website and install github desktop.

you can use git in the command line or use github desktop. i would recommend github desktop.

# quick guide to Github
there are plenty of resources online which teach you how to use github.

once you have everything installed you need to clone this repository and place it somewhere.
i would suggest C:/Users/YourUserName/Documents/Github/RepositoryName
in Github desktop you can add a repository at the top left.

a branch is a set of files. every repository has a "master" branch.
the master branch is considered the branch which represents the repository, other branches are just things that are works in progress.
before you can make changes to the repository you need to make a new branch which is a copy of master at the time that you made the branch.
then you need to checkout the branch, this just means use the branch, i'm not sure why its called checkout.

now you can make changes to your code, they will be automatically picked up by Github desktop.

when you are happy with your changes you should commit them to your branch with the button at the bottom left.  
then at the top menu you go to Repository > Push to push your changes to the branch that is stored on Github (as opposed to storing them on your own computer as they have been up to this point) 

then to merge your branch with master you should go to this page and make a pull request. (note: it's a request not a demand)

# quick git command line guide
how you should make changes to this git repository is:
 - make a NEW branch "git branch branch_name_here"
 - checkout the branch (start using it) "git checkout branch_name"
 - make sure you are not on the master branch "git status"
 - make your changes
 - add your changes to the branch "git add ."
 - commit your changes to the branch "git commit -m commit message here"
 - make a pull request to merge to with the master branch.
   this is done on this page, not in the command line.
   it is a request, your changes aren't immediately made, the owner of
   this repository (chris) will review the change before it can be made.
