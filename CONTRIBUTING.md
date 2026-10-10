# Contributing to Build Origin

Every improvement starts somewhere. Thanks for considering this one.
Build Origin is a small project built in the open. You don't need to be an expert, write a huge PR, or get everything perfect on your first try. A useful fix is a useful fix.

## Before you jump in

Have an idea that changes how the project works? Open an issue first so we can talk it through.
Spotted a typo, a broken link, or something small that could be better? Feel free to send a PR directly.
If someone is already working on the same thing, check in before starting duplicate work.

## From your machine to a PR

**1. Get your copy ready**

```bash

git clone https://github.com/P-r-e-m-i-u-m/build-origin.git
cd build-origin
git checkout -b fix/short-description

```

Use a branch name that tells people what you're working on.
**2. Make the change**
Keep it focused. Fix the thing you came to fix, and leave unrelated cleanup for another day.
**3. Check what you're about to send**
Stage only the files you meant to change:

```bash

git add path/to/changed-file
git diff --cached --check
git diff --cached

```

Replace `path/to/changed-file` with the actual path. Read the staged diff before moving on. If anything unexpected appears, unstage it and check again.
**4. Save your work and push the branch**

```bash

git commit -m "fix: describe the change"
git push origin fix/short-description

```

**5. Open a pull request**
Explain what changed and why. Add a screenshot if it helps someone understand a visual change. Link the related issue when there is one.
That's it. No need to turn a small fix into a big production.

## Keep the work easy to review

- One PR, one clear purpose.
- Explain the reason when the change isn't obvious.
- Test what you reasonably can.
- Don't include unrelated files or drive-by refactors.
- If something is unfinished, say so. Clear context beats pretending everything is perfect.

## Commit messages

Keep them short and useful. These prefixes are enough:

```text

feat: add something
fix: correct something
docs: explain something
refactor: simplify something
chore: maintain the project

```

You don't need a perfect commit message. Just make the history understandable.

## New to contributing?

That's fine. Ask questions, open an issue, or send a small PR. You don't have to know everything before you begin.

## One last thing

Be thoughtful about the work and respectful toward the people doing it.
Leave the project a little better than you found it. That's what Build Origin is here for.
