from github import Github


class GithubFilteredChanges:
    """
    Construct a GithubFilteredChanges
    :param repo: GitHub repository
    :param path: path of interest in which to track git changes
    :param hierarchy: file path hierarchy of interest e.g /home/bobo/test.yaml hierarchy 1 will collect the bobo name
    :param organization: the GitHub organization
    :param token = token: GitHub token
    :param commit = commit: the commit to track
    """
    def __init__(self, repo: str, path: str, hierarchy: int, organization: str, token: str, commit: str):
        self.repo = repo
        self.path = path
        self.hierarchy = hierarchy
        self.organization = organization
        self.token = token
        self.commit = commit

    @property
    def session(self):
        return Github(self.token).get_organization(self.organization).get_repo(self.repo)

    def get_changed_files(self):
        changed_files = []
        for change in self.session.get_commit(self.commit).files:
            if change.status != 'removed' and self.path in change.filename:
                changed_files.append(change.filename.split('/')[self.hierarchy])
        return set(changed_files)

    def get_github_session(self):
        return Github(self.token).get_organization(self.organization).get_repo(self.repo)
