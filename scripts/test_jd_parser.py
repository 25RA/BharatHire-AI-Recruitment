from pprint import pprint

from engines.jd_engine.jd_loader import JDLoader
from engines.jd_engine.jd_parser import JDParser

text = JDLoader.load("job_description.docx")

parser = JDParser(text)

jd = parser.parse()

print()

print("=" * 80)
print("JD INTELLIGENCE")
print("=" * 80)

pprint(jd, sort_dicts=False)

print("=" * 80)