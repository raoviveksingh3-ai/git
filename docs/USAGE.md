# Usage Guide

## Basic Usage

### Command Syntax

```bash
python contribute.py [OPTIONS]
```

### Required Options

- `--repository=URL`: The target Git repository URL (SSH or HTTPS)

### Optional Options

- `--max_commits=N`: Maximum number of commits to generate (default: 10)
- `--frequency=N`: Time interval between commits in seconds (default: 60)
- `--no_weekends`: Skip weekends when generating commits
- `--help`: Display help information

## Examples

### Example 1: Basic Usage with SSH

```bash
python contribute.py --repository=git@github.com:username/repo.git
```

This will:
- Generate 10 commits (default)
- Wait 60 seconds between commits (default)
- Include weekend days

### Example 2: Generate 12 Commits with Custom Frequency

```bash
python contribute.py \
  --max_commits=12 \
  --frequency=60 \
  --repository=git@github.com:username/repo.git
```

### Example 3: Skip Weekends

```bash
python contribute.py \
  --max_commits=20 \
  --no_weekends \
  --repository=git@github.com:username/myproject.git
```

### Example 4: HTTPS Repository

```bash
python contribute.py \
  --repository=https://github.com/username/repo.git \
  --max_commits=5
```

## What the Script Does

1. **Clones the repository** to a temporary directory
2. **Creates commits** by:
   - Creating a new file for each commit
   - Staging the file with `git add`
   - Creating a commit with timestamp
3. **Pushes commits** to the remote repository
4. **Cleans up** temporary files

## Output Example

```
GitHub Activity Generator
Repository: git@github.com:user/myrepo.git
Max Commits: 5
Frequency: 60s
Skip Weekends: False
--------------------------------------------------
Cloning repository to /tmp/github_activity_xyz123...
Repository cloned successfully.
Created commit 1/5: activity_20260607_120000.txt
Waiting 60 seconds...
Created commit 2/5: activity_20260607_120100.txt
Waiting 60 seconds...
...
Pushing commits to remote...
All commits pushed successfully!
Cleaned up temporary directory: /tmp/github_activity_xyz123
```

## Advanced Usage

### Scripting Multiple Repositories

Create a script to generate activity across multiple repositories:

```bash
#!/bin/bash

repos=(
  "git@github.com:user/repo1.git"
  "git@github.com:user/repo2.git"
  "git@github.com:user/repo3.git"
)

for repo in "${repos[@]}"; do
  python contribute.py --repository="$repo" --max_commits=5
done
```

## Important Notes

⚠️ **Disclaimer**: This tool is intended for educational and development purposes. Use it responsibly and in compliance with:
- GitHub's Terms of Service
- Your organization's policies
- Applicable laws and regulations

## Troubleshooting

### Authentication Failures

If you get authentication errors:

1. **For SSH**: Ensure your SSH keys are registered with GitHub
   ```bash
   ssh -T git@github.com
   ```

2. **For HTTPS**: Ensure you have proper credentials configured
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"
   ```

### Permission Errors

If you get "Permission denied":
- Ensure the repository exists
- Verify you have push access to the repository
- Check that the repository URL is correct

### No Commits Created

If commits aren't appearing:
- Verify the repository URL is accessible
- Check internet connectivity
- Ensure Git is properly configured
- Review the error messages in the output

## Support

For issues or questions, please:
1. Check this documentation
2. Review the code comments
3. Open an issue on GitHub
