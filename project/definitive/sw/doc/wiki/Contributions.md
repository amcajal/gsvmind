CONTRIBUTIONS
=============
GSVmind is open to any kind of contributions, from fixes to new features, including requests.

To do so, open an issue in the Issue Tracker of the project. Remember to be polite (otherwise, it will be deleted),
and provide enough information. More details the better!

Given the scope of the project, certain degree of
freedom is allowed when summiting issues or starting pull requests. However, **coherency** is key to keep the project clean
and easy to manage. To do so, a set of general rules or recommendations are given below, that can be summarized in
"keep to try the project with the same appearance". 
To aid the user in this goal, project/def/sw/doc/templates contains a bunch of template files ready to be used for
starting new source code files, create new scripts, etc. And of course, the current project files can be used as example.

**ENHANCING THE PROJECT**
It depends on the task being performed, but usually, each contribution to the project will include this steps:
- Update in the requirements.txt document, under project/def/sw/req:
	First, requirements are updated (created, deleted, modified)	
- Update (if required) in the design documents.
- Update the tests of the project (remember, in TDD, first come a failing test!)
	Then, tests are updated (created, deleted, or modified)
- Update in the source of the project
	Then source code is developed.
- Run tests, and check everything works.
- Generate (if required) performance reports: coverage, time usage...
- Update (if required) the documentation of the project.

**COHERENCY TASKS**
Besides implementing new working functionality, there are a set of tasks that increases the overall "health" of the project.
Examples of it can be found in the very files of the application, from source code to wiki documents.
- Trace requirements to code and tests. Ensure there is no single requirement uncovered!
- Keep requirements with unique IDs.
- Try to always increase Code Coverage.
- Delete deprecated or unused functionality.


And in case of doubt, do not hesitate to ask!