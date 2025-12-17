import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Qualification Dashboard", layout="wide")

data = [
    {
        "Name": "Dr. Emily Carter",
        "Title": "Director of Toxicology",
        "Company": "Livera Biotech",
        "Person Location": "Colorado (Remote)",
        "Company HQ": "Cambridge, MA",
        "Funding Stage": "Series B",
        "Published DILI Paper (Last 2Y)": True,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/emilycarter",
        "Email": "emily.carter@liverabiotech.com"
    },
    {
        "Name": "Dr. Sarah Mitchell",
        "Title": "Head of Preclinical Safety",
        "Company": "HepatoRx",
        "Person Location": "Boston, MA",
        "Company HQ": "Boston, MA",
        "Funding Stage": "Series A",
        "Published DILI Paper (Last 2Y)": True,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/sarahmitchell",
        "Email": "sarah.mitchell@hepatorx.com"
    },
    {
        "Name": "Dr. Luca Romano",
        "Title": "VP Safety Assessment",
        "Company": "NeoLiver Therapeutics",
        "Person Location": "Basel, Switzerland",
        "Company HQ": "Basel, Switzerland",
        "Funding Stage": "Series B",
        "Published DILI Paper (Last 2Y)": True,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/lucaromano",
        "Email": "luca.romano@neoliver.com"
    },
    {
        "Name": "Dr. Michael Thompson",
        "Title": "Principal Scientist, Toxicology",
        "Company": "OncoSafe Bio",
        "Person Location": "San Diego, CA",
        "Company HQ": "San Diego, CA",
        "Funding Stage": "Series A",
        "Published DILI Paper (Last 2Y)": False,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/michaelthompson",
        "Email": "michael.thompson@oncosafebio.com"
    },
    {
        "Name": "Dr. Ananya Rao",
        "Title": "Associate Director, Safety Pharmacology",
        "Company": "CardioNova",
        "Person Location": "Remote (India)",
        "Company HQ": "Cambridge, MA",
        "Funding Stage": "Series B",
        "Published DILI Paper (Last 2Y)": False,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/ananyarao",
        "Email": "ananya.rao@cardionova.com"
    },
    {
        "Name": "Dr. James Wilson",
        "Title": "Senior Scientist, Investigative Toxicology",
        "Company": "PharmaCore",
        "Person Location": "New Jersey",
        "Company HQ": "New Jersey",
        "Funding Stage": "Public Company",
        "Published DILI Paper (Last 2Y)": False,
        "Uses In-Vitro / NAMs": False,
        "LinkedIn": "https://linkedin.com/in/jameswilson",
        "Email": "james.wilson@pharmacore.com"
    },
    {
        "Name": "Dr. Sophie Laurent",
        "Title": "Director of Translational Toxicology",
        "Company": "BioLiver SA",
        "Person Location": "Paris, France",
        "Company HQ": "Paris, France",
        "Funding Stage": "Series A",
        "Published DILI Paper (Last 2Y)": True,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/sophielaurent",
        "Email": "sophie.laurent@bioliver.fr"
    },
    {
        "Name": "Dr. Kevin Park",
        "Title": "Head of Safety Sciences",
        "Company": "GenNext Therapeutics",
        "Person Location": "Bay Area, CA",
        "Company HQ": "South San Francisco, CA",
        "Funding Stage": "Series B",
        "Published DILI Paper (Last 2Y)": True,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/kevinpark",
        "Email": "kevin.park@gennexttx.com"
    },
    {
        "Name": "Dr. Maria Gonzalez",
        "Title": "Senior Director, Preclinical Development",
        "Company": "LiverAxis",
        "Person Location": "Madrid, Spain",
        "Company HQ": "Boston, MA",
        "Funding Stage": "Series A",
        "Published DILI Paper (Last 2Y)": False,
        "Uses In-Vitro / NAMs": True,
        "LinkedIn": "https://linkedin.com/in/mariagonzalez",
        "Email": "maria.gonzalez@liveraxis.com"
    },
    {
        "Name": "Dr. Alex Wong",
        "Title": "Junior Scientist",
        "Company": "BioStart",
        "Person Location": "Austin, TX",
        "Company HQ": "Austin, TX",
        "Funding Stage": "Bootstrapped",
        "Published DILI Paper (Last 2Y)": False,
        "Uses In-Vitro / NAMs": False,
        "LinkedIn": "https://linkedin.com/in/alexwong",
        "Email": "alex.wong@biostart.com"
    }
]


df = pd.DataFrame(data)

def calculate_score(row):
    score = 0
    if any(k in row["Title"] for k in ["Director", "Head", "VP"]):
        score += 30
    if row["Published DILI Paper (Last 2Y)"]:
        score += 40
    if row["Funding Stage"] in ["Series A", "Series B"]:
        score += 20
    if row["Uses In-Vitro / NAMs"]:
        score += 15
    if any(hub in row["Company HQ"] for hub in ["Cambridge", "Boston", "Basel", "Bay Area"]):
        score += 10
    return score

df["Probability Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values("Probability Score", ascending=False)
df["Rank"] = range(1, len(df) + 1)

st.title("3D In-Vitro Lead Qualification Dashboard")

search = st.text_input("Search by name, title, company, location or keyword")

if search:
    df = df[df.apply(lambda r: search.lower() in r.astype(str).str.lower().to_string(), axis=1)]

st.dataframe(df, use_container_width=True)

st.download_button(
    label="Download Leads as CSV",
    data=df.to_csv(index=False),
    file_name="qualified_leads.csv",
    mime="text/csv"
)
