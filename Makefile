bindir = $(HOME)/bin

TOOLS = \
				gh-org-people \
				gh-repo-people \
				gh-pick-people \
				gh-pick-reviewers \
				gh-pick-assignees \
				gh-pick-labels \
				gh-prs

all:

install:
	install -m 755 -d $(HOME)/bin
	install -m 755 $(TOOLS) $(bindir)
	ln -sf gh-prs $(bindir)/gh-issues
