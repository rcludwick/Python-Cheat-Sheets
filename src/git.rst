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

**Amending Commit Message** usage::

    #Amending last commit
    $ git commit --amend

