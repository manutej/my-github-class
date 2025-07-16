# My GitHub Class 🎓

A comprehensive tutorial project demonstrating GitHub Actions workflows with Python. This repository serves as a practical example of implementing CI/CD, automated code review, and changelog generation.

## 📋 Features

- **Continuous Integration**: Automated testing across multiple Python versions
- **Code Quality**: Automated linting, formatting, and type checking
- **Security Scanning**: Vulnerability detection and dependency checking
- **Automated Code Review**: Pull request analysis and feedback
- **Changelog Generation**: Automatic changelog updates based on conventional commits
- **Documentation**: Complete examples and tutorials

## 🚀 GitHub Actions Workflows

### 1. CI Pipeline (`.github/workflows/ci.yml`)
- **Triggers**: Push to main/develop, Pull requests to main
- **Features**:
  - Multi-version Python testing (3.8, 3.9, 3.10, 3.11)
  - Code formatting with Black
  - Import sorting with isort
  - Linting with flake8
  - Type checking with mypy
  - Unit testing with pytest
  - Code coverage reporting

### 2. Automated Code Review (`.github/workflows/code-review.yml`)
- **Triggers**: Pull request events
- **Features**:
  - Security scanning with Bandit
  - Vulnerability checking with Safety
  - Code quality analysis with Pylint
  - Complexity analysis with Radon
  - Automated PR comments with findings

### 3. Changelog Generation (`.github/workflows/changelog.yml`)
- **Triggers**: Push to main, Release events
- **Features**:
  - Automatic changelog generation with git-cliff
  - Conventional commit parsing
  - Release notes extraction
  - Automatic commit and push

## 🛠️ Project Structure

```
my-github-class/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── code-review.yml
│       └── changelog.yml
├── src/
│   ├── calculator.py
│   └── utils.py
├── tests/
│   ├── test_calculator.py
│   └── test_utils.py
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

## 🧪 Sample Code

The project includes example Python modules:

- **Calculator**: Basic mathematical operations with comprehensive tests
- **Utils**: Common utility functions for JSON handling, email validation, and more

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/my-github-class.git
cd my-github-class
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest tests/ -v
```

## 🔧 Development

### Code Formatting
```bash
black .
isort .
```

### Linting
```bash
flake8 .
pylint src/
```

### Type Checking
```bash
mypy .
```

### Security Scanning
```bash
bandit -r .
safety check
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all tests pass
5. Submit a pull request

The automated workflows will:
- Run comprehensive tests
- Check code quality
- Perform security scans
- Provide automated feedback

## 🏷️ Conventional Commits

This project uses conventional commits for automated changelog generation:

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Test changes
- `chore:` Maintenance tasks

## 📊 Workflows in Action

### CI Pipeline
Every push and pull request triggers:
- Multi-version Python testing
- Code quality checks
- Security scanning
- Coverage reporting

### Code Review
Pull requests receive automated analysis:
- Security vulnerability detection
- Code complexity analysis
- Quality metrics
- Automated suggestions

### Changelog
Releases automatically generate:
- Structured changelogs
- Release notes
- Version tracking

## 🎯 Learning Objectives

By exploring this repository, you'll learn:
- GitHub Actions workflow syntax
- CI/CD best practices
- Python project structure
- Automated testing strategies
- Code quality tools
- Security scanning
- Documentation automation

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Testing Best Practices](https://docs.pytest.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Code Quality Tools](https://github.com/psf/black)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Support

If you have questions or need help:
- Open an issue in this repository
- Check the GitHub Actions logs for detailed information
- Review the workflow files for configuration examples

---

*This project is designed for educational purposes to demonstrate GitHub Actions capabilities with Python projects.*