# Contributing to Python Project Structure Generator and Analyzer (PyPSGA)

First off, thank you for considering contributing to PyPSGA. It's people like you that make PyPSGA such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/your-username/PyPSGA/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and make one!

## Fork & create a branch

If this is something you think you can fix, then fork PyPSGA and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the PyPSGA code onto your machine. 

```bash
git clone https://github.com/your-username/PyPSGA.git
```

## Make a Pull Request

At this point, you should switch back to your master branch and make sure it's up to date with PyPSGA's master branch:

```bash
git remote add upstream https://github.com/your-username/PyPSGA.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master and push it!

```bash
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Go to the PyPSGA repository and you should see recently pushed branches.

Click "Compare & pull request" button next to your branch. Fill out the PR form, and then press "Create pull request"!

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To update your `325-add-japanese-localisation` branch, use these steps:

```bash
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease origin 325-add-japanese-localisation
```

## What if my Pull Request gets rejected?

Don't despair! The great part about contributing to open source is that all contributions are valuable, and even if your pull request isn't accepted, it may inspire someone else to continue where you left off.

## And last but not least: Always remember to have fun!

We're an open-source project, and we love to see new contributors.
