
LabCrawler by [Francis Potter](https://www.linkedin.com/in/francispotter/)

**NOTE: The project has changed. We intend to rewrite everything. In the meantime, enjoy limited functionality.**

Installation
------------

Install LabCrawler using `pipx`. [Install `pipx` first if necessary.](https://pypa.github.io/pipx/#install-pipx)

```bash
pipx install labcrawler
```

Later, to upgrade to the latest version of LabCrawler:

```bash
pipx upgrade labcrawler
```

Host and token
----

LabCrawler operations require a GitLab host (such as GitLab.com) and token.

Download a [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or [group access token](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html) with API access to the group(s) and project(s) you wish to query at the correct role level for the requested operation. For best practice desktop use, store the token in a password manager such as 1Password.

LabCrawler uses the [WizLib ConfigMachine framework](https://gitlab.com/steampunk-wizard/projects/wizlib/-/blob/main/wizlib/config_machine.py?ref_type=heads), which supports several options for configuring the host and token (to be documented here).

The default host is `gitlab.com` and the default behaviour is to request the token from the user at runtime.


List Projects
-----

Lists all the projects in a group and its subgroups.

```bash
labcrawler list projects my-group
```

List Groups
-----------

Lists all the subgroups in a group and its subgroups.

```bash
labcrawler list groups my-group
```

Move projects
-------------

Transfer multiple projects between namespaces (groups/subgroups). Note [specific token requirements](https://docs.gitlab.com/ee/user/project/settings/index.html#transfer-a-project-to-another-namespace).

The list of projects to be moved comes from stdin and must use the entire path with namespace. For best practice desktop use, apply a bash pipe.

```bash
echo "my-group/my-project" | labcrawler move projects my-new-group
```

Of course, the list of project paths can come from a file.

```bash
cat "my-list-of-project-paths.txt" | labcrawler move projects my-new-group
```

Piping allows the commands to chain.

```bash
labcrawler list projects my-group | labcrawler move projects my-new-group
```

Or, edit the list before moving the projects.

```bash
labcrawler list projects my-group > tempfile.txt
emacs tempfile.txt
cat tempfile.txt | labcrawler move projects my-new-group
```


Legacy documentstion
====================

Using [Meltano](https://meltano.com/) and [Pandas](https://pandas.pydata.org/).

Examine a set of GitLab projects for usage of governance processes such as CI/CD, merge requests, merge request approvals, security scanning, and code review. This tool pulls project and group configuration and recent history data from GitLab and returns it in a CSV that can be imported to a spreadsheet.

Assumes the use of the GitLab "ultimate" paid tier, as it looks for configuration settings such as merge request approvals, which are only available at that level.

Remember, in GitLab, a "group" is like a portfolio or folder containing projects and subgroups. Currently, Labcrawler doesn't actually "crawl" - it only surveys projects that live directly in the designated groups.

Installation
------------

Install LabCrawler using `pipx`. [Install `pipx` first if necessary.](https://pypa.github.io/pipx/#install-pipx)

```
pipx install labcrawler
```

Note that LabCrawler installs its own dependencies, including Meltano, which might override the `meltano` command for an existing Meltano installation. It ought to work fine, but might contain a different version of Meltano itself.

From your GitLab instance, you will also need a [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or [group access token](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html) with API read access to the group(s) you wish to query. LabCrawler supports 2 options for token storage:

- For desktop use: Store the token in a password manager, then copy-and-paste it into LabCrawler when requested.
- For offline automated operation: Make the token available in the `'GITLAB_PRIVATE_TOKEN` environment variable using an environment manager such as a `.env` file or your CI platform's variables.


Upgrade
-------

Later, to upgrade to the latest version of LabCrawler:

```
pipx upgrade labcrawler
```

Check the release notes for the new version - it might be necessary to run `labcrawler init` again to reload the Meltano tap and/or target.

Initialization
--------------

LabCrawler maintains a "workspace" for its config file and everything required for Meltano to operate. To set up the workspace, type:

```
labcrawler init
```

The workspace should be good for the life of LabCrawler, though in rare cases a LabCrawler upgrade might require you to recreate it, so check the release notes when upgrading.

The output from the `init` command includes the location of the LabCrawler config file (`labcrawler.json`). Edit the file with the following information:

- `api_url` - URL to the root of the GitLab API, including `https://`.
- `groups` - All the groups containing projects that you wish to examine. LabCrawler will not examine subgroups, so include them too.
- `output_dir` - Directory to store the CSV files that are generated; the default is based on the OS and might be sufficient.

Meltano loading
---------------

LabCrawler loads data from the GitLab API into CSV files, which can then be examined using a spreadsheet application, independent script, or LabCrawler's built-in analyzer.

Generating the CSV files requires two phases: `melt` and `load`.

To run Meltano, issue the following command:

```
labcrawler melt
```

The CSV files generated by Meltano will contain the verbatim fields from the GitLab REST API, so refer to the [GitLab API Documentation](https://docs.gitlab.com/ee/api/api_resources.html) to understand the fields. Data loaded includes:
    - `groups`
    - `projects`
    - `branches`
    - `merge_requests`
    - `project_members`
    - `group_members`
    - `users`

CI configuration data loading
-----------------------------

To load LabCrawler-specific data, include CI configuration includes and committers, issue the following command:

```
labcrawler load
```

The `load` command includes queries specific to GitLab CI configuration files, which are not covered by the Meltano tap.

LabCrawler looks at each project's main GitLab CI configuration file. The default file is at the repo root with the name `.gitlab-ci.yml`, but the location can be overridden by the project maintainers, in which case it's read from the `ci_config_path` setting at the project level. Since `ci_config_path` is now loaded by the Meltano tap, LabCrawler uses that information to query about the correct file.

At this point, the main GitLab CI configuration file is the only file for which LabCrawler loads file-specific information.

The `load` phase loads two specific types of information:

- *includes* - Paths to other GitLab CI configuration files from the same repo that are loaded into the main CI configuration file using the `include:` key. Useful to know where all the CI configuration lives, so it can be easily inspected.
- *committers* - Names and email addresses of developers who committed the most recent change to at least one line of the main CI configuration file, as per the `git blame` command. Useful to know who has touched CI configuratoin most recently, so they can be easily questioned.

*Understanding includes*

To list the "includes", LabCrawler downloads the CI configuration file itself from the default branch, parses the YAML, and identifies the `include:` key if it exists. The idea is to help understand where more CI configuration lives inside the project.

[The `include:` key](https://docs.gitlab.com/ee/ci/yaml/includes.html) has some power, including the ability to include templates (shipped with GitLab itself) and CI configuration files from other projects and even from URLs outside of the GitLab instance. LabCrawler only lists local includes - that is, other CI configuration files in the same project that are used by the main CI configuration file.

*Understanding committers*

LabCralwer's "committers" list is based on the output from a [GitLab API call](https://docs.gitlab.com/ee/api/repository_files.html#get-file-blame-from-repository) that emulates the [`git blame`](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame) command.

Git differentiates between the author of a commit and the committer, both of which are stored by name and email address within the repo based on the developer's local configuration settings. Authors and committers are not authenticated by Git itself on the desktop.

A push to GitLab might contain one or more commits. GitLab requires authentication and authorization for every push, and records the user who made the push in the database. Optionally, a pre-receive hook can be set up to confirm that the committers (inside the repo data) are authorized users. It's also possible to require signed commits. But GitLab has no way to authenticate the committers themselves, who might have committed code offline.

So within the GitLab API, committer information comes from the Git repo itself, not from the users table. LabCrawler doesn't check other project-level configuration (such as push rules and the signed commit requirement) when reporting committer data. The discrepancy can result in surprises, such as commits by people not authorized to push to the repo, or even employees from other companies (or GitLab itself) showing up as committers.

To investigate why an unknown committer appears in the committers data, use the GitLab web UI. Navigate to the project in question, identify the CI configuration file, and click the "Blame" button. You'll be able to see exactly which lines of code were touched by each committer, and with what commit message. It's also possible to use the "History" button to see the history of all commits to the file.

Note that LabCrawler simply extracts the committers themselves from the API output, and discards the detailed information about which line each developer committed.

*TODO: Note about only loading one project's data*

Analysis
--------

LabCrawler generates simple CSV files in the output directory, which can be opened using Microsoft Excel or any other CSV application. Also, LabCrawler offers an easy-to-use analysis prompt based on `pandas`. To use the analysis:

```
labcrawler analyze
```

The above command:

1. Reads the CSV file data into Pandas DataFrames (called "raw)
2. Joins raw DataFrames into slightly-more-useful DataFrames with specific names for each datatype
3. Outputs how many rows are in each DataFrame, with the variable name for each
4. Starts a Python command-line Python interpreter for querying the resulting DataFrames using Pandas operations


``` python

# List the projects
gitlab.projects

# See what columns are available in any table
gitlab.projects.columns

# View just certain columns from a table
gitlab.projects[['name','merge_method']]

# See how many of each value are included
gitlab.projects.value_counts(['merge_method'])

# Count the total of unmerged branches
len(gitlab.branches.loc[~gitlab.branches['merged']])

# View the number of unmerged branches by project
gitlab.branches.loc[~gitlab.branches['merged']].value_counts(['project_name'])

# See who has access to a project
gitlab.project_members.query('project_name == "<project-name>"')[['user_username','access_level_name']]

# See who has access to a group
gitlab.group_members.query('group_path == "<group-path>"')[['username','access_level_name']]

# How many have each access level
gitlab.group_members.value_counts(['access_level_name'])

# Who are the owners and maintainers?
gitlab.group_members.query('group_path == "<group-path>" and access_level_name in ["Owner","Maintainer"]')[['username','access_level_name']]

# Which projects use a non-default location for CI configuration?
gitlab.projects.query("ci_config_path.notnull()")[['name','ci_config_path']]

# Which projects have CI configuration at all?
gitlab.ci_config_paths.query("main.notnull()")[['project_name']]

# Projects without any CI configuration
gitlab.ci_config_paths.query("main.isnull() and local_include.isnull()")[['project_name']]

# Local CI configuration includes
gitlab.ci_config_paths.query("local_include.notnull()")[['project_name','local_include']]

# Who has edited the main CI configuration file
gitlab.ci_config_committers[['committer_name','project_name']]

```

LabCrawler sets the `max_rows` attribute to `None` so you will see all the rows in default DataFrame output.

For prettier output, we've added a `neat()` function.

```python
>>> neat(gitlab.projects[['name_with_namespace','merge_method']])
name_with_namespace                                          merge_method
-----------------------------------------------------------  --------------
Steampunk Wizard / WizLib                                    merge
Steampunk Wizard / FileWiz                                   merge
Steampunk Wizard / LabCrawler                                merge
Steampunk Wizard / Busy                                      merge
```

Roadmap
-------

We maintain an informal roadmap of future functionality. Development of such functionality depends on contributions from the community, a generous donation, or us simply finding the time ;-).

- Put all these roadmap items into GitLab issues for visibility and sharing
- Redesign it to work within GitLab CI/CD
- Undo the hack that allows for large group lists
- Fix the bug where users are being loaded into the CSV multiple times (possible Meltano tap-gitlab fix?)
- Fix everything to use the `logger` instead of `print()`.
- Add a command (`labcrawler info`?) to get e.g. locations of config and output files.
- Load information about [external main CI configuration files](https://docs.gitlab.com/ee/ci/pipelines/settings.html#specify-a-custom-cicd-configuration-file)
- Load information about external included CI configuration files
- Load CI configuration includes recursively, so if an included CI config includes another one, it's loaded also
- Pull committer information for included and external CI configuration files
- "Crawl" through subgroups at the beginning, to get all the groups and projects within a portfolio
- Add one command to combine `crawl`, `melt`, and `load`
- Enable designation of groups and/or projects as options in the CLI
- Provide a Dockerfile for easy deployment
- Integrate with Jupyter Notebook to make querying easier
- Generate useful reports (in GitLab Pages? Conflucence?)
- Read the CI configuration and smartly explain what it includes
- Add (in reports, analysis, Jupyter, etc) clear explanations of what each field means (so users new to GitLab can understand more quickly)
- Provide a test bed for LabCrawler itself, including a GitLab instance with test groups/projects
- Contribute some or all of LabCrawler's custom queries back to tap-gitlab

Troubleshooting
---------------

If the `load` command seems to fail, try querying the GitLab API directly. The shell commands below assume that your token is already in the `GITLAB_PRIVATE_TOKEN` environment variable.

To make sure you can connect, and see the towen's user information:

``` bash
curl --request GET --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" "$GITLAB_API_URL/api/v4/personal_access_tokens/self"
```

 Here's how to look up the raw blame data using CURL. You *might* need to replace `.gitlab-ci.yml` with the actual path to the CI configuration file, and you also might need to change the `ref` to the default branch.

``` bash
curl --request GET --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" "$GITLAB_API_URL/api/v4/projects/<id>/repository/files/.gitlab-ci.yml/blame?ref=master"
```

Finally, here's a crude API-driven way to list the files and directories at the root of a project:

``` bash
curl --request GET --header "PRIVATE-TOKEN: $GITLAB_PRIVATE_TOKEN" "$GITLAB_API_URL/api/v4/projects/<id>/repository/tree?per_page=999"
```

Useful links
------------

[Meltano tutorial](https://docs.meltano.com/getting-started/)

[Meltano CLI reference](https://docs.meltano.com/reference/command-line-interface)

[tap-gitlab on GitHub](https://github.com/MeltanoLabs/tap-gitlab)

[GitLab API docs](https://docs.gitlab.com/ee/api/)

[Pandas DataFrame reference](https://pandas.pydata.org/docs/reference/frame.html)


Development
-----------

1. Make sure you have Python 3.8+ and Pip installed
2. Make a GitLab account and give it your SSH public key
3. Follow the steps below (YMMV, from memory, please update if I missed anything)

```
git clone git@gitlab.com:steampunk-wizard/projects/labcrawler.git
cd labcrawler
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/freeze.txt
```

Then to run it:

```
python -m labcrawler init
```

... and the other commands

Thoughts on adding `tap-github`:

- Add it to `meltano.yml`
- Set up required env vars in `labcrawler.json`
- Re-run `init`


