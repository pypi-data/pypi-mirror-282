
# Breadslicer

Breadslicer is a python project template engine. Which can be programmed with a
set of function and methods and overloading classes.


## Opinionated python project
Breadslicer comes with the build in `opinionated` template.
This template will make a best-effort in creating a well thought-out development
environment for python programming. It gets tiresome after some years to setup
these skeleton projects from the scratch, so this is a solution to this issue.

For different targets(Project types) this engine can create configurations for
vscode, together with devcontainers, a gitlab ci pipeline, docker files to be
used for deployment, and release packages for python package registries. It will
install and force exercise of linters, formatters and type checkers.

For the gitlab ci pipelines to work properly it is expected that they are run as
merge requests. For the CI there will be a focus on having a minimal storage
footprint without sacrifice significant speed of execution. It will expect to
have access to gitlab runners and a 
[kubernetes cluster](https://docs.gitlab.com/ee/user/clusters/agent/install/index.html).


## Getting started

The template will check if its dependencies are met, and will abort if a
required dependency is missing. The following dependencies are required:

* [python-poetry](https://python-poetry.org/)
* [GNU make](https://www.gnu.org/software/make/manual/make.html)
* [git](https://git-scm.com/)

The following dependencies are optional but recommended:

* [direnv](https://direnv.net/docs/installation.html#from-system-packages)

### Install breadslicer

The recommended way to install breadslicer is by using [`pipx`](https://pipx.pypa.io/stable/):

```
> pipx install breadslicer
```

```
> breadslicer
```

The template will prompt for different project setups. First it will prompt for
author name and project name ect.

Then it will prompt for project type where the following choices are available.

* Command-line application
* Django Service
* Flask Service
* Library

When relevant, the layout can be chosen between flat and source. This
references to directory layout of the project, see
[a guide to python project structure](https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95).
The difference between library and command-line application is that the cmd-line
app contains a main file and will build package that installs a binary.

### Direnv
Direnv is a small utility that can be used to automatically source the virtual
environment. It is optional but it is will make your life easier. After
installation, the following snippet should be added to you shell initialization,
such as `.bashrc` or `.zsh`:

```
realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}
layout_python-venv() {
    local python=${1:-python3}
    [[ $# -gt 0 ]] && shift
    unset PYTHONHOME
    if [[ -n $VIRTUAL_ENV ]]; then
        VIRTUAL_ENV=$(realpath "${VIRTUAL_ENV}")
    else
        local python_version
        python_version=$("$python" -c "import platform; print(platform.python_version())")
        if [[ -z $python_version ]]; then
            log_error "Could not detect Python version"
            return 1
        fi
        VIRTUAL_ENV=$PWD/.env
    fi
    export VIRTUAL_ENV
    if [[ ! -d $VIRTUAL_ENV ]]; then
        log_error "no venv found; Searching for $VIRTUAL_ENV"
        unset VIRTUAL_ENV
    else
        PATH="${VIRTUAL_ENV}/bin:${PATH}"
        export PATH
    fi
}
```

Afterwards when entering a directory containing a `.envrc` file, direnv will
prompt to allow or disallow the .envrc to run. The `.envrc` file will need to contain:

```
export VIRTUAL_ENV=.venv
layout python-venv
```


## Makefile
The template will provide a Makefile that is tailored to the project type. The
Makefile contains commands such as build, test, deploy, release. The are
specific commands that are only relevant for specific project types, others are
general for python projects. This is the list of general commands:

* **build-docker**    Build docker image from Dockerfile
* **check:**          Run poetry check
* **clean:**          Remove virtual python environment
* **default:**        Invoke: 'make help'
* **docs:**           Make docs
* **format:**         Run linters and auto formatters.
* **freeze:**         Create requirements.txt of non-dev packages
* **help:**           Print the description of every target
* **help-verbose:**   Print the verbose description of every target
* **install:**        Run poetry to install all none-dev packages.
* **install-all:**    Run poetry to install all packages including dev packages
* **tests:**          Run tests via pytest
* **verify:**         Run linters and verify project integrity.


## Project types
Different types of python projects will have different directory layouts and
make commands available. E.g. a django project will have little use in releasing
the code as a python package, so it won't contain a `make release` command. Vice
versa a library project would have little use for a `make deploy` command, that
deploys to a kubernetes environment.

### Command-line applications
This project type is used when you need a main file that can be used as a
command line application. There are two of these types of projects, the
source/src directory layout and flat layout. Both are acceptable layouts and can
be used for different use cases. The flat layout will just create a directory
named the same as the project, this will a simple layout that best accommodates
a single application per repository.

The source layout will create a `src` directory in the root of the project and
inside the `src` there will be a directory with the same name as the project.
This layout type is more flexible and can be used if there is a chance the
repository should contain more than one application or multiple libraries.

The command-line applications project type has the following extra Makefile
commands:

* **build:**        Build python packages from project
* **release:**      Release python packages defined in pyproject.toml to package repository
* **run:**          Run application, postfix with ARGS="..." for cli arguments.

### Python library packages
The python library project type is very similar to the command-line, with the
exception that there is no main file and that it will not create a script to be
installed on the system. It does not have a `make run` command, but has the following:

* **build:**        Build python packages from project
* **release:**      Release python packages defined in pyproject.toml to package repository

### Django service
The django project will install the newest version of django and create a
project using the django-admin command tool. It will install django typing
packages, together with django rest frame work. If these packages are not desired they
can be removed by running `poetry remove <package_name>` inside the virtual
environment.

The django project Makefile contains the following extra commands:

* **collectstatic:** Run database migration through django manage.py
* **deploy:**        Deploy project with helm 
* **migrate:**       Run database migration through django manage.py

### Flask service
The ...

## VSCode integration
The new project will have integrations depending on the project type. E.g. when
the `Run->Build Task` is run in the django project that equals the `./manage.py
runserver` command. For command-line applications this executes the `main.py`
file. In general the integration will provide debugging enabled, and `pytest`
integration enabled.

The configuration does not automatically install the plugins for vs code that
gives the best experience. It does however provide these as recommendations
under the `Extensions` vscode menu.

## Docker
The template will compile a Dockerfile that defines a container used for the CI
environment. It relies on docker multi-stage builds to control what environment
is used in what context.

## CI/CD
The template will prompt for installation of git hooks and if the project should
use gitlab or github ci setup. Atlassians bitbucket is not supported and there
is no plan for it to be supported in the near future. Also the github is not
implemented yet.

### Gitlab CI
For the pipeline to function correctly, it is required to use [gitlab merge
requests](https://docs.gitlab.com/ee/user/project/merge_requests/). It uses
rules depending on merge requests to detect changes in python and docker
requirements. So to limit rebuild the ci image version only when it is required.

The pipeline is divided into the following stages:

* **Build:** In a merge request this stage will build the ci image if its
  necessary, the job will detect if any dependency changes have happened. If
  there is a package to deploy this stage will build it when the main branch is
  updated. If a container should be deployed this stage will build it when the
  main branch is updated.
* **Test:** This stage will run tests and linting. It will generally use the ci docker
  image created previously in the build stage.
* **Deploy:** This stage will deploy to various kubernetes environments if this
  is applicable by project type.
* **Release:** This stage will release packages to python package registries if
  applicable by project type.
* **Pages:** This stage is specific to gitlab and is used to publish documentation.


### Github Actions
TODO: Implement github actions as replacement for gitlab

### Feature wishlist

**A more comprehensive integration with gitlab.** 
* Implement review applications through dynamic environments.
* Implement manual and incremental rollout
* Use gitlab releases, together with semantic versioning
* Make poetry an optional dependency and add multiple build options such as
  setuptools.
