from engines.jd_engine.jd_loader import JDLoader

text = JDLoader.load("job_description.docx")

print("=" * 80)
print("JOB DESCRIPTION")
print("=" * 80)
print(text)
print("=" * 80)