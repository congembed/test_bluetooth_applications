from github import Github

def got_reviewe_approved(pull_request):
    # Fetch reviews for the pull request
    reviews = pull_request.get_reviews()

    # Filter for approved reviews
    approvers = []
    for review in reviews:
        if review.state == "APPROVED":
            approvers.append(review.user.login)

    # Remove duplicates and maintain order
    unique_list_approvers = list(dict.fromkeys(approvers))
    return unique_list_approvers

def func1():
    g = Github("")
    repo = g.get_repo("SiliconLabsSandbox/test_bluetooth_applications")
    pull_requests = repo.get_pulls(state="open")
    for pull_request in pull_requests:
        print(f"Title:",pull_request.title)
        print(f"Author: {pull_request.user.login}")
        print(f"Created at: {pull_request.created_at}")
        print(f"URL: {pull_request.html_url}")

        print(f"Head Branch: {pull_request.head.ref}")
        print(f"Reviewers: {[reviewer.login for reviewer in pull_request.requested_reviewers]}")
        print(f"Number changed Files: {pull_request.changed_files}")
        print(f"Mergeable: {pull_request.mergeable}")  # True, False, or None (if not yet determined)
        # print(f"Mergeable State: {pull_request.mergeable_state}") 

        # print(f"Status: {pull_request.state}")
        # print(f"Description: {pull_request.body}")
        # print(f"Base Branch: {pull_request.base.ref}")
        # print(f"Labels: {[label.name for label in pull_request.labels]}")
        # print(f"Milestone: {pull_request.milestone}")
        # print(f"Commits number: {pull_request.commits}")

        approvers = got_reviewe_approved(pull_request)
        # Print the list of reviewers who approved
        if approvers:
            print("Approved by:")
            for approver in approvers:
                print(f"- {approver}")
        else:
            print("No reviewers have approved the pull request yet.")

        # Get the latest commit from the pull request
        latest_commit = list(pull_request.get_commits())[-1]  # The last commit in the list
        print("Latest commit:", latest_commit)

        # Only got check status passed my Jenkins
        statuses = latest_commit.get_statuses()
        for status in statuses:
            print(f"Status Context: {status.context}")
            print(f"State: {status.state}")  # e.g., success, failure, pending
            print(f"Description: {status.description}")
            print(f"Target URL: {status.target_url}")
            print("=" * 40)  # Formatting

        print(50*"=")

func1()        
