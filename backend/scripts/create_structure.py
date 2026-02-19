import os

BASE_DIR = os.getcwd()

structure = {
    "app": {
        "api": {
            "v1": {
                "auth": ["router.py", "__init__.py"],
                "resume": ["router.py", "__init__.py"],
                "jd": ["router.py", "__init__.py"],
                "applications": ["router.py", "__init__.py"],
                "dashboard": ["router.py", "__init__.py"],
                "__init__.py": None,
            }
        },
        "core": [
            "config.py",
            "security.py",
            "dependencies.py",
            "exceptions.py",
            "constants.py",
        ],
        "db": {
            "repositories": [
                "user_repository.py",
                "resume_repository.py",
                "jd_repository.py",
                "application_repository.py",
            ],
            "session.py": None,
            "base.py": None,
        },
        "models": [
            "user.py",
            "resume.py",
            "jd.py",
            "application.py",
        ],
        "schemas": [
            "auth.py",
            "resume.py",
            "jd.py",
            "application.py",
            "dashboard.py",
        ],
        "services": [
            "auth_service.py",
            "resume_service.py",
            "jd_service.py",
            "application_service.py",
            "dashboard_service.py",
            "langgraph_service.py",
        ],
        "agents": [
            "orchestrator.py",
            "jd_parser_agent.py",
            "resume_matcher_agent.py",
            "mail_generator_agent.py",
        ],
        "integrations": [
            "smtp_client.py",
            "llm_provider.py",
        ],
        "utils": [
            "email_templates.py",
            "helpers.py",
        ],
        "main.py": None,
    },
    "scripts": [],
    "tests": {
        "auth": [],
        "jd": [],
        "applications": [],
    },
    "requirements.txt": None,
    ".env": None,
    "README.md": None,
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for file in content:
                file_path = os.path.join(path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        f.write("")

        elif content is None:
            if "." in name:
                with open(path, "w") as f:
                    f.write("")
            else:
                os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    create_structure(BASE_DIR, structure)
    print("JobStream-AI Backend structure created successfully.")
