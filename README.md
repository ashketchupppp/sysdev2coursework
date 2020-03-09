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

# how we are going to work
we have to test each individual module that we write and each module has a specific file structure.
in the example directory there is an example module, copy the structure of this module for any module that you write.

michael marked me down for not using docstrings in the last piece of coursework so make sure every function
has a docstring.
 - Triple quotes are used even though the string fits on one line. This makes it easy to later expand it.
 - The closing quotes are on the same line as the opening quotes. This looks better for one-liners.
 - There's no blank line either before or after the docstring.
 - The docstring is a phrase ending in a period. It prescribes the function or method's effect as a command ("Do this", "Return that"), not as a description; e.g. don't write "Returns the pathname ...".
 - The one-line docstring should NOT be a "signature" reiterating the function/method parameters (which can be obtained by introspection). Don't do:
more information here https://www.python.org/dev/peps/pep-0257/ (i use a docstring in the example module)


# best practices
here is a list of things which yu should do when you are working
   1. work incrementally and commit often. large changes take a LONG time to review.
