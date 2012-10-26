git (Advanced)
~~~~~~~~~~~~~~

This goes beyond the *clone*, *checkin* and *checkout*, *push*, and *pull*
options, and discusses the rarely used features that need a reference
as they are not necessarily used on a daily basis.

**Branching** usage::

    #Create new local branch
    $ git checkout -b branchname [start_point]

    #Delete a local branch
    $ git checkout -d branchname 

    #Look at the local branches
    $ git branch

    #Push a branch to a remote server
    $ git push origin <branchname>

    #Track a remote branch
    $ git checkout --track origin/plugin

    #Delete a remote branch with the colon
    $ git push origin :<branchname>

**Resetting and Restoring** usage::

    #Amending last commit
    $ git commit --amend

    #Resetting every file
    $ git reset HEAD --hard

    #Resetting an edited file to an unstage commit
    $ git reset -- <filename>

    #Restoring a staged file to the previous commit
    $ git reset commit

**Aliases and Config** usage::

    #Aliasing "co" to "Checkout"
    $ git config --global alias.co checkout

**Creating New Repos** usage::

    #Create a new repo
    $ git init

    #Create the repo on the server
    $ git init --bare --share repo.git

    #Now push the local repo up to the server
    $ git push ssh://example.com/git/repo.git "*:*"

