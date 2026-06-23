"""
Task 3: Task Automation with Python Scripts
Covers all 3 automation ideas:
  1. Move all .jpg files from a folder to a new folder
  2. Extract all email addresses from a .txt file and save them
  3. Scrape the title of a fixed webpage and save it
"""

import os
import re
import shutil
import requests


# ─────────────────────────────────────────────
# TASK 3A: Move all .jpg files to a new folder
# ─────────────────────────────────────────────
def move_jpg_files(source_folder="sample_images", destination_folder="moved_images"):
    """
    Moves all .jpg files from source_folder to destination_folder.
    Creates destination_folder if it doesn't exist.
    """
    print("\n" + "=" * 50)
    print("  TASK 3A: Move .jpg Files")
    print("=" * 50)

    # Create source folder with dummy .jpg files for demo
    os.makedirs(source_folder, exist_ok=True)
    for i in range(1, 4):
        open(os.path.join(source_folder, f"photo_{i}.jpg"), "w").close()
    open(os.path.join(source_folder, "document.pdf"), "w").close()  # non-jpg file
    open(os.path.join(source_folder, "notes.txt"), "w").close()     # non-jpg file
    print(f"📁 Source folder '{source_folder}' created with demo files.")

    # Create destination folder
    os.makedirs(destination_folder, exist_ok=True)

    # Find and move .jpg files
    moved = []
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            src = os.path.join(source_folder, filename)
            dst = os.path.join(destination_folder, filename)
            shutil.move(src, dst)
            moved.append(filename)
            print(f"  ✅ Moved: {filename}")

    if moved:
        print(f"\n✔ Total {len(moved)} .jpg file(s) moved to '{destination_folder}'.")
    else:
        print("⚠️  No .jpg files found in source folder.")


# ─────────────────────────────────────────────────────────────
# TASK 3B: Extract email addresses from a .txt file
# ─────────────────────────────────────────────────────────────
def extract_emails(input_file="emails_input.txt", output_file="extracted_emails.txt"):
    """
    Reads input_file, finds all email addresses using regex,
    and saves unique emails to output_file.
    """
    print("\n" + "=" * 50)
    print("  TASK 3B: Extract Email Addresses")
    print("=" * 50)

    # Create a sample input file for demo
    sample_text = """
    Hello team,
    Please contact john.doe@example.com or jane_smith@gmail.com for details.
    You can also reach out to support@company.org and admin@website.net.
    Invalid addresses like @nouser.com or noatsign.com are ignored.
    Duplicate: john.doe@example.com should appear only once.
    For billing, use billing@shop.co.uk or payments@store.io.
    """
    with open(input_file, "w") as f:
        f.write(sample_text)
    print(f"📄 Sample input file '{input_file}' created.")

    # Read the file
    with open(input_file, "r") as f:
        content = f.read()

    # Regex pattern to match email addresses
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails_found = re.findall(email_pattern, content)

    # Remove duplicates while preserving order
    unique_emails = list(dict.fromkeys(emails_found))

    # Save to output file
    with open(output_file, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"\n  Emails found ({len(unique_emails)}):")
    for email in unique_emails:
        print(f"    📧 {email}")
    print(f"\n✔ Emails saved to '{output_file}'.")


# ─────────────────────────────────────────────────────────────
# TASK 3C: Scrape the title of a webpage and save it
# ─────────────────────────────────────────────────────────────
def scrape_webpage_title(url="https://www.python.org", output_file="webpage_title.txt"):
    """
    Fetches the given URL and extracts the <title> tag content.
    Saves the title to output_file.
    """
    print("\n" + "=" * 50)
    print("  TASK 3C: Scrape Webpage Title")
    print("=" * 50)
    print(f"  🌐 Fetching: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract title using regex (no external HTML parser needed)
        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            print(f"  📰 Title found: {title}")

            # Save to file
            with open(output_file, "w") as f:
                f.write(f"URL   : {url}\n")
                f.write(f"Title : {title}\n")
            print(f"\n✔ Title saved to '{output_file}'.")
        else:
            print("⚠️  No <title> tag found on the page.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching page: {e}")


# ─────────────────────────────────────────────
# Main entry point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 Starting Task 3: Task Automation with Python Scripts\n")

    move_jpg_files()
    extract_emails()
    scrape_webpage_title()

    print("\n" + "=" * 50)
    print("  ✅ All automation tasks completed!")
    print("=" * 50)
