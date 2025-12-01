json_structure = """
{
  "experience": [{"title": "", "duration": "", "responsibilities": []}],
  "skills": {"skill_name": "", "spokenlanguages": [{"language": "", "level": ""}]},
  "education": [{"title": "", "school name": "", "grade": "", "description": ""}],
  "summary": {"description": ""},
  "projects": [{"title": "", "description": ""}]
}
"""

example_json="""
{
  "experience": [
    {
      "title": "Senior Software Engineer",
      "duration": "2019 - Present",
      "responsibilities": [
        "Led a team of 5 developers to migrate a monolithic legacy architecture to microservices using Node.js and Docker, reducing deployment time by 40%.",
        "Designed and implemented high-traffic API endpoints handling over 1M requests daily with 99.9% uptime.",
        "Mentored junior engineers through code reviews and pair programming, resulting in a 25% decrease in post-release bugs."
      ]
    },
    {
      "title": "Software Developer",
      "duration": "2016 - 2019",
      "responsibilities": [
        "Developed and maintained full-stack web applications using React and Python (Django) for a fintech client.",
        "Optimized SQL database queries, improving report generation speed by 60%.",
        "Collaborated with product managers and UX designers to implement responsive UI features, increasing user engagement by 15%."
      ]
    }
  ],
  "skills": {
    "JavaScript (ES6+), Python, Java, SQL, TypeScript",
    "React, Node.js, Django, Spring Boot, Express",
    "AWS (EC2, Lambda), Docker, Kubernetes, Git, Jenkins (CI/CD)",
    "Agile/Scrum, Technical Leadership, System Design, Problem Solving"
    "spokenlanguages": [
        {
        "language": "English",
        "level": "Native/Bilingual"
        },
        {
        "language": "Spanish",
        "level": "Professional Working Proficiency"
        },
        {
        "language": "German",
        "level": "Basic"
        }
    ],  
  },
  "education": [
    {
      "title": "M.S. in Computer Science",
      "school name": "University of Technology",
      "grade": "3.8 GPA",
      "description": "Specialized in Distributed Systems and Cloud Computing. Thesis on 'Optimizing Serverless Architecture Performance'."
    },
    {
      "title": "B.S. in Software Engineering",
      "school name": "State University",
      "grade": "Summa Cum Laude",
      "description": "Dean's List all semesters. President of the ACM Student Chapter."
    }
  ],
  "summary": {
    "description": "Results-oriented Senior Software Engineer with 7+ years of experience in full-stack development and cloud architecture. Proven track record of delivering scalable solutions and optimizing system performance in fast-paced Agile environments. Adept at translating complex business requirements into robust technical solutions and leading cross-functional teams to success."
  },
  "projects": [
    {
      "title": "E-Commerce Recommendation Engine",
      "description": "Built a real-time product recommendation system using Python and TensorFlow, which increased cross-selling revenue by 20% in the first quarter."
    },
    {
      "title": "Secure Client Portal",
      "description": "Architected a secure, GDPR-compliant document sharing portal using React and AWS S3, serving over 10,000 active enterprise users."
    }
  ]
}
"""