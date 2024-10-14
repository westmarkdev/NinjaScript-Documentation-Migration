# Git Branching Strategy for NinjaScript Migration

## Main Branches

- `main`: The primary branch containing production-ready code.
- `develop`: Integration branch for features and batches.
- `testing`: Testing branch for features and batches.

## Batch Processing Branches

- `batch/lg`
- `batch/md`
- `batch/sm`
- `batch/xl`
- `batch/xs`
- `batch/pics`

## Feature Branches

- `feature/[feature-name]`

## Hotfix Branches

- `hotfix/[issue-description]`

## Workflow

1. Create a new batch branch from `develop` for each batch of files:

   ```bash
   git checkout -b batch/lg develop
   ```

2. Process the batch, making commits as necessary:

   ```bash
   git commit -m "Process lg batch: [specific changes]"
   ```

3. When batch processing is complete, create a pull request to merge into `develop`.

4. After review, merge the batch branch into `develop`:

   ```bash
   git checkout develop
   git merge --no-ff batch/lg
   git push origin develop
   ```

5. Delete the batch branch after successful merge:

   ```bash
   git branch -d batch/lg
   ```

6. Repeat steps 1-5 for each batch.

7. For new features or improvements not related to a specific batch:

   ```bash
   git checkout -b feature/[feature-name] develop
   ```

8. When all batches are processed and features are complete, create a release branch:

   ```bash
   git checkout -b release/v1.0 develop
   ```

9. After final testing, merge the release branch into both `main` and `develop`:

   ```bash
   git checkout main
   git merge --no-ff release/v1.0
   git push origin main

   git checkout develop
   git merge --no-ff release/v1.0
   git push origin develop
   ```

10. Tag the release on `main`:

    ```bash
    git tag -a v1.0 -m "Version 1.0"
    git push origin v1.0
    ```

11. For critical fixes, create a hotfix branch from `main`, fix the issue, and merge back into both `main` and `develop`.
