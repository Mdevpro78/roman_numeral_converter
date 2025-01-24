# Roman Numerals To Integer Convertor (FastAPI Version)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Algorithm Explaination](#algorithm)
- [Tasks](#tasks)
- [Git Convention](#git)

## About

This Project is a web API to convert the roman numerals to integer number through REST API implemented by **FastAPI**

## Getting Started

These instructions will help you run the project on your local machine using Docker Compose.

### Prerequisites

1. Docker and Docker Compose

### Installing

use the following docker compose command to mange the app.

#### Environment Setup

To run the app:

- Description: Starts the application using Docker Compose.
- Command: `docker compose -f docker-compose.yaml up -d`

#### Build Commands

To build the docker image of app:

- Description: Builds the Docker images without using cache.
- Command: `docker compose -f docker-compose.yaml build --no-cache`

To remove the built image of app :

- Description: Removes the latest Docker image for the Roman Converter.
- Command: `docker image rm roman-conveter:latest`

#### Docker Management

To stop app:

- Description: Stops and removes containers, networks, volumes, and images created by `up`.
- Command: `docker compose -f docker-compose.yaml down -v`

To show the app container log:

- Description: Follows the logs of the running containers.
- Command: `docker compose -f docker-compose.yaml logs -f`

To show status of app contianer:

- Description: Lists all containers, including stopped ones.
- Command: `docker compose -f docker-compose.yaml ps -a`

## Usage `<a name = "usage"></a>`

### App Execution Flow

1. create .env file

```bash
cp env-example .env
```

2. build app image:

```bash
docker compose -f docker-compose.yaml build --no-cache
```

3. run app container:

```bash
docker compose -f docker-compose.yaml up -d
```

#### URL paths

convert endpoint

```bash
http://localhost:8080/api/v1/convert
```

swagger endpoint

```bash
http://localhost:8080/docs
```

redoc endpoint

```bash
http://localhost:8080/redoc
```

### Test Execution Flow

1. run docker-compose.test.yaml:
   ```bash
   docker compose -f docker-compose.yaml -f docker-compose.test.yaml up -d
   ```
2. run test script:

```bash
docker compose -f docker-compose.yaml -f docker-compose.test.yaml exec -it backend sh -c "dos2unix /app/scripts/run_tests.sh && /app/scripts/run_tests.sh"
```

on linux use `sudo` prefix for previous commands

# Project Structure Documentation

```bash
.
|-- docker
|   `-- Dockerfile                 # Specifies the environment to build a Docker image for the application.
|-- docs
|   `-- images
|       |-- flowchart.png          # A PNG image of a flowchart illustrating project structure or logic.
|       `-- flowchart.svg          # An SVG version of the flowchart for scaling purposes.
|   `-- openapi
|       |-- openapi.yaml        # An OpenAPI specification file defining API endpoints and their responses.
|-- scripts
|   `-- run_tests.sh               # A shell script to execute the test suite for the project.
|-- src
|   |-- conversion
|   |   |-- __init__.py            # Marks the directory as a Python package; initializes the package.
|   |   |-- dtos.py                # Contains Data Transfer Objects (DTOs) used in the application.
|   |   |-- exceptions.py          # Defines exceptions used in the conversion process.
|   |   |-- routers.py             # Defines API endpoint routes related to conversion functionality.
|   |   |-- services.py            # Contains business logic and services for the conversion module.
|   |   `-- value_objects.py       # Defines value objects, encapsulating domain-specific concepts.
|   `-- main.py                    # Main entry point of the application.
`-- tests
    |-- conversion
    |   |-- __init__.py            # Marks the directory as a Python package for test discovery.
    |   `-- test_convert_endpoint.py  # Contains unit tests for conversion API endpoints.
    `-- __init__.py                # Marks the directory as a Python package for test discovery.
|-- Makefile                       # Automates tasks and builds using make commands.
|-- README.md                      # Provides an overview of the project, setup instructions, and documentation.
|-- docker-compose.test.yaml       # Configuration for setting up a Docker environment for testing.
|-- docker-compose.yaml            # Configuration for setting up the main Docker environment.
|-- env-example                    # Example of environment variable settings; template for actual `.env` file.
|-- pyproject.toml                 # Configuration for Python project management and dependencies.
|-- requirements-dev.lock          # Locked versions of development dependencies for reproducibility.
|-- requirements.lock              # Locked versions of production dependencies for reproducibility.
|-- ruff.toml                      # Configuration for Ruff, a linting tool to enforce code quality.
```

## Algorithm Explaination

### Flow Chart

![flowchart](docs/images/flowchart.png)

code related to this flow are located in the following path:

```bash
src/conversion/value_objects.py (Validations) and src/conversion/services.py (Conversion)
```

#### Flow Explanation:

1. **Start**: The process begins with receiving the Roman numeral string as input.
2. **Validation**: The input is validated:
   - First, check if the input is a string (`Is input a string?`).
   - Then, ensure all characters are valid Roman numerals (`Are all characters valid Roman numerals?`).
3. **Conversion**: The valid Roman numeral string is mapped to integer values.
4. **Comparison and Summation**:
   - The current and next integer values are compared using the subtraction rule.
   - The final sum is calculated.
5. **Result**: The integer value is returned as the result.

#### Error Handling:

- If the input is not a string, a `TypeError` is raised.
- If the input contains invalid Roman numeral characters, a `ValueError` is raised.

## Tasks getting done `<a name = "tasks"></a>`

* [X] create project structure
* [X] install packages
* [X] conversion project
* [X] conversion service test
* [X] conversion api test
* [X] refactor project
* [X] readme doc
* [X] docker file
* [X] docker compoes
* [X] makefile commands
* [X] create github repository
* [X] ruff and pre-commit (Optional)

## Git Conventions `<a name = "git"></a>`

"Conventional Commits" guidelines:

Format: Each commit message should consist of three parts: a type, a scope, and a subject, separated by colons.

```git
<type>(<scope>): <subject>
```

***Type* **: The type describes the kind of change that was made. It should be one of the following:

- *feat*: A new feature
- *fix*: A bug fix
- *docs*: Documentation changes
- *style*: Changes to formatting or whitespace, no code changes
- *refactor*: Code refactor without any feature or bug fix
- *test*: Adding or updating tests
- *chore*: Updating build tasks, package manager configs, etc.
- *ops*: affect operational components like infrastructure, deployment, backup, recovery, ...

***Scope*** (optional) : The scope provides a hint at what part of the codebase the change affected. It's often omitted if the change is small or affects multiple parts of the codebase.

***Subject*** : The subject is a brief description of the change, written in the imperative mood (e.g. "Add" instead of "Added").

## GitFlow Workflow Conventions for FastAPI Project

### Branching Model

#### Main Branches

- **main**:
  - Contains the production-ready state of the codebase.
  - **No direct commits**; only merges from `release` or `hotfix` branches.
  - Tagged with version numbers for releases.

- **develop**:
  - The integration branch for features. It contains the latest development changes.
  - Reflects the next release version.

#### Supporting Branches

- **feature/**:
  - Naming convention: `feature/feature-name`
  - Use for developing new features or enhancements.
  - Branch off from: `develop`
  - Merge back into: `develop`

- **release/**:
  - Naming convention: `release/version-number` (e.g., `release/0.1.0`)
  - Used for release preparation. Allows for minor bug fixes and meta-data preparation for release.
  - Branch off from: `develop`
  - Merge back into: `main` and `develop`

- **hotfix/**:
  - Naming convention: `hotfix/fix-description` (e.g., `hotfix/fix-login-issue`)
  - For quick fixes on production releases.
  - Branch off from: `main`
  - Merge back into: `main` and `develop`

### Workflow Steps

#### Starting a New Feature

```bash
git checkout -b feature/my-new-feature develop
```

- Develop the feature, commit changes with meaningful messages.
- Push the feature branch to the remote repository if collaboration is needed.

#### Completing a Feature

```bash
git checkout develop
git merge --no-ff feature/my-new-feature
git branch -d feature/my-new-feature
git push origin develop
```

#### Preparing a Release

```bash
git checkout -b release/0.1.0 develop
```

- Update documentation, version numbers, and make any necessary tweaks.
- Once ready, merge into `main` and `develop`.

#### Finishing a Release

```bash
git checkout main
git merge --no-ff release/0.1.0
git tag -a v0.1.0 -m "Version 0.1.0"
git checkout develop
git merge --no-ff release/0.1.0
git branch -d release/0.1.0
git push origin main develop --tags
```

#### Hotfix Workflow

```bash
git checkout -b hotfix/issue-fix main
```

- Fix the issue, commit, then:

```bash
git checkout main
git merge --no-ff hotfix/issue-fix
git checkout develop
git merge --no-ff hotfix/issue-fix
git branch -d hotfix/issue-fix
git push origin main develop
```

### General Conventions

- **Commit Messages**: Should be descriptive. Use present tense ("Add feature" not "Added feature").
- **Pull Requests**: Use for merging features into `develop` for code review, even if working alone.
- **Testing**: Ensure all tests pass before merging into `develop` or `main`.
- **Documentation**: Update relevant documentation with each feature or change.

### CI/CD

- **Continuous Integration**: Should run on pushes to `develop` and `main` to ensure code quality.
- **Continuous Deployment**: Automate deployment from `main` branch to production after successful CI checks.
