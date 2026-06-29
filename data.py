"""
Portfolio content.

Everything the site renders lives here, so you can update your portfolio by
editing plain Python data instead of touching HTML. Add a project, tweak a
metric, add a job — the template loops over these structures automatically.
"""

PROFILE = {
    "name": "Adeyemi Oluwaseyi Alao",
    "brand": ("ADEYEMI", "ALAO"),  # split for the styled dot in the logo
    "role": "AI / ML Engineer · Full-stack Developer · Educator",
    "location": "Lagos, Nigeria",
    "email": "alaooluwaseyi007@gmail.com",
    "phone_display": "+234 810 325 6001",
    "phone_link": "+2348103256001",
    "title": "Adeyemi Oluwaseyi Alao — AI/ML Engineer & Educator",
    "meta_description": (
        "Adeyemi Oluwaseyi Alao builds and deploys AI/ML systems — computer "
        "vision, NLP, and full-stack applications — and trains the next "
        "generation of engineers."
    ),
    # Hero
    "headline_pre": "I build AI systems that ",
    "headline_em": "work",
    "headline_post": " in the real world — and teach others to do the same.",
    "lede": (
        "I'm Adeyemi Oluwaseyi Alao, based in Lagos, Nigeria. I design, train, "
        "and deploy computer-vision and NLP models, ship full-stack "
        "applications around them, and mentor engineers building their first "
        "production AI."
    ),
}

# Hero metric ledger — (value, unit, label)
METRICS = [
    ("96", "%", "Peak model accuracy"),
    ("250", "+", "Learners trained"),
    ("10", "+", "Apps & models shipped"),
    ("8", "yrs", "In the tech field"),
]

ABOUT_PARAGRAPHS = [
    "I started in front-end development and IT infrastructure, moved through "
    "graphic and web design, and grew into <strong>data science, machine "
    "learning, and AI</strong>. That path means I care about the full picture "
    "— from a clean model to a clean interface a person actually wants to use.",

    "Today I work as a Data Science, AI &amp; Machine Learning Specialist, "
    "building real systems: an NLP chatbot on the OpenAI API and Hugging Face "
    "Transformers, a Vision Transformer for sign-language recognition, "
    "CNN-based emotion recognition, and a crop-disease predictor in "
    "TensorFlow. I ship the supporting apps too — expense trackers, banking "
    "systems — with Python, Streamlit, Flask, and MySQL behind them.",

    "Alongside the building, I teach. As part of Nigeria's <strong>3MTT</strong> "
    "government program I've trained 250+ learners in data science and AI, "
    "guiding hands-on, Agile-based projects from sprint planning to deployment.",
]

FOCUS_AREAS = [
    ("Computer Vision", "ViT · CNN"),
    ("Natural Language", "NLP · LLM"),
    ("Model deployment", "Streamlit"),
    ("Full-stack apps", "Flask · SQL"),
    ("Mentorship", "Agile"),
]

# Selected work. `gauge` drives the animated bar (0–100).
# `metric`/`metric_small` control the big readout number.
#
# Each project also has its own detail page at /work/<slug>. The `detail`
# block is what fills that page — edit those fields (or paste your own write-up,
# links, and image filenames) to flesh out each case study.
#
#   detail.links  -> list of {"label": ..., "url": ...}. Leave url as "#" and it
#                    renders as a muted "coming soon" chip until you add a real
#                    GitHub / live-demo URL.
#   detail.gallery-> list of image filenames placed in static/img/. Empty = none.
PROJECTS = [
    {
        "slug": "sign-language-recognition",
        "tag": "Computer Vision",
        "title": "Sign-language recognition",
        "desc": "A Vision Transformer (ViT) using transfer learning for "
                "image-based gesture classification and real-time prediction "
                "— built toward accessibility for the deaf and mute community.",
        "stack": ["ViT", "Transfer Learning", "PyTorch", "OpenCV", 'Python'],
        "metric": "96", "metric_unit": "%", "metric_small": False,
        "metric_label": "Classification accuracy", "gauge": 96,
        "detail": {
            "year": "2024",
            "role": "Model design, training & real-time deployment",
            "overview": [
                "A computer-vision system that reads hand gestures from the "
                "camera and classifies them into sign-language letters in real "
                "time — a step toward more accessible communication for the "
                "deaf and mute community.",
            ],
            "problem": "Sign language is the primary mode of communication for "
                       "many, yet most software still can't interpret it. The "
                       "goal was an accurate, real-time recognizer that runs on "
                       "an ordinary webcam.",
            "approach": [
                "Built on a Vision Transformer (ViT) backbone with transfer "
                "learning, fine-tuned on a labelled gesture dataset.",
                "Applied augmentation, normalization, and careful train/val "
                "splits to fight overfitting on the gesture classes.",
                "Wired up an OpenCV capture loop for live, frame-by-frame "
                "prediction with on-screen labels.",
            ],
            "results": [
                "Reached 96% classification accuracy on the held-out set.",
                "Runs in real time on a standard webcam feed.",
            ],
            "links": [
                {"label": "GitHub", "url": "#"},
                {"label": "Live demo", "url": "#"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "crop-disease-prediction",
        "tag": "Agriculture · ML",
        "title": "Crop-disease prediction",
        "desc": "A predictive system for early plant-disease detection, built "
                "and deployed with TensorFlow to support better, earlier "
                "decisions in agricultural applications.",
        "stack": ["TensorFlow", "CNN", "Python", 'Matplotlib', 'NumPy', 'OpenCV'],
        "metric": "90–95", "metric_unit": "%", "metric_small": False,
        "metric_label": "Model accuracy range", "gauge": 93,
        "detail": {
            "year": "2024",
            "role": "Data pipeline, model & deployment",
            "overview": [
                "An image classifier that flags plant disease from a photo of "
                "a leaf, so farmers and agronomists can act earlier and lose "
                "less of a harvest.",
            ],
            "problem": "Crop disease is often spotted too late. Early, "
                       "low-cost detection from a phone photo can mean the "
                       "difference between treating a patch and losing a field.",
            "approach": [
                "Trained a convolutional neural network in TensorFlow on a "
                "labelled crop-disease image dataset.",
                "Used preprocessing and augmentation to generalize across "
                "lighting and leaf conditions.",
                "Packaged the model behind a simple interface for quick "
                "field-side predictions.",
            ],
            "results": [
                "Achieved a 90–95% accuracy range across disease classes.",
                "Deployed as a usable prediction tool, not just a notebook.",
            ],
            "links": [
                {"label": "GitHub", "url": "#"},
                {"label": "Live demo", "url": "#"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "disease-prediction",
        "tag": "Healthcare · ML",
        "title": "Disease prediction",
        "desc": "“ML Health” — a Flask web app serving Random Forest models that "
                "predict heart-disease risk and obesity from patient health "
                "indicators, with a clean multi-page interface.",
        "stack": ["Random Forest", "Scikit-learn", "Flask", "NumPy", "Python"],
        "metric": "87", "metric_unit": "%", "metric_small": False,
        "metric_label": "Prediction accuracy", "gauge": 87,
        "detail": {
            "year": "2024",
            "role": "Model training & full-stack delivery",
            "overview": [
                "A supervised classification system that estimates the "
                "likelihood of obesity and heart disease from patient health "
                "indicators, returning a presence (1) or absence (0) prediction "
                "with a probability score.",
                "Served as a Flask web app (“ML Health”) with separate pages for "
                "heart-disease, obesity, and symptom-based prediction, each "
                "calling the model through a JSON API.",
            ],
            "problem": "Many health risks go unflagged until they're advanced. "
                       "Given a patient's medical values, the goal was a "
                       "reliable, interpretable model that surfaces disease "
                       "risk early enough to act on.",
            "approach": [
                "Chose a Random Forest classifier — it handles non-linear "
                "relationships, resists overfitting better than a single "
                "decision tree, and works well with mixed medical data.",
                "Split the dataset 80% training / 20% testing and evaluated on "
                "held-out data.",
                "Used the model's feature-importance scores to see which health "
                "indicators drive each prediction.",
                "Prediction flow: validate and format user-entered medical "
                "values, run them through the model, generate a probability, "
                "and return the result to the interface.",
            ],
            "results": [
                "Accuracy: 87%.",
                "Precision: 85%.",
                "Recall: 83%.",
                "F1-score: 84%.",
            ],
            "links": [
                {"label": "GitHub", "url": "https://github.com/yemires007/mlhealth_checker"},
                {"label": "Live demo", "url": "https://ml-health.onrender.com"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "emotion-recognition",
        "tag": "Computer Vision",
        "title": "Emotion recognition",
        "desc": "A CNN-based system for facial-expression classification, with "
                "image preprocessing, model design, training, and tuning "
                "across the full pipeline.",
        "stack": ["CNN", "Keras", "OpenCV"],
        "metric": "84", "metric_unit": "%", "metric_small": False,
        "metric_label": "Facial-expression accuracy", "gauge": 84,
        "detail": {
            "year": "2023",
            "role": "Full pipeline — preprocessing to tuning",
            "overview": [
                "A facial-expression classifier that reads emotion from a face "
                "image, covering the full pipeline from raw pixels to a tuned, "
                "evaluated model.",
            ],
            "problem": "Expression recognition is noisy — faces vary in pose, "
                       "lighting, and individual features. The challenge was a "
                       "model that stays reliable across that variation.",
            "approach": [
                "Designed and trained a CNN in Keras on a facial-expression "
                "dataset.",
                "Built the preprocessing pipeline in OpenCV: face detection, "
                "cropping, grayscale, and normalization.",
                "Tuned architecture and hyperparameters to lift validation "
                "accuracy.",
            ],
            "results": [
                "Reached 84% accuracy on facial-expression classification.",
            ],
            "links": [
                {"label": "GitHub", "url": "#"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "spam-email-detection",
        "tag": "NLP · ML",
        "title": "Spam email detection",
        "desc": "A text-classification model that separates spam from "
                "legitimate email, using NLP preprocessing and TF-IDF features "
                "to flag unwanted messages automatically.",
        "stack": ["Scikit-learn", "NLP", "TF-IDF", "Python", "Pandas"],
        "metric": "98", "metric_unit": "%", "metric_small": False,
        "metric_label": "Classification accuracy", "gauge": 98,
        "detail": {
            "year": "2023",
            "role": "Text pipeline, model & evaluation",
            "overview": [
                "A supervised classifier that reads an email's text and labels "
                "it spam or legitimate (ham), turning raw messages into a clean "
                "automatic filter.",
            ],
            "problem": "Spam clutters inboxes and carries real phishing and "
                       "malware risk. The goal was an accurate, automatic "
                       "filter that catches unwanted mail without burying the "
                       "messages that matter.",
            "approach": [
                "Built an NLP preprocessing pipeline — cleaning, tokenization, "
                "and stop-word removal — to normalize raw email text.",
                "Converted text to numerical features with TF-IDF "
                "vectorization.",
                "Trained and tuned a classifier on a labelled spam/ham dataset, "
                "evaluating on a held-out split.",
            ],
            "results": [
                "Reached ~98% classification accuracy on the test set.",
                "Strong precision and recall on the spam class — few false "
                "alarms on legitimate mail.",
            ],
            "links": [
                {"label": "GitHub", "url": "#"},
                {"label": "Live demo", "url": "#"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "ai-chatbot",
        "tag": "NLP · LLM",
        "title": "AI chatbot",
        "desc": "A conversational assistant built on Natural Language "
                "Processing, integrating the OpenAI API and Hugging Face "
                "Transformers, served through a Streamlit interface for "
                "low-latency, real-time interaction.",
        "stack": ["NLP", "OpenAI API", "Transformers", "Streamlit"],
        "metric": "Real-time", "metric_unit": "", "metric_small": True,
        "metric_label": "Low-latency responses", "gauge": 100,
        "detail": {
            "year": "2024",
            "role": "NLP integration & app delivery",
            "overview": [
                "A conversational assistant that answers in natural language, "
                "combining the OpenAI API with Hugging Face Transformers behind "
                "a clean Streamlit chat interface.",
            ],
            "problem": "Users want quick, natural answers — not forms and menus. "
                       "The aim was a responsive assistant that feels like a "
                       "conversation, served through an interface anyone can use.",
            "approach": [
                "Integrated the OpenAI API for generation and Hugging Face "
                "Transformers for NLP tasks.",
                "Built a Streamlit chat UI for low-latency, real-time "
                "back-and-forth.",
                "Managed prompts and conversation state for coherent multi-turn "
                "replies.",
            ],
            "results": [
                "Delivers real-time, low-latency responses in a live chat UI.",
            ],
            "links": [
                {"label": "GitHub", "url": "#"},
                {"label": "Live demo", "url": "#"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "expense-tracker",
        "tag": "Full-stack",
        "title": "Expense tracker",
        "desc": "SpendWise — a web app for recording, managing, and analyzing "
                "expenses: full CRUD, user accounts, month/category filtering, "
                "and spending analytics, built in Flask with a SQLite backend.",
        "stack": ["Flask", "SQLite", "Jinja", "Werkzeug Auth", "Python", 'HTML', 'CSS', 'JavaScript'],
        "metric": "Deployed", "metric_unit": "", "metric_small": True,
        "metric_label": "CRUD + auth + analytics", "gauge": 100,
        "detail": {
            "year": "2023 · rebuilt 2026",
            "role": "Full-stack — backend, data model & UI",
            "overview": [
                "A personal expense tracker (“SpendWise”) for recording, "
                "managing, and analyzing spending — full create-read-update-"
                "delete, per-user accounts, filtering, and analytics.",
                "Rebuilt as a Flask web app with hashed passwords, sessions, and "
                "CSRF-protected forms, backed by SQLite.",
            ],
            "problem": "Spreadsheets fall apart for ongoing expense tracking. "
                       "The goal was a proper app: accounts, persistent data, "
                       "and a clear view of where the money goes.",
            "approach": [
                "Built full CRUD over expenses (amount, category, note, date) "
                "scoped per user, with ownership checks on every edit/delete.",
                "Added month and category filtering, plus analytics — totals, "
                "average per month, and breakdowns by category and month.",
                "Authenticated users with Werkzeug-hashed passwords and "
                "server-side sessions.",
            ],
            "results": [
                "Working CRUD with per-user data isolation and persistence.",
                "Spending analytics by category and month, rendered without a "
                "charting library.",
            ],
            "links": [
                {"label": "GitHub", "url": "https://github.com/yemires007/spendwise"},
                {"label": "Live demo", "url": "https://spendwise-fvok.onrender.com"},
            ],
            "gallery": [],
        },
    },
    {
        "slug": "banking-application",
        "tag": "Full-stack",
        "title": "Banking application",
        "desc": "A multi-bank web banking app — register, log in, transfer "
                "across banks, buy airtime and data, and track every "
                "transaction. Built in Flask with hashed PINs and a relational "
                "data model.",
        "stack": ["Flask", "SQLite", "Jinja", "Werkzeug Auth", "Python", 'HTML', 'CSS', 'JavaScript'],
        "metric": "Secure", "metric_unit": "", "metric_small": True,
        "metric_label": "Auth + transactions", "gauge": 100,
        "detail": {
            "year": "2023 · rebuilt 2026",
            "role": "Full-stack — backend, data model & UI",
            "overview": [
                "A multi-bank banking web app covering registration, secure "
                "sign-in, money transfer within and across banks, airtime and "
                "data purchase, deposits, and a running transaction history.",
                "Originally a command-line Python/MySQL project, rebuilt as a "
                "Flask web app with hashed PINs, sessions, and CSRF-protected "
                "forms.",
            ],
            "problem": "Money software has zero tolerance for sloppiness. The "
                       "focus was secure authentication and transaction handling "
                       "that keeps account state correct and consistent.",
            "approach": [
                "Identify accounts by a unique account number; verify with a "
                "PIN hashed via Werkzeug (never stored in plain text).",
                "Collapsed three duplicated bank code paths into one accounts "
                "table with a bank column, plus a transactions ledger.",
                "Handle transfers, airtime, data and deposits as balance "
                "operations with validation and a recorded history.",
            ],
            "results": [
                "Secure authentication with hashed PINs and session management.",
                "Working cross-bank transfers, airtime/data purchase, and a "
                "live transaction history.",
            ],
            "links": [
                {"label": "GitHub", "url": "https://github.com/yemires007/naijabank"},
                {"label": "Live demo", "url": "https://yemires.pythonanywhere.com"},
            ],
            "gallery": [],
        },
    },
]

EXPERIENCE = [
    {
        "when": "2024 — Now", "place": "SQI College of ICT<br>Ibadan, Nigeria",
        "role": "Data Science, AI &amp; ML Specialist",
        "org": "SQI College of ICT · 3MTT Program",
        "points": [
            "Build and deploy CV/NLP systems: ViT sign-language recognition, "
            "CNN emotion recognition, NLP chatbot, crop-disease prediction.",
            "Mentored 50+ students with an 85% project-completion rate; 90% "
            "presented functional, portfolio-ready systems.",
            "Lead hands-on, Agile/Scrum projects — sprint planning, task "
            "allocation, iterative delivery.",
        ],
    },
    {
        "when": "2021 — 2024",
        "place": "Allpac Technology<br>St. Louis, Missouri, USA",
        "role": "Graphic &amp; Web Designer", "org": "Allpac Technology",
        "points": [
            "Revamped the company website, driving a 95% increase in user "
            "engagement and time on site.",
            "Designed brand assets, logos, and layouts across web, mobile, and "
            "campaign channels.",
            "Led UX/UI work that sharpened navigation and overall engagement.",
        ],
    },
    {
        "when": "2020 — 2021", "place": "SQI College of ICT<br>Ibadan, Nigeria",
        "role": "Python Instructor", "org": "SQI College of ICT",
        "points": [
            "Taught Python from beginner to advanced; improved student pass "
            "rate by 30% with project-based learning.",
            "Trained 200+ students, with 80% reporting increased confidence in "
            "their Python skills.",
            "Ran workshops and coding bootcamps for intensive, real-world "
            "skill-building.",
        ],
    },
    {
        "when": "2018 — 2019", "place": "Julifaith Nig. Ltd<br>Ibadan, Nigeria",
        "role": "Office Assistant", "org": "Julifaith Nig. Limited",
        "points": [
            "Streamlined Excel data-entry processes, cutting processing time "
            "by 30%.",
            "Produced presentations and documents that lifted client "
            "engagement in meetings.",
        ],
    },
    {
        "when": "2017 — 2018",
        "place": "Xircuitron Technologies<br>Iwo, Nigeria",
        "role": "Front-End Developer", "org": "Xircuitron Technologies Ltd",
        "points": [
            "Built and launched 10+ responsive websites with clean, "
            "maintainable HTML/CSS.",
            "Worked across design and back-end teams on accessibility, SEO, "
            "and performance.",
        ],
    },
    {
        "when": "2016", "place": "Bowen University<br>Iwo, Nigeria",
        "role": "Industrial Trainee — IT", "org": "Bowen University",
        "points": [
            "Installed and maintained 15+ hardware components across campus IT "
            "infrastructure.",
            "Set up and configured systems, servers, and network equipment "
            "with the IT team.",
        ],
    },
]

SKILLS = [
    ("Programming & Scripting", ["Python", "SQL", "JavaScript", "HTML", "CSS"]),
    ("ML & Deep Learning",
     ["TensorFlow", "PyTorch", "Keras", "CNNs", "RNNs", "Transformers",
      "Scikit-learn", "XGBoost"]),
    ("Computer Vision & NLP",
     ["OpenCV", "Hugging Face", "OpenAI API", "Image Processing",
      "Text Processing"]),
    ("Web & App Development", ["Flask", "Streamlit", "Frontend Integration"]),
    ("Data & Visualization",
     ["Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Power BI",
      "Excel"]),
    ("Databases & Cloud",
     ["MySQL", "PostgreSQL", "SQLite", "Google Cloud (GCP)"]),
    ("Tooling & Collaboration",
     ["Git", "GitHub", "Docker", "Linux", "Jupyter", "Agile / Scrum"]),
    ("Professional",
     ["Problem Solving", "Leadership", "Project Management", "Mentorship",
      "Documentation"]),
]

EDUCATION = [
    ("2023", "B.Tech, Industrial Mathematics",
     "Federal University of Technology, Akure (FUTA)"),
    ("2017", "National Diploma, Computer Science",
     "Federal Polytechnic Ede, Osun State"),
]

CERTIFICATIONS = [
    ("2023", "Applied Data Science Lab", "WorldQuant University"),
    ("2019 · 2023", "Basic Life Support (BLS)", "American Heart Association"),
]
