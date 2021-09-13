# Branches, Remotes, and Conflicts                                                        

## Summary

We'll continue with our survey of `git` and GitHub with a focus
now on navigating local and remote branches.  As we get further into
collaborative work (including with ourselves!), *merge conflicts*
will arise, and we'll see how to handle them.

<!--

## Learning Outcomes

  - Students will be able to create, update, and push branches.

  - Students will be able to define remote repository locations and
    fetch/push updates from/to those repositories.

  - Students will be able to recognize avoidable merge conflicts and
    resolve unavoidable merge conflicts


## Essential Questions

      What question(s) will your students be able to answer by the end of
      instruction?

  - What happens if my friend and I both make a pull request into the
    same remote branch?

  - How can make a development branch on my computer and have it show up
    on GitHub?

  - What is the difference between `branch`, `clone`, and `fork`?

-->


## Resources

The [Pro Git](https://git-scm.com/book/en/v2) book is freely available and
provides just about all one needs to dive into `git` for the first time.

Atlassian provides this [nice git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)



##  Evidence of Student Learning


  - Students will clone a remote repository, make a new branch, and push
    changes in that branch to the remote
  - Students will explain how to fix a merge conflict.
  - Students will reflect on their learning by completing their daily log.


## Learning Plan


### Required Preparation

  - Skim Pro Git chapters 5 and 6.


### Live Activities

  1. Exercise to understand basic mechanics of a two-person development cycle.
     -  Head to `https://github.com/me701/homework2_teams` and *fork* it to your account
     -  Clone https://github.com/your_github_name/homework2_teams
     -  Find your name in the list of students and modify it following the
        directions
     -  Commit and push your changes to your GitHub repository
     -  Create a pull request for your changes back to `me701/homework2_teams`
        that you forked.
     -  Add one student to `me701/homework2_teams` to illustrate permissions
        and demonstrate how a PR is reviewed and merged.
  2. Exercise to demonstrate branches and conflicts.
     - Head to `https://github.com/me701/conflicted_python` and *fork* it.
     - Clone it.
     - Check `git log`
     - Switch to `dev` by typing `git checkout dev` and check the log.  
     - Merge `dev` into `master` and push.
     - Checkout a new branch called `demo` from `master`.  Implement the Python function
       and push this new branch.  Then, make a PR into `master` from `demo` on your Fork.

### Videos

 - [Video, Lecture, 09/10/2021](https://mediasite.k-state.edu/mediasite/Play/f39d464b2cd84e1981f5361a66a58a6c1d)
 - slides](https://github.com/robertsj/me701/blob/f2019/lectures/CollaborativeVersionControl.ipynb).


### Useful Tips (To Be Updated As We Learn!)

  - Make directions clearer!
