import csv, os, sys, argparse, requests

API_BASE = "https://api.github.com"

def create_issue(session, repo, title, body=None, labels=None, assignees=None):
    url = f"{API_BASE}/repos/{repo}/issues"
    payload = {"title": title}
    if body: payload["body"] = body
    if labels: payload["labels"] = labels
    if assignees: payload["assignees"] = assignees
    r = session.post(url, json=payload)
    r.raise_for_status()
    return r.json()["html_url"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv_path", nargs="?", default="python-sprint-issues.csv")
    p.add_argument("--repo", default=os.getenv("GITHUB_REPO"))
    p.add_argument("--labels", default=os.getenv("GITHUB_LABELS", ""))
    p.add_argument("--assign", default=os.getenv("GITHUB_ASSIGNEE", ""))
    args = p.parse_args()

    token = os.getenv("GITHUB_TOKEN")
    if not token: sys.exit("ERROR: set GITHUB_TOKEN")
    if not args.repo: sys.exit('ERROR: pass --repo "owner/repo" or set GITHUB_REPO')

    labels = [x.strip() for x in args.labels.split(",") if x.strip()] or None
    assignees = [args.assign] if args.assign else None

    s = requests.Session()
    s.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "issue-bulk-create",
    })

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), 1):
            title = (row.get("Title") or "").strip()
            body  = (row.get("Body")  or "").strip()
            if not title: continue
            url = create_issue(s, args.repo, title, body=body, labels=labels, assignees=assignees)
            print(f"[{i:02d}] Created: {title} -> {url}")

if __name__ == "__main__":
    import requests  # ensure installed
    main()
