import os
from datetime import datetime

def generate_post():
    title = "test-post"
    date = datetime.now().strftime("%Y-%m-%d")

    filename = f"posts/{date}-{title}.md"

    content = f"""# Test Post

Generated at: {datetime.now()}

This is automated content.
"""

    return filename, content


def save_file(filename, content):
    os.makedirs("posts", exist_ok=True)

    with open(filename, "w") as f:
        f.write(content)


def git_push(title):
    os.system("git add .")
    os.system(f'git commit -m "add {title}"')
    os.system("git push")


def main():
    filename, content = generate_post()
    save_file(filename, content)
    git_push("test-post")


if __name__ == "__main__":
    main()