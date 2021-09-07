# Collaborative Version Control with `git` and GitHub                                                         

## Summary

By the end of this lesson, you should be able to demonstrate the
basic, collaborative development cycle using `git` and GitHub (or
similar repository-hosting systems).  Along the way, you will work
with a partner to complete part of the next homework.

<!--

## Learning Outcomes

  - Students will be able to employ command-line tools to create, access, and
    modify remote software repositories.

  - Students will be able to write succinct messages for the repository
    log that describe source-code modifications.

  - Students will be able to select an appropriate collaborative workflow.


## Essential Questions

  - How can I use a `git` repository that lives on another server?

  - How can my friend and I work on the same repository at the same time?

  - What is a `branch` and a `fork`?

-->

## Resources

The [Pro Git](https://git-scm.com/book/en/v2) book is freely available and
provides just about all one needs to dive into `git` for the first time.

Atlassian provides this [nice git cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

##  Evidence of Student Learning

  - Students will clone, modify, and push changes to a remote repository.
  - Students will fork, clone, modify, push changes to and create a pull
    request for a remote repository.
  - Students will reflect on their learning by completing their daily log.

## Learning Plan

### Before Lecture

  - Skim Pro Git chapters 5 and 6.

### During Lecture

  1. Provide overview of GitHub.
  2. Explain basic collaborative workflows
  3. Introduce essential `git` commands for remote work.
  4. Exercise to understand how to ensure local copies remain up-to-date.
     - `git clone https://github.com/robertsj/me701/` (to get our content)
     - `git checkout f2021` (to get this term's stuff)
     - `git pull` (to get updates i've made)
  5. Exercise to understand basic mechanics of a two-person development cycle.
     -  Head to `https://github.com/me701/homework2_teams` and *fork* it to your account
     -  Clone https://github.com/your_github_name/homework2_teams
     -  Find your name in the list of students and modify it following the
        directions
     -  Commit and push your changes to your GitHub repository
     -  Create a pull request for your changes back to the `me701` repository
        that you forked.

### After Lecture

 - [Video, Lecture, 09/08/2021](tbd)
 - [Lecture, Fall 2019](https://mediasite.k-state.edu/mediasite/Play/0b11a97836724467afc6150837ce3e9f1d)
   and [slides](https://github.com/robertsj/me701/blob/f2019/lectures/CollaborativeVersionControl.ipynb).


### Jeremy's Notes

  - Don't forget that you need `git add` and `git commit` before
    `git push`
  - Students should review pull requests by others; maybe a formal
    assignment of who does what would be good
  - 
