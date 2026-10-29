# GH Tools

This is a collection of tools that take advantage of the [gh] GitHub cli
and [fzf], the interactive fuzzy finder terminal UI.

[gh]: https://github.com/cli/cli
[fzf]: https://github.com/junegunn/fzf

## Prerequisites

You will need to install `gh` and `fzf`. You will also need Linux or Linux-like
environment. Feel free to submit pull requests to make the tools run elsewhere.

### Optional

If you have the `glow` command installed, it will be used to render Markdown in
the preview window.

## Installation

Running `make install` will install the tools into `$HOME/bin`.

## The tools

### gh-prs and gh-issues

These tools present you with a list of pull requests or issues (when called
as `gh-prs` you get pull requests, and when called as `gh-issues` you get
issues). Pressing ENTER on an entry will open it in a web browser. Pressing
CTRL-T will open a preview window showing the pull request or issue
description. The list supports fuzzy searching; as you type, the list will
be filtered to show the best matches for your search string.

When run inside a git repository, these tools will by default operate
against the repository organization (or user, for individually owned
repositories). You can set a default organization by setting your
`GITHUB_ORG` environment variable, or by using the `-o`/`--org` command
line option:

```sh
gh-prs -o cci-moc
```

Without any qualifiers, the tool will list all pull requests or issues in
the organization. You can filter that list using one of the following
options:

- `--me` -- show pull requests or issues in which you are "involved". This
  means you are the author, the assignee, a commenter, or you are mentioned
  in a comment.

- `--mine` -- show pull requests or issues for which you are the author.

- `-A|--assignee ASSIGNEE` -- show pull requests or issues assigned to
  `ASSIGNEE`.

- `-a|--author AUTHOR` -- show pull requests or issues with author
  `AUTHOR`.

- `-c|--commenter COMMENTER` -- show pull requests or issues with a comment
  by `COMMENTER`.

- `-m|--mentions USER` -- show pull requests or issues that mention `USER`.

In all cases, you can use `@me` to refer to yourself (`-m @me`).

#### Options that only apply to gh-prs

- `--review` -- show pull requests that are waiting on your review (not
  valid with `gh-issues`).

- `--no-dependabot|-D` -- do not show pull requests created by dependabot.

### gh-pick-reviewers and gh-pick-assignees

These are command line tools that allow you to select assignees (for pull
requests or issues) or reviewers (for pull requests). You use them like
this:

```sh
gh issue create -t 'This is an issue' $(gh-pick-assignees)
```

Or like this:

```sh
gh pr create -f $(gh-pick-reviewers)
```

(Etc.)

These tools must be run from inside a repository that is a member of the
target organization. This will present you with a list of users; you can
select a single user by pressing ENTER immediately, or you can select
multiple users with the TAB key (and then press ENTER to submit your
selection).

`gh-pick-reviewers` will only present users that are associated with the
current repository. `gh-pick-assignees` will present a list of all members
of the organization.
