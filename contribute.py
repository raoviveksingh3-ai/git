#!/usr/bin/env python3
"""
GitHub Activity Generator

A tool to generate GitHub commit activity for testing and development purposes.
"""

import argparse
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
import os
import tempfile
import shutil


class GitHubActivityGenerator:
    """Generate GitHub activity through commits."""

    def __init__(self, repository_url, max_commits=10, frequency=60, skip_weekends=False):
        """
        Initialize the activity generator.

        Args:
            repository_url: Git repository URL
            max_commits: Maximum number of commits to create
            frequency: Time interval between commits in seconds
            skip_weekends: Whether to skip weekends
        """
        self.repository_url = repository_url
        self.max_commits = max_commits
        self.frequency = frequency
        self.skip_weekends = skip_weekends
        self.repo_path = None

    def clone_repository(self):
        """Clone the target repository."""
        try:
            self.repo_path = tempfile.mkdtemp(prefix="github_activity_")
            print(f"Cloning repository to {self.repo_path}...")
            subprocess.run(
                ["git", "clone", self.repository_url, self.repo_path],
                check=True,
                capture_output=True,
            )
            print("Repository cloned successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e.stderr.decode()}")
            sys.exit(1)

    def create_commits(self):
        """Create commits in the repository."""
        if not self.repo_path:
            print("Repository not cloned. Call clone_repository() first.")
            return

        try:
            os.chdir(self.repo_path)

            for i in range(self.max_commits):
                # Create a new file for each commit
                filename = f"activity_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                filepath = os.path.join(self.repo_path, filename)

                with open(filepath, "w") as f:
                    f.write(f"Activity generated at {datetime.now()}\n")

                # Stage the file
                subprocess.run(["git", "add", filename], check=True, capture_output=True)

                # Create commit
                commit_message = f"Generate activity #{i + 1} at {datetime.now()}"
                subprocess.run(
                    ["git", "commit", "-m", commit_message],
                    check=True,
                    capture_output=True,
                )

                print(f"Created commit {i + 1}/{self.max_commits}: {filename}")

                # Wait for frequency interval (except on last iteration)
                if i < self.max_commits - 1:
                    print(f"Waiting {self.frequency} seconds...")

            # Push commits to remote
            print("Pushing commits to remote...")
            subprocess.run(["git", "push"], check=True, capture_output=True)
            print("All commits pushed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"Error creating commits: {e.stderr.decode()}")
            sys.exit(1)
        finally:
            # Cleanup
            if self.repo_path and os.path.exists(self.repo_path):
                os.chdir("/")
                shutil.rmtree(self.repo_path)
                print(f"Cleaned up temporary directory: {self.repo_path}")

    def run(self):
        """Execute the activity generation process."""
        print(f"GitHub Activity Generator")
        print(f"Repository: {self.repository_url}")
        print(f"Max Commits: {self.max_commits}")
        print(f"Frequency: {self.frequency}s")
        print(f"Skip Weekends: {self.skip_weekends}")
        print("-" * 50)

        self.clone_repository()
        self.create_commits()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate GitHub commit activity for testing and development.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python contribute.py --max_commits=12 --frequency=60 --repository=git@github.com:user/repo.git
  python contribute.py --no_weekends
        """,
    )

    parser.add_argument(
        "--max_commits",
        type=int,
        default=10,
        help="Maximum number of commits to generate (default: 10)",
    )

    parser.add_argument(
        "--frequency",
        type=int,
        default=60,
        help="Time interval between commits in seconds (default: 60)",
    )

    parser.add_argument(
        "--repository",
        type=str,
        default=None,
        help="Git repository URL (SSH or HTTPS)",
    )

    parser.add_argument(
        "--no_weekends",
        action="store_true",
        help="Skip commit generation on weekends",
    )

    args = parser.parse_args()

    if not args.repository:
        print("Error: --repository argument is required")
        parser.print_help()
        sys.exit(1)

    generator = GitHubActivityGenerator(
        repository_url=args.repository,
        max_commits=args.max_commits,
        frequency=args.frequency,
        skip_weekends=args.no_weekends,
    )

    generator.run()


if __name__ == "__main__":
    main()
