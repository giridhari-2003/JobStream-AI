<!-- Folder Str -->
JobStream-AI/
│
├── Backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth/
│   │   │       │   ├── router.py
│   │   │       │   └── __init__.py
│   │   │       │
│   │   │       ├── resume/
│   │   │       │   ├── router.py
│   │   │       │   └── __init__.py
│   │   │       │
│   │   │       ├── jd/
│   │   │       │   ├── router.py
│   │   │       │   └── __init__.py
│   │   │       │
│   │   │       ├── applications/
│   │   │       │   ├── router.py
│   │   │       │   └── __init__.py
│   │   │       │
│   │   │       ├── dashboard/
│   │   │       │   ├── router.py
│   │   │       │   └── __init__.py
│   │   │       │
│   │   │       └── __init__.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   ├── dependencies.py
│   │   │   ├── exceptions.py
│   │   │   └── constants.py
│   │   │
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   ├── base.py
│   │   │   └── repositories/
│   │   │       ├── user_repository.py
│   │   │       ├── resume_repository.py
│   │   │       ├── jd_repository.py
│   │   │       └── application_repository.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── jd.py
│   │   │   └── application.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   ├── resume.py
│   │   │   ├── jd.py
│   │   │   ├── application.py
│   │   │   └── dashboard.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── resume_service.py
│   │   │   ├── jd_service.py
│   │   │   ├── application_service.py
│   │   │   ├── dashboard_service.py
│   │   │   └── langgraph_service.py
│   │   │
│   │   ├── agents/
│   │   │   ├── orchestrator.py
│   │   │   ├── jd_parser_agent.py
│   │   │   ├── resume_matcher_agent.py
│   │   │   └── mail_generator_agent.py
│   │   │
│   │   ├── integrations/
│   │   │   ├── smtp_client.py
│   │   │   └── llm_provider.py
│   │   │
│   │   ├── utils/
│   │   │   ├── email_templates.py
│   │   │   └── helpers.py
│   │   │
│   │   └── main.py
│   │
│   ├── scripts/
│   │   └── create_structure.py
│   │
│   ├── tests/
│   │   ├── auth/
│   │   ├── jd/
│   │   └── applications/
│   │
│   ├── requirements.txt
│   ├── .env
│   └── README.md
│
├── Frontend/
│   └── (future React/Next dashboard)
│
└── docker-compose.yml   (future)
