# Git Flows

This sheet summarizes the `git` workflows we use in this class.  This does 
not represent all use cases.


## Case 1 - Working Alone with Only Local Changes

Everything we do in this class lives on GitHub. The simplest use case is
when you create (or are given) a repository on GitHub and need to 
make changes locally.  Here's a sample flow:


 1. "Copy" the repository from GitHub onto your machine.

```
you$ git clone https://github.com/you/therepo.git
```

 2. If this is a *private* repository, you'll need to enter your
GitHub user name and your [personal token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).  Otherwise, it should clone without issue.


 3. Make any changes and commit them.  For example, say you changed `README.md`.

```
you$ cd therepo           # make sure you are in the repo
you$ git add README.md    # add before committing
you$ git commit -m "Updated some info in the README file."
```

 4. Send your commits to GitHub:


```
you$ git push
```

You'll definitely need to enter your GitHub user name and your [personal token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).  

## Case 2 - Working Alone with Changes from Multiple Sources

This is almost as common.  Suppose you work on your laptop and make
updates to `therepo` like you did in Case 1.  Then you go to the office
to work on `therepo` but using your desktop machine.  You need to make
sure your local copy is up-to-date:

```
you$ cd /path/to/therepo 
you$ git checkout master # usually the default, but good practice
you$ git fetch
you# git merge origin/master   
```

Alternatively, you can combine the `fetch` and `merge` into one, simple command:

```
you$ git pull  # = git fetch; git merge origin/master 
```

Now, any changes you make locally will be made to a current version of `master`.  If you don't
do this before you make changes, any commits to `origin/master` will result in an error (that
says to update your local repository!)

## Case 3 - Connecting to the Mothership

Assume you have forked `me701/project` to `you/project`.  

```
you$ git clone https://github.com/you/project.git
you$ cd project
```

Add the `mothership`:

```
you$ git remote add mothership ttps://github.com/me701/project.git
```

Verify you have both `origin` and `mothership`:

```
you$ git remote -v
```

If you have a typo in the address, etc., then start over by first
removing the remote repository:

```
you$ git remote remove mothership
```

To update your repository's master branch with changes from the `mothership` master branch, do

```
you$ git checkout master # again, you're usually in the master branch by default but good practice
you$ git fetch mothership
you$ git merge mothership/master
```

To get those same changes back to `you/project`, do

```
you$ git push
```

## Making a Dev Branch

Suppose you are developing some new code feature, etc. in `project`.  To keep it 
separate from the "always should work" `master` branch, do

```
you$ git checkout -b dev
```

Make your changes, add files, commit, etc.  Then, to push this branch to your
remote repository, do

```
you$ git push origin dev
```

Now, you'll have two branches on your GitHub account: `master` and `dev`.

If you want to merge your `dev` changes into `master`, do

```
you$ git checkout master
you$ git merge dev
```

